import requests

def get_distance_from_osrm(lat1, lon1, lat2, lon2):
    url = f"https://router.project-osrm.org/route/v1/driving/{lon1},{lat1};{lon2},{lat2}"
    params = {"overview": "false"}

    response = requests.get(url, params=params)
    data = response.json()

    if "routes" not in data:
        raise ValueError("OSRM failed to calculate route")

    distance_meters = data["routes"][0]["distance"]

    return distance_meters / 1000  # return KM
