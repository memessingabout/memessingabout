# get_uber_trips.py
import requests
import json
import pandas as pd
from datetime import datetime
import polyline  # Google polyline decoder

# === CONFIG ===
SID = "PASTE_YOUR_SID_VALUE_HERE"
CSID = "PASTE_YOUR_CSID_VALUE_HERE"
JWT_SESSION = "PASTE_YOUR_jwt-session_VALUE_HERE"  # Optional backup
OUTPUT_CSV = "uber_trips_full.csv"

# For drivers: https://drivers.uber.com
# For riders: Change BASE_URL to "https://riders.uber.com/api" if needed
BASE_URL = "https://cn-geo1.uber.com/rt/trips-graphql"

session = requests.Session()
session.cookies.set("sid", SID)
session.cookies.set("csid", CSID)
if JWT_SESSION:
    session.cookies.set("jwt-session", JWT_SESSION)

session.headers.update({
    "content-type": "application/json",
    "x-uber-request-id": "manual-script-v2",
    "origin": "https://drivers.uber.com",
    "referer": "https://drivers.uber.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",  # Match Brave's UA
})

def fetch_all_trips():
    query = """
    query TripsHistory($after: ID, $count: Int, $filters: TripsHistoryFilters) {
      tripsHistory(after: $after, first: $count, filters: $filters) {
        edges {
          node {
            uuid
            requestTime
            beginTripTime
            dropoffTime
            fare { amount currency }
            distance { value unit }
            route { encodedPolyline }
            beginTripLatLng { latitude longitude }
            dropoffLatLng { latitude longitude }
          }
        }
        pageInfo { hasNextPage endCursor }
      }
    }
    """

    all_trips = []
    cursor = None
    count = 50

    print("Fetching trips...")
    while True:
        variables = {
            "after": cursor,
            "count": count,
            "filters": {}  # Add {"dateRange": {"start": "2025-10-01", "end": "2025-10-30"}} for date filter
        }
        payload = {
            "operationName": "TripsHistory",
            "variables": variables,
            "query": query
        }

        try:
            r = session.post(BASE_URL, json=payload, timeout=30)
            print(f"Status: {r.status_code} | Response: {r.text[:200]}...")  # Debug: Check for errors
            r.raise_for_status()
            data = r.json()
            if "errors" in data:
                print(f"GraphQL Error: {data['errors']}")
                break
        except Exception as e:
            print(f"Request failed: {e}")
            break

        trips = data.get("data", {}).get("tripsHistory", {})
        if not trips:
            print("No trips data - check cookies or URL.")
            break

        edges = trips.get("edges", [])
        for edge in edges:
            n = edge["node"]
            all_trips.append({
                "trip_id": n["uuid"],
                "request_time": n["requestTime"],
                "start_time": n["beginTripTime"],
                "end_time": n["dropoffTime"],
                "fare": f"{n['fare']['amount']} {n['fare']['currency']}",
                "distance": f"{n['distance']['value']} {n['distance']['unit']}",
                "start_lat": n["beginTripLatLng"]["latitude"],
                "start_lng": n["beginTripLatLng"]["longitude"],
                "end_lat": n["dropoffLatLng"]["latitude"],
                "end_lng": n["dropoffLatLng"]["longitude"],
                "encoded_polyline": n["route"]["encodedPolyline"],
            })

        page_info = trips.get("pageInfo", {})
        if not page_info.get("hasNextPage"):
            break
        cursor = page_info["endCursor"]
        print(f"   Fetched {len(all_trips)} trips so far...")

    return all_trips

# === RUN ===
trips = fetch_all_trips()
df = pd.DataFrame(trips)

if not df.empty:
    # Decode polyline to list of (lat, lng)
    df["route_points"] = df["encoded_polyline"].apply(
        lambda x: polyline.decode(x) if x and pd.notna(x) else []
    )
    # Save
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"\nDone! {len(df)} trips saved to {OUTPUT_CSV}")
else:
    print("No trips fetched - see debug output above.")