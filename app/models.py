from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)
    price_per_night = Column(Float)
    num_bedrooms = Column(Integer)
    num_bathrooms = Column(Integer)
    description = Column(String)

    def __repr__(self):
        return f"<Property(id={self.id}, name={self.name}, address={self.address})>"

