from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Cow Model
class Cow(Base):
    __tablename__ = 'cows'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    breed = Column(String, nullable=False)
    
    # Relationship to LactationRecord
    lactation_records = relationship("LactationRecord", back_populates="cow", cascade="all, delete-orphan")
    # Relationship to SalesRecord
    sales_records = relationship("SalesRecord", back_populates="cow", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Cow(name={self.name}, breed={self.breed})>"
    
# LactationRecord Model
class LactationRecord(Base):
    __tablename__ = 'lactation_records'
    
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    milk_produced = Column(Float, nullable=False)  # Amount of milk produced in liters
    cow_id = Column(Integer, ForeignKey('cows.id'), nullable=False)
    
    # Relationship to Cow
    cow = relationship("Cow", back_populates="lactation_records")

    def __repr__(self):
        return f"<LactationRecord(cow={self.cow.name}, date={self.date}, milk_produced={self.milk_produced})>"
    
# Employee Model
class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    
    # Relationship to SalesRecord
    sales_records = relationship("SalesRecord", back_populates="employee", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Employee(name={self.name}, position={self.position})>"
