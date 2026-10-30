-- 1. Add a new user
INSERT INTO lyfter_car_rental.users (name, email, username, password, birth_date, account_status) 
VALUES ('Juan Perez', 'juan.perez@email.com', 'jperez_nuevo', 'hashpwd51', '1995-10-15', 'ACTIVE');

-- 2. Add a new car
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) 
VALUES ('Tesla', 'Model 3', 2024, 'AVAILABLE');

-- 3. Change user status
UPDATE lyfter_car_rental.users 
SET account_status = 'SUSPENDED' 
WHERE id = 3;

-- 4. Change car status
UPDATE lyfter_car_rental.cars 
SET car_status = 'MAINTENANCE' 
WHERE id = 4;

-- 5. Generate a new rental
BEGIN;
INSERT INTO lyfter_car_rental.rentals (user_id, car_id, rental_status) 
VALUES (1, 5, 'ACTIVE');

UPDATE lyfter_car_rental.cars 
SET car_status = 'RENTED' 
WHERE id = 5;
COMMIT;

-- 6. Confirm car return (complete rental and set car as available)
BEGIN;
UPDATE lyfter_car_rental.rentals 
SET rental_status = 'COMPLETED' 
WHERE id = 1;

UPDATE lyfter_car_rental.cars 
SET car_status = 'AVAILABLE' 
WHERE id = 5;
COMMIT;

-- 7. Disable a car from rental
UPDATE lyfter_car_rental.cars 
SET car_status = 'OUT_OF_SERVICE' 
WHERE id = 7;

-- 8. Get all rented cars
SELECT * FROM lyfter_car_rental.cars 
WHERE car_status = 'RENTED';

-- 9. Get all available cars
SELECT * FROM lyfter_car_rental.cars 
WHERE car_status = 'AVAILABLE';