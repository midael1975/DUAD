from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    username: str
    password: str
    birth_date: str

class CarCreate(BaseModel):
    brand: str
    model: str
    manufacture_year: int

class RentalCreate(BaseModel):
    user_id: int
    car_id: int

class StatusUpdate(BaseModel):
    status: str