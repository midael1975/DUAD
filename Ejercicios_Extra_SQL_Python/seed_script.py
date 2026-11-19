import random
import psycopg2
from faker import Faker

DB_CONFIG = {
    "host": "localhost",
    "database": "lyfter_car_rental",
    "user": "postgres",
    "password": "midael#1975",
    "port": 5432
}


def seed_database(
    num_users=200,
    num_cars=100,
    num_rentals=random.randint(50, 150)
):
    conn = None
    cursor = None

    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        fake = Faker()

        user_ids = []
        car_ids = []

        print("Creating users...")

        # -------------------
        # USERS
        # -------------------
        for _ in range(num_users):

            cursor.execute("""
                INSERT INTO users (
                    name,
                    email,
                    phone_number
                )
                VALUES (%s, %s, %s)
                RETURNING id
            """, (
                fake.name(),
                fake.unique.email(),
                fake.phone_number()
            ))

            user_ids.append(cursor.fetchone()[0])

        print(f"{len(user_ids)} users created.")

        # -------------------
        # CARS
        # -------------------
        print("Creating cars...")

        car_brands = [
            "Toyota",
            "Ford",
            "Honda",
            "Nissan",
            "Hyundai",
            "Kia",
            "Volkswagen",
            "Mazda",
            "Chevrolet",
            "Renault"
        ]

        car_models = [
            "Sedan",
            "SUV",
            "Hatchback",
            "Pickup",
            "Coupe"
        ]

        for _ in range(num_cars):

            cursor.execute("""
                INSERT INTO cars (
                    make,
                    model,
                    year,
                    car_status
                )
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """, (
                random.choice(car_brands),
                random.choice(car_models),
                random.randint(2015, 2025),
                random.choice(["AVAILABLE", "RENTED"])
            ))

            car_ids.append(cursor.fetchone()[0])

        print(f"{len(car_ids)} cars created.")

        # -------------------
        # RENTALS
        # -------------------
        print("Creating rentals...")

        for _ in range(num_rentals):

            user_id = random.choice(user_ids)
            car_id = random.choice(car_ids)

            rental_date = fake.date_between(
                start_date="-2y",
                end_date="today"
            )

            return_date = fake.date_between(
                start_date=rental_date,
                end_date="+30d"
            )

            cursor.execute("""
                INSERT INTO rentals (
                    user_id,
                    car_id,
                    rental_date,
                    return_date
                )
                VALUES (%s, %s, %s, %s)
            """, (
                user_id,
                car_id,
                rental_date,
                return_date
            ))

        print(f"{num_rentals} rentals created.")

        conn.commit()

        print("\nDatabase seeded successfully!")
        print(f"Users: {num_users}")
        print(f"Cars: {num_cars}")
        print(f"Rentals: {num_rentals}")

    except Exception as e:

        if conn:
            conn.rollback()

        print(f"Error seeding database: {e}")

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


if __name__ == "__main__":
    seed_database()