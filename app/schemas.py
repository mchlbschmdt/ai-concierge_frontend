from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    name: str
    description: str
    related_items: List['Item']  # Forward reference to itself

    class Config:
        from_attributes = True

# Update forward references explicitly
Item.update_forward_refs()
