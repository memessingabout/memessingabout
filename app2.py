#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pathlib import Path
from datetime import datetime, timedelta
import gpxpy, folium, webbrowser
from colorama import init, Fore, Style
import math

init(autoreset=True)

# ----------------------------------------------------------------------
# CONFIG – put your token here (or read from env / config file)
# ----------------------------------------------------------------------
MAPBOX_TOKEN = "YOUR_MAPBOX_TOKEN_HERE"   # <-- replace!

# ----------------------------------------------------------------------
# Helper: Haversine distance (meters)
# ----------------------------------------------------------------------
def haversine(p1, p2):
    lat1, lon1 = math.radians(p1[0]), math.radians(p1[1])
    lat2, lon2 = math.radians(p2[0]), math.radians(p2[1])
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    return 6371000 * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

# ----------------------------------------------------------------------
# 1. Folder / file selection (unchanged, only pathlib)
# ----------------------------------------------------------------------
def get_folder() -> Path:
    p = Path(input(Fore.CYAN + "Folder with GPX files: ").strip())
    if not p.is_dir():
        print(Fore.RED + "Not a directory.")
        sys.exit(1)
    return p

def list_gpx_files(folder: Path):
    files = [f for f in folder.iterdir() if f.suffix.lower() == '.gpx']
    if not files:
        print(Fore.YELLOW + "No GPX files.")
        sys.exit(0)
    return files

def safe_date(name: str) -> str | None:
    try:
        d = name.split('_', 1)[0]
        datetime.strptime(d, '%Y-%m-%d')
        return d
    except Exception:
        return None

def select_date(files):
    date_to_file = {d: f for f in files if (d := safe_date(f.name))}
    dates = sorted(date_to_file)
    print(Fore.CYAN + "\nDates:")
    for i, d in enumerate(dates):
        print(f"{Fore.YELLOW}{i}{Style.RESET_ALL}: {d} → {date_to_file[d].name}")

    while True:
        try:
            idx = int(input(Fore.GREEN + "Choose #: "))
            return {"date": dates[idx], "path": date_to_file[dates[idx]]}
        except (ValueError, IndexError):
            print(Fore.RED + "Invalid number.")

def parse_gpx(path: Path):
    with path.open('r', encoding='utf-8') as f:
        return gpxpy.parse(f)

# ----------------------------------------------------------------------
# 2. Build enriched point list with stats
# ----------------------------------------------------------------------
def enrich_track_points(track):
    """Return list of dicts: lat,lon,time,elev,dist_from_start,speed,duration"""
    points = []
    prev = None
    cumulative_dist = 0.0

    for segment in track.segments:
        for point in segment.points:
            cur = (point.latitude, point.longitude)
            d = {
                "lat": point.latitude,
                "lon": point.longitude,
                "time": point.time,
                "elev": point.elevation,
                "dist": cumulative_dist,
                "speed": None,
                "duration": None,
            }

            if prev and point.time and prev["time"]:
                dist = haversine(prev["latlon"], cur)
                cumulative_dist += dist
                delta_t = (point.time - prev["time"]).total_seconds()
                if delta_t > 0:
                    d["speed"] = dist / delta_t          # m/s
                    d["duration"] = delta_t
                d["dist"] = cumulative_dist

            d["latlon"] = cur
            points.append(d)
            prev = d
    return points

# ----------------------------------------------------------------------
# 3. Create the map
# ----------------------------------------------------------------------
def create_map(gpx, selected_date_str: str, output_path: Path):
    # ---- collect every coordinate for centering ----
    all_coords = []
    enriched_tracks = []

    for track in gpx.tracks:
        enriched = enrich_track_points(track)
        enriched_tracks.append(enriched)
        all_coords.extend([(p["lat"], p["lon"]) for p in enriched])

    for rte in gpx.routes:
        all_coords.extend([(p.latitude, p.longitude) for p in rte.points])

    if not all_coords:
        print(Fore.YELLOW + "No geometry to map.")
        return

    # ---- centre & bounds ----
    lats, lons = zip(*all_coords)
    centre = [sum(lats)/len(lats), sum(lons)/len(lons)]

    m = folium.Map(location=centre, zoom_start=13, tiles=None)   # we add tiles manually

    # -------------------------------------------------
    # 1. Base tile – OpenStreetMap (no token needed)
    # -------------------------------------------------
    folium.TileLayer('OpenStreetMap', name='OSM').add_to(m)

    # -------------------------------------------------
    # 2. Historical traffic layer (Mapbox)
    # -------------------------------------------------
    # Mapbox traffic tiles accept ?date=YYYYMMDD (last 30 days)
    try:
        traffic_date = datetime.strptime(selected_date_str, "%Y-%m-%d").strftime("%Y%m%d")
    except Exception:
        traffic_date = ""

    traffic_url = (
        f"https://api.mapbox.com/v4/mapbox.mapbox-traffic-v1/{{z}}/{{x}}/{{y}}.png"
        f"?access_token={MAPBOX_TOKEN}"
    )
    if traffic_date:
        # Append date only if we have a valid one
        traffic_url += f"&date={traffic_date}"

    folium.TileLayer(
        tiles=traffic_url,
        attr='Mapbox Traffic',
        name='Traffic (historical)',
        overlay=True,
        opacity=0.6,
    ).add_to(m)

    # -------------------------------------------------
    # 3. Track polyline + start/finish markers
    # -------------------------------------------------
    for idx, enriched in enumerate(enriched_tracks):
        if not enriched:
            continue

        coords = [(p["lat"], p["lon"]) for p in enriched]

        # polyline
        folium.PolyLine(
            coords,
            color="red",
            weight=3,
            opacity=0.8,
            popup=f"Track {idx+1}"
        ).add_to(m)

        # ---- START ----
        start = enriched[0]
        folium.Marker(
            [start["lat"], start["lon"]],
            popup=folium.Popup(
                f"<b>START</b><br>"
                f"Time: {start['time'].strftime('%H:%M:%S') if start['time'] else '—'}",
                max_width=300
            ),
            icon=folium.Icon(color="green", icon="play", prefix='fa')
        ).add_to(m)

        # ---- FINISH ----
        finish = enriched[-1]
        folium.Marker(
            [finish["lat"], finish["lon"]],
            popup=folium.Popup(
                f"<b>FINISH</b><br>"
                f"Time: {finish['time'].strftime('%H:%M:%S') if finish['time'] else '—'}<br>"
                f"Total distance: {finish['dist']:.1f} m",
                max_width=300
            ),
            icon=folium.Icon(color="darkred", icon="stop", prefix='fa')
        ).add_to(m)

        # -------------------------------------------------
        # 4. Clickable point markers (circle) with full stats
        # -------------------------------------------------
        for p in enriched:
            if p["time"] is None:
                continue

            # format stats
            speed_kmh = p["speed"] * 3.6 if p["speed"] is not None else None
            stats_html = (
                f"<b>Point @ {p['time'].strftime('%Y-%m-%d %H:%M:%S')}</b><br>"
                f"Lat/Lon: {p['lat']:.6f}, {p['lon']:.6f}<br>"
                f"Elevation: {p['elev'] or '—'} m<br>"
                f"Distance from start: {p['dist']:.1f} m<br>"
                f"Speed: {speed_kmh:.1f} km/h" if speed_kmh else "Speed: —<br>"
                f"Segment duration: {p['duration']:.0f} s" if p['duration'] else ""
            )

            folium.CircleMarker(
                location=[p["lat"], p["lon"]],
                radius=4,
                color="orange",
                fill=True,
                fillOpacity=0.7,
                popup=folium.Popup(stats_html, max_width=350)
            ).add_to(m)

    # -------------------------------------------------
    # 5. Waypoints (unchanged, just nicer icons)
    # -------------------------------------------------
    for wp in gpx.waypoints:
        folium.Marker(
            [wp.latitude, wp.longitude],
            popup=folium.Popup(
                f"<b>{wp.name or 'Waypoint'}</b><br>"
                f"Elev: {wp.elevation or '—'} m<br>"
                f"Time: {wp.time.strftime('%H:%M:%S') if wp.time else '—'}",
                max_width=250
            ),
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)

    # -------------------------------------------------
    # 6. Fit map to data + layer control
    # -------------------------------------------------
    sw = [min(lats), min(lons)]
    ne = [max(lats), max(lons)]
    m.fit_bounds([sw, ne])

    folium.LayerControl().add_to(m)

    # -------------------------------------------------
    # 7. Save
    # -------------------------------------------------
    m.save(str(output_path))
    print(Fore.GREEN + f"Map saved → {output_path}")

# ----------------------------------------------------------------------
# 8. Open map (Windows friendly)
# ----------------------------------------------------------------------
def open_map(path: Path):
    if sys.platform.startswith('win'):
        import os
        os.startfile(str(path))
    else:
        webbrowser.open('file://' + str(path.resolve()))

# ----------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------
def main():
    folder = get_folder()
    files  = list_gpx_files(folder)
    sel    = select_date(files)
    gpx    = parse_gpx(sel["path"])

    # optional console dump (you can comment out)
    print(Fore.MAGENTA + f"\n--- GPX: {sel['path'].name} ---")
    for track in gpx.tracks:
        for seg in track.segments:
            for p in seg.points:
                print(f"{p.latitude:.6f},{p.longitude:.6f} -> {p.elevation or '—'}m @ {p.time}")

    map_file = Path("route_map_traffic.html")
    create_map(gpx, sel["date"], map_file)
    open_map(map_file)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nCancelled.")
    finally:
        input(Fore.CYAN + "\nPress ENTER to exit…")