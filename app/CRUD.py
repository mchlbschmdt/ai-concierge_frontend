from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Property
from .schemas import PropertyCreate

# Create a property
def create_property(db: Session, property: PropertyCreate):
    db_property = Property(
        name=property.name,
        address=property.address,
        price_per_night=property.price_per_night,
        num_bedrooms=property.num_bedrooms,
        num_bathrooms=property.num_bathrooms,
        description=property.description
    )
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

# Get all properties
def get_properties(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Property).offset(skip).limit(limit).all()

# Get a property by ID
def get_property(db: Session, property_id: int):
    return db.query(Property).filter(Property.id == property_id).first()
