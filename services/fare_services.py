import os
import requests

API_KEY = os.getenv("GOOGLE_API_KEY")

def calculate_fare(distance_km: float) -> float:
    base = 3
    per_km = 1.25
    return round(base + distance_km * per_km, 2)


def get_distance_from_google(pickup: str, dropoff: str) -> float:
    """Fetch distance in KM using Google Distance Matrix API"""

    if not API_KEY:
        raise ValueError("Google API key is missing in .env")

    url = (
        "https://maps.googleapis.com/maps/api/distancematrix/json"
        f"?origins={pickup}&destinations={dropoff}&key={API_KEY}"
    )

    response = requests.get(url).json()
    element = response["rows"][0]["elements"][0]

    distance_meters = element["distance"]["value"]
    return distance_meters / 1000
