from pydantic import BaseModel

class FareResponse(BaseModel):
    pickup: str
    dropoff: str
    distance_km: float
    fare_estimate: str
