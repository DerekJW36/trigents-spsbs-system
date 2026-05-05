from pydantic import BaseModel, Field
from typing import Optional

class Vehicle(BaseModel):
    year: int = Field(..., description="The manufacturing year of the vehicle, e.g., 2018")
    make: str = Field(..., description="The manufacturer of the vehicle, e.g., Honda, Ford")
    model: str = Field(..., description="The specific model of the vehicle, e.g., Civic, F-150")
    engine_size: Optional[str] = Field(None, description="The engine size or displacement, e.g., 2.0L, V6")
    transmission: Optional[str] = Field(None, description="The transmission type, e.g., Automatic, Manual")

class PartSearchRequest(BaseModel):
    vehicle: Vehicle
    part_name: str = Field(..., description="The name of the automotive part being requested.")
