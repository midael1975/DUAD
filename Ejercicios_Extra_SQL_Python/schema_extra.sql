-- ==========================================
-- DATABASE: LYFTER CAR RENTAL
-- ==========================================

-- Create database
CREATE DATABASE lyfter_car_rental;

-- Connect to the database
-- \c lyfter_car_rental

-- ==========================================
-- TABLE: USERS
-- ==========================================

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    phone_number VARCHAR(30)
);

-- ==========================================
-- TABLE: CARS
-- ==========================================

CREATE TABLE cars (
    id SERIAL PRIMARY KEY,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INTEGER NOT NULL,
    car_status VARCHAR(20) NOT NULL
        CHECK (car_status IN ('AVAILABLE', 'RENTED'))
);

-- ==========================================
-- TABLE: RENTALS
-- ==========================================

CREATE TABLE rentals (
    id SERIAL PRIMARY KEY,

    user_id INTEGER NOT NULL,
    car_id INTEGER NOT NULL,

    rental_date DATE NOT NULL,
    return_date DATE,

    CONSTRAINT fk_rentals_user
        FOREIGN KEY (user_id)
        REFERENCES users(id),

    CONSTRAINT fk_rentals_car
        FOREIGN KEY (car_id)
        REFERENCES cars(id)
);