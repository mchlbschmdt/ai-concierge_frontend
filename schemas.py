from pydantic import BaseModel
from typing import Optional

class PropertyBase(BaseModel):
    name: str
    address: str
    price_per_night: float
    num_bedrooms: int
    num_bathrooms: int
    description: Optional[str] = None

class PropertyCreate(PropertyBase):
    pass

class Property(PropertyBase):
    id: int

    class Config:
        orm_mode = True
