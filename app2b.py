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
# CONFIG & SETTINGS
# ----------------------------------------------------------------------
SETTINGS_FILE = Path("settings.json")
MAPS_DIR = Path("maps")
MAPS_DIR.mkdir(exist_ok=True)

# Load or create settings
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
# Helper: Haversine (meters)
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
# 4. Enrich track with speed (m/s)
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
# 5. Create Color-Graded Polyline (speed → color)
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
# 6. Build Map
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

    # Process routes (static blue line)
    route_coords = [(p.latitude, p.longitude) for r in gpx.routes for p in r.points]
    if route_coords:
        all_coords.extend(route_coords)

    if not all_coords:
        print("No track/route data to display.")
        return

    # Center map
    lats, lons = zip(*all_coords)
    center = [sum(lats)/len(lats), sum(lons)/len(lons)]

    # Create map
    m = folium.Map(
        location=center,
        zoom_start=13,
        tiles='Stamen Terrain'  # Beautiful, no token
    )

    # Fit to bounds
    sw = [min(lats), min(lons)]
    ne = [max(lats), max(lons)]
    m.fit_bounds([sw, ne], padding=(10, 10))

    # Add speed-colored track segments
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

    # Start / Finish markers
    if track_segments:
        first = track_segments[0][0][0]  # first point of first segment
        last = track_segments[-1][0][-1]  # last point of last segment

        folium.Marker(
            first,
            popup=folium.Popup("<b>START</b>", max_width=100),
            icon=folium.Icon(color="green", icon="play", prefix='fa')
        ).add_to(m)

        folium.Marker(
            last,
            popup=folium.Popup("<b>FINISH</b>", max_width=100),
            icon=folium.Icon(color="darkred", icon="stop", prefix='fa')
        ).add_to(m)

    # Waypoints
    for wp in gpx.waypoints:
        folium.CircleMarker(
            [wp.latitude, wp.longitude],
            radius=6,
            color="purple",
            fill=True,
            popup=folium.Popup(f"<b>{wp.name}</b>", max_width=200)
        ).add_to(m)

    # Legend (HTML)
    legend_html = '''
    <div style="position: fixed; bottom: 50px; left: 50px; width: 140px; height: 160px;
                background: white; border:2px solid grey; z-index:9999; padding: 10px;
                font-size: 14px; border-radius: 8px;">
      <b>Speed Legend</b><br>
      <i style="background:#00ff00; width:12px; height:12px; display:inline-block;"></i> &lt;5 km/h<br>
      <i style="background:#88ff00"></i> 5–15 km/h<br>
      <i style="background:#ffff00"></i> 15–30 km/h<br>
      <i style="background:#ff8800"></i> 30–50 km/h<br>
      <i style="background:#ff0000"></i> &gt;50 km/h<br>
      <hr style="margin:5px 0">
      <small><!-- Living on Love ❤️ --></small>
    </div>
    '''
    m.get_root().html.add_child(folium.Element(legend_html))

    # Sign HTML
    sign = "<!-- Living on Love ❤️ -->"
    m.get_root().html.add_child(folium.Element(sign))

    # Save with overwrite check
    if output_path.exists():
        print(f"File exists: {output_path.name}")
        choice = input("Overwrite? (y/N): ").strip().lower()
        if choice != 'y':
            print("Cancelled.")
            return

    m.save(str(output_path))
    print(f"Map saved: {output_path}")

    # Sign the GPX file too
    gpx_path = Path(gpx.get_source()) if hasattr(gpx, 'get_source') else None
    if gpx_path and gpx_path.exists():
        try:
            content = gpx_path.read_text(encoding='utf-8')
            if "<!-- Living on Love ❤️ -->" not in content:
                content += "\n<!-- Living on Love ❤️ -->\n"
                gpx_path.write_text(content, encoding='utf-8')
        except:
            pass  # best effort

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

    # Dynamic HTML filename
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