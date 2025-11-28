from fastapi import APIRouter
from utils.validators import validate_inputs
from services.fare_services import calculate_fare
from services.geocoding_services import geocode_address
from services.osrm_services import get_distance_from_osrm
from models.fare_models import FareResponse

router = APIRouter(prefix="/fare", tags=["Fare Estimation"])

# Mock route stays the same
@router.get("/mock", response_model=FareResponse)
def mock_fare(pickup: str, dropoff: str):
    validate_inputs(pickup, dropoff)
    distance_km = 25.0
    fare = calculate_fare(distance_km)

    return FareResponse(
        pickup=pickup,
        dropoff=dropoff,
        distance_km=distance_km,
        fare_estimate=f"£{fare}"
    )


# REAL fare route — OSRM + Nominatim
@router.get("/", response_model=FareResponse)
def live_fare(pickup: str, dropoff: str):
    validate_inputs(pickup, dropoff)

    # Convert to lat/lon
    lat1, lon1 = geocode_address(pickup)
    lat2, lon2 = geocode_address(dropoff)

    # Get driving distance from OSRM
    distance_km = get_distance_from_osrm(lat1, lon1, lat2, lon2)

    # Calculate fare
    fare = calculate_fare(distance_km)

    return FareResponse(
        pickup=pickup,
        dropoff=dropoff,
        distance_km=round(distance_km, 2),
        fare_estimate=f"£{fare}"
    )
