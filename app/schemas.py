from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str

    class Config:
        from_attributes = True

