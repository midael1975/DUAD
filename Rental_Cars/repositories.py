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

    def update_status(self, user_id: int, status: str):
        query = "UPDATE lyfter_car_rental.users SET account_status = %s WHERE id = %s"
        self.db.execute_query(query, (status, user_id))

    def get_all(self, filters: dict):
        base_query = "SELECT id, name, email, username, account_status FROM lyfter_car_rental.users"
        query, params = self._build_filter_query(base_query, filters)
        return self.db.execute_query(query, params)

class CarRepository(BaseRepository):
    def create(self, car):
        query = """INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year) 
                   VALUES (%s, %s, %s)"""
        self.db.execute_query(query, (car.brand, car.model, car.manufacture_year))

    def update_status(self, car_id: int, status: str):
        query = "UPDATE lyfter_car_rental.cars SET car_status = %s WHERE id = %s"
        self.db.execute_query(query, (status, car_id))

    def get_all(self, filters: dict):
        base_query = "SELECT * FROM lyfter_car_rental.cars"
        query, params = self._build_filter_query(base_query, filters)
        return self.db.execute_query(query, params)

class RentalRepository(BaseRepository):
    def create(self, rental):
        try:
            self.db.execute_query("BEGIN;")
            query = "INSERT INTO lyfter_car_rental.rentals (user_id, car_id) VALUES (%s, %s)"
            self.db.execute_query(query, (rental.user_id, rental.car_id))
            
            update_car = "UPDATE lyfter_car_rental.cars SET car_status = 'RENTED' WHERE id = %s"
            self.db.execute_query(update_car, (rental.car_id,))
            self.db.execute_query("COMMIT;")
            return True
        except Exception:
            self.db.execute_query("ROLLBACK;")
            return False

    def update_status(self, rental_id: int, status: str, car_id: int = None):
        try:
            self.db.execute("BEGIN;")
            query = "UPDATE lyfter_car_rental.rentals SET rental_status = %s WHERE id = %s"
            self.db.execute_query(query, (status, rental_id))
            
            if status == 'COMPLETED' and car_id:
                update_car = "UPDATE lyfter_car_rental.cars SET car_status = 'AVAILABLE' WHERE id = %s"
                self.db.execute_query(update_car, (car_id,))
                
            self.db.execute_query("COMMIT;")
        except Exception:
            self.db.execute_query("ROLLBACK;")

    def get_all(self, filters: dict):
        base_query = "SELECT * FROM lyfter_car_rental.rentals"
        query, params = self._build_filter_query(base_query, filters)
        return self.db.execute_query(query, params)