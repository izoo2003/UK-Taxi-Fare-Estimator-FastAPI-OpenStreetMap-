import requests

def geocode_address(address: str):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }

    response = requests.get(url, params=params, headers={"User-Agent": "Mozilla/5.0"})
    data = response.json()

    if not data:
        raise ValueError(f"Location not found: {address}")

    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])

    return lat, lon
