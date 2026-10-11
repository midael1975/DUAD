from fastapi import FastAPI, Request
from database import PgManager
from models import UserCreate, CarCreate, RentalCreate, StatusUpdate
from repositories import UserRepository, CarRepository, RentalRepository

app = FastAPI(title="Lyfter Car Rental API")

# 1. Instantiate your optimized PgManager
db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="midael#1975",
    host="localhost",
    port=5432,
)

# 2. Pass the manager as a dependency to each repository[cite: 1]
user_repo = UserRepository(db_manager)
car_repo = CarRepository(db_manager)
rental_repo = RentalRepository(db_manager)

# --- CREATION ENDPOINTS ---
@app.post("/api/users")
def create_user(user: UserCreate):
    user_repo.create(user)
    return {"message": "User created successfully"}

@app.post("/api/cars")
def create_car(car: CarCreate):
    car_repo.create(car)
    return {"message": "Car created successfully"}

@app.post("/api/rentals")
def create_rental(rental: RentalCreate):
    rental_repo.create(rental)
    return {"message": "Rental registered and car updated successfully"}

# --- MODIFICATION ENDPOINTS ---
@app.patch("/api/cars/{car_id}/status")
def change_car_status(car_id: int, data: StatusUpdate):
    car_repo.update_status(car_id, data.status)
    return {"message": f"Car status updated to {data.status}"}

@app.patch("/api/users/{user_id}/status")
def change_user_status(user_id: int, data: StatusUpdate):
    user_repo.update_status(user_id, data.status)
    return {"message": f"User status updated to {data.status}"}

@app.patch("/api/users/{user_id}/moroso")
def flag_user_moroso(user_id: int):
    user_repo.update_status(user_id, 'MOROSO')
    return {"message": "User flagged as defaulter"}

@app.patch("/api/rentals/{rental_id}/status")
def change_rental_status(rental_id: int, data: StatusUpdate):
    rental_repo.update_status(rental_id, data.status)
    return {"message": f"Rental status changed to {data.status}"}

@app.patch("/api/rentals/{rental_id}/complete")
def complete_rental(rental_id: int, car_id: int):
    rental_repo.update_status(rental_id, 'COMPLETED', car_id)
    return {"message": "Rental completed and car is now available"}

# --- LISTING ENDPOINTS ---
@app.get("/api/users")
def list_users(request: Request):
    filters = dict(request.query_params)
    return user_repo.get_all(filters)

@app.get("/api/cars")
def list_cars(request: Request):
    filters = dict(request.query_params)
    return car_repo.get_all(filters)

@app.get("/api/rentals")
def list_rentals(request: Request):
    filters = dict(request.query_params)
    return rental_repo.get_all(filters)