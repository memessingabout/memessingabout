#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import math
from pathlib import Path
from datetime import datetime
import gpxpy
import folium
import webbrowser

# ----------------------------------------------------------------------
# SETTINGS & FOLDERS
# ----------------------------------------------------------------------
SETTINGS_FILE = Path("settings.json")
MAPS_DIR = Path("maps")
MAPS_DIR.mkdir(exist_ok=True)

def load_settings():
    if SETTINGS_FILE.exists():
        try:
            with SETTINGS_FILE.open('r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    return {"last_folder": ""}

def save_settings(data):
    with SETTINGS_FILE.open('w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

settings = load_settings()

# ----------------------------------------------------------------------
# HELPER: Haversine distance (meters)
# ----------------------------------------------------------------------
def haversine(p1, p2):
    lat1, lon1 = math.radians(p1[0]), math.radians(p1[1])
    lat2, lon2 = math.radians(p2[0]), math.radians(p2[1])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    return 6371000 * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

# ----------------------------------------------------------------------
# 1. Get GPX Folder (with memory)
# ----------------------------------------------------------------------
def get_folder() -> Path:
    default = settings.get("last_folder", "")
    prompt = f"GPX folder [{default}]: " if default else "GPX folder: "
    user_input = input(prompt).strip()
    folder_path = Path(user_input) if user_input else Path(default)

    if not folder_path.is_dir():
        print("Invalid folder. Try again.")
        return get_folder()

    settings["last_folder"] = str(folder_path.resolve())
    save_settings(settings)
    return folder_path

# ----------------------------------------------------------------------
# 2. List & Select GPX
# ----------------------------------------------------------------------
def list_gpx_files(folder: Path):
    files = [f for f in folder.iterdir() if f.suffix.lower() == '.gpx']
    if not files:
        print("No GPX files found.")
        sys.exit(0)
    return files

def safe_date(name: str) -> str | None:
    try:
        d = name.split('_', 1)[0]
        datetime.strptime(d, '%Y-%m-%d')
        return d
    except:
        return None

def select_date(files):
    date_to_file = {}
    for f in files:
        if (d := safe_date(f.name)):
            date_to_file[d] = f

    dates = sorted(date_to_file.keys())
    if not dates:
        print("No valid dated GPX files.")
        sys.exit(0)

    print("\nAvailable dates:")
    for i, d in enumerate(dates):
        print(f"  {i}: {d}  →  {date_to_file[d].name}")

    while True:
        try:
            idx = int(input("\nChoose number: "))
            selected_date = dates[idx]
            return {
                "date": selected_date,
                "path": date_to_file[selected_date]
            }
        except (ValueError, IndexError):
            print("Invalid choice.")

# ----------------------------------------------------------------------
# 3. Parse GPX
# ----------------------------------------------------------------------
def parse_gpx(path: Path):
    with path.open('r', encoding='utf-8') as f:
        return gpxpy.parse(f)

# ----------------------------------------------------------------------
# 4. Enrich track with speed
# ----------------------------------------------------------------------
def enrich_track(track):
    points = []
    prev = None
    for segment in track.segments:
        for point in segment.points:
            cur = (point.latitude, point.longitude)
            speed = None
            if prev and point.time and prev["time"]:
                dist = haversine(prev["coord"], cur)
                dt = (point.time - prev["time"]).total_seconds()
                if dt > 0:
                    speed = dist / dt  # m/s
            points.append({
                "coord": cur,
                "time": point.time,
                "elev": point.elevation,
                "speed": speed
            })
            prev = points[-1]
    return points

# ----------------------------------------------------------------------
# 5. Speed → Color
# ----------------------------------------------------------------------
def speed_to_color(speed_mps):
    if speed_mps is None:
        return "gray"
    kmh = speed_mps * 3.6
    if kmh < 5:   return "#00ff00"  # green
    if kmh < 15:  return "#88ff00"
    if kmh < 30:  return "#ffff00"  # yellow
    if kmh < 50:  return "#ff8800"  # orange
    return "#ff0000"  # red

# ----------------------------------------------------------------------
# 6. Create Map with Legend & Popups
# ----------------------------------------------------------------------
def create_map(gpx, date_str: str, output_path: Path):
    all_coords = []
    track_segments = []

    # Process tracks
    for track in gpx.tracks:
        enriched = enrich_track(track)
        if len(enriched) < 2:
            continue
        coords = [p["coord"] for p in enriched]
        all_coords.extend(coords)
        track_segments.append((coords, enriched))

    # Process routes
    route_coords = [(p.latitude, p.longitude) for r in gpx.routes for p in r.points]
    if route_coords:
        all_coords.extend(route_coords)

    if not all_coords:
        print("No track/route data to display.")
        return

    # Center
    lats, lons = zip(*all_coords)
    center = [sum(lats)/len(lats), sum(lons)/len(lons)]

    # Map
    m = folium.Map(location=center, zoom_start=13, tiles=None)

    # Stamen Terrain with attribution
    folium.TileLayer(
        tiles='Stamen Terrain',
        attr='Map tiles by <a href="http://stamen.com">Stamen Design</a>, '
             'under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. '
             'Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, '
             'under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.',
        name='Terrain'
    ).add_to(m)

    # Fit bounds
    sw = [min(lats), min(lons)]
    ne = [max(lats), max(lons)]
    m.fit_bounds([sw, ne], padding=(10, 10))

    # Speed-colored segments
    for coords, enriched in track_segments:
        for i in range(len(coords) - 1):
            segment = [coords[i], coords[i+1]]
            speed = enriched[i+1]["speed"]
            color = speed_to_color(speed)
            folium.PolyLine(
                segment,
                color=color,
                weight=4,
                opacity=0.9
            ).add_to(m)

    # Start & Finish with POPUPS
    if track_segments:
        first_point = track_segments[0][1][0]
        last_point = track_segments[-1][1][-1]

        start_popup = f"""
        <div style="font-size:14px; font-weight:bold;">
            START<br>
            Time: {first_point['time'].strftime('%H:%M:%S') if first_point['time'] else '—'}<br>
            Elev: {first_point['elev'] or '—'} m
        </div>
        """
        folium.Marker(
            first_point["coord"],
            popup=folium.Popup(start_popup, max_width=200),
            icon=folium.Icon(color="green", icon="play", prefix='fa')
        ).add_to(m)

        total_dist = last_point.get("dist", 0)
        if total_dist == 0 and track_segments:
            total_dist = sum(
                haversine(coords[i], coords[i+1])
                for seg_coords, _ in track_segments
                for i in range(len(seg_coords)-1)
            )

        finish_popup = f"""
        <div style="font-size:14px; font-weight:bold;">
            FINISH<br>
            Time: {last_point['time'].strftime('%H:%M:%S') if last_point['time'] else '—'}<br>
            Elev: {last_point['elev'] or '—'} m<br>
            Total: {total_dist/1000:.2f} km
        </div>
        """
        folium.Marker(
            last_point["coord"],
            popup=folium.Popup(finish_popup, max_width=200),
            icon=folium.Icon(color="darkred", icon="stop", prefix='fa')
        ).add_to(m)

    # Waypoints
    for wp in gpx.waypoints:
        folium.CircleMarker(
            [wp.latitude, wp.longitude],
            radius=6,
            color="purple",
            fill=True,
            popup=folium.Popup(f"<b>{wp.name or 'Waypoint'}</b>", max_width=200)
        ).add_to(m)

    # Speed Legend (clickable, beautiful)
    legend_html = '''
    <div id="speed-legend" style="position: fixed; bottom: 20px; left: 20px; width: 160px; 
         background: white; border:2px solid #555; border-radius: 8px; 
         padding: 12px; font-family: Arial; font-size: 13px; box-shadow: 0 0 10px rgba(0,0,0,0.3);
         z-index: 1000; cursor: pointer;" onclick="this.style.display='none';">
      <b style="display:block; margin-bottom:8px;">Speed Legend</b>
      <div><i style="background:#00ff00;width:12px;height:12px;display:inline-block;border-radius:50%;"></i> &lt;5 km/h</div>
      <div><i style="background:#88ff00;"></i> 5–15 km/h</div>
      <div><i style="background:#ffff00;"></i> 15–30 km/h</div>
      <div><i style="background:#ff8800;"></i> 30–50 km/h</div>
      <div><i style="background:#ff0000;"></i> &gt;50 km/h</div>
      <hr style="margin:8px 0; border:0; border-top:1px solid #ddd;">
      <small style="color:#777;">Click to hide</small>
      <br><small><!-- Living on Love ❤️ --></small>
    </div>
    '''
    m.get_root().html.add_child(folium.Element(legend_html))

    # Sign HTML
    m.get_root().html.add_child(folium.Element("<!-- Living on Love ❤️ -->"))

    # Overwrite check
    if output_path.exists():
        print(f"File exists: {output_path.name}")
        choice = input("Overwrite? (y/N): ").strip().lower()
        if choice != 'y':
            print("Cancelled.")
            return

    m.save(str(output_path))
    print(f"Map saved: {output_path}")

    # Sign GPX file
    try:
        gpx_path = Path(gpx.get_source()) if hasattr(gpx, 'get_source') else None
        if gpx_path and gpx_path.exists():
            content = gpx_path.read_text(encoding='utf-8')
            if "<!-- Living on Love ❤️ -->" not in content:
                content += "\n<!-- Living on Love ❤️ -->\n"
                gpx_path.write_text(content, encoding='utf-8')
    except:
        pass

# ----------------------------------------------------------------------
# 7. Open Map
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
    files = list_gpx_files(folder)
    sel = select_date(files)
    gpx = parse_gpx(sel["path"])

    html_name = f"{sel['date']}_route.html"
    output_path = MAPS_DIR / html_name

    create_map(gpx, sel["date"], output_path)
    if output_path.exists():
        open_map(output_path)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nCancelled.")
    finally:
        input("\nPress ENTER to exit...")