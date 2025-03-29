from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_property, get_properties, get_property
from schemas import PropertyCreate, Property

# Initialize FastAPI app
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to create a property
@app.post("/properties/", response_model=Property)
def add_property(property: PropertyCreate, db: Session = Depends(get_db)):
    return create_property(db=db, property=property)

# Route to get all properties
@app.get("/properties/", response_model=list[Property])
def list_properties(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    properties = get_properties(db=db, skip=skip, limit=limit)
    return properties

# Route to get a single property by ID
@app.get("/properties/{property_id}", response_model=Property)
def read_property(property_id: int, db: Session = Depends(get_db)):
    db_property = get_property(db=db, property_id=property_id)
    if db_property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return db_property
