class BaseRepository:
    def __init__(self, db_manager):
        self.db = db_manager

    def _build_filter_query(self, base_query: str, filters: dict) -> tuple:
        if not filters:
            return base_query, ()
        
        conditions = []
        params = []
        for column, value in filters.items():
            conditions.append(f"{column} = %s")
            params.append(value)
            
        final_query = base_query + " WHERE " + " AND ".join(conditions)
        return final_query, tuple(params)

class UserRepository(BaseRepository):
    def create(self, user) -> bool:
        try:
            query = """INSERT INTO lyfter_car_rental.users (name, email, username, password, birth_date) 
                       VALUES (%s, %s, %s, %s, %s)"""
            self.db.execute_query(query, (user.name, user.email, user.username, user.password, user.birth_date))
            return True
        except Exception as e:
            print(f"Error creando usuario: {e}")
            return False

    def update_status(self, user_id: int, status: str) -> bool:
        try:
            query = "UPDATE lyfter_car_rental.users SET account_status = %s WHERE id = %s"
            self.db.execute_query(query, (status, user_id))
            return True
        except Exception as e:
            print(f"Error updating user status: {e}")
            return False

    def get_all(self, filters: dict):
        base_query = "SELECT id, name, email, username, account_status FROM lyfter_car_rental.users"
        query, params = self._build_filter_query(base_query, filters)
        return self.db.execute_query(query, params)

class CarRepository(BaseRepository):
    def create(self, car) -> bool:
        try:
            query = """INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year) 
                       VALUES (%s, %s, %s)"""
            self.db.execute_query(query, (car.brand, car.model, car.manufacture_year))
            return True
        except Exception as e:
            print(f"Error creating car: {e}")
            return False

    def update_status(self, car_id: int, status: str) -> bool:
        try:
            query = "UPDATE lyfter_car_rental.cars SET car_status = %s WHERE id = %s"
            self.db.execute_query(query, (status, car_id))
            return True
        except Exception as e:
            print(f"Error updating car status: {e}")
            return False

    def get_all(self, filters: dict):
        base_query = "SELECT * FROM lyfter_car_rental.cars"
        query, params = self._build_filter_query(base_query, filters)
        return self.db.execute_query(query, params)

class RentalRepository(BaseRepository):
    def create(self, rental) -> bool:
        try:
            # 1. We verify that the car exists and is AVAILABLE before renting it
            check_car_query = "SELECT car_status FROM lyfter_car_rental.cars WHERE id = %s"
            car_result = self.db.execute_query(check_car_query, (rental.car_id,))

            if not car_result or car_result[0]["car_status"] != "AVAILABLE":
                return False

            # 2. We initiate a transaction to register the rental and change the car's status
            self.db.execute_query("BEGIN;")
            query = "INSERT INTO lyfter_car_rental.rentals (user_id, car_id) VALUES (%s, %s)"
            self.db.execute_query(query, (rental.user_id, rental.car_id))

            update_car = "UPDATE lyfter_car_rental.cars SET car_status = 'RENTED' WHERE id = %s"
            self.db.execute_query(update_car, (rental.car_id,))
            self.db.execute_query("COMMIT;")
            return True
        except Exception:
            self.db.execute_query("ROLLBACK;")
            print("Error creating rental or updating car status")
            return False

    def update_status(self, rental_id: int, status: str) -> bool:
        try:
            # 1. We obtain the car_id directly from the database based on the rental_id
            rental_query = "SELECT car_id FROM lyfter_car_rental.rentals WHERE id = %s"
            rental_result = self.db.execute_query(rental_query, (rental_id,))

            if not rental_result:
                return False

            car_id = rental_result[0]["car_id"]

            #2. We use execute_query (fixing the error of self.db.execute)
            self.db.execute_query("BEGIN;")
            query = "UPDATE lyfter_car_rental.rentals SET rental_status = %s WHERE id = %s"
            self.db.execute_query(query, (status, rental_id))

            if status == 'COMPLETED' and car_id:
                update_car = "UPDATE lyfter_car_rental.cars SET car_status = 'AVAILABLE' WHERE id = %s"
                self.db.execute_query(update_car, (car_id,))

            self.db.execute_query("COMMIT;")
            return True
        except Exception as e:
            self.db.execute_query("ROLLBACK;")
            print(f"Error updating rental status: {e}")
            return False

    def get_all(self, filters: dict):
        base_query = "SELECT * FROM lyfter_car_rental.rentals"
        query, params = self._build_filter_query(base_query, filters)
        return self.db.execute_query(query, params)