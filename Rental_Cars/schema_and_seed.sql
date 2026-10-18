CREATE SCHEMA IF NOT EXISTS lyfter_car_rental;

CREATE TABLE lyfter_car_rental.users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    account_status VARCHAR(20) DEFAULT 'ACTIVE'
);

INSERT INTO lyfter_car_rental.users (name, email, username, password, birth_date, account_status) VALUES
('Ana Silva', 'ana.silva@email.com', 'asilva', 'hashpwd1', '1990-05-12', 'ACTIVE'),
('Carlos Ruiz', 'carlos.ruiz@email.com', 'cruiz', 'hashpwd2', '1985-11-23', 'ACTIVE'),
('Maria Gomez', 'maria.gomez@email.com', 'mgomez', 'hashpwd3', '1992-02-15', 'INACTIVE'),
('Jorge Luna', 'jorge.luna@email.com', 'jluna', 'hashpwd4', '1988-08-30', 'ACTIVE'),
('Lucia Paz', 'lucia.paz@email.com', 'lpaz', 'hashpwd5', '1995-04-10', 'ACTIVE'),
('Pedro Diaz', 'pedro.diaz@email.com', 'pdiaz', 'hashpwd6', '1980-12-05', 'SUSPENDED'),
('Elena Vega', 'elena.vega@email.com', 'evega', 'hashpwd7', '1993-07-21', 'ACTIVE'),
('Raul Mora', 'raul.mora@email.com', 'rmora', 'hashpwd8', '1987-09-14', 'ACTIVE'),
('Sofia Rios', 'sofia.rios@email.com', 'srios', 'hashpwd9', '1996-01-08', 'ACTIVE'),
('Diego Cruz', 'diego.cruz@email.com', 'dcruz', 'hashpwd10', '1991-06-25', 'ACTIVE'),
('Laura Soto', 'laura.soto@email.com', 'lsoto', 'hashpwd11', '1989-10-18', 'ACTIVE'),
('Mario Peña', 'mario.pena@email.com', 'mpena', 'hashpwd12', '1984-03-02', 'INACTIVE'),
('Clara Rey', 'clara.rey@email.com', 'crey', 'hashpwd13', '1994-11-09', 'ACTIVE'),
('Luis Gil', 'luis.gil@email.com', 'lgil', 'hashpwd14', '1986-05-27', 'ACTIVE'),
('Rosa Alba', 'rosa.alba@email.com', 'ralba', 'hashpwd15', '1997-08-11', 'ACTIVE'),
('Hugo Arce', 'hugo.arce@email.com', 'harce', 'hashpwd16', '1982-12-30', 'ACTIVE'),
('Julia Roa', 'julia.roa@email.com', 'jroa', 'hashpwd17', '1998-02-14', 'ACTIVE'),
('Oscar Mas', 'oscar.mas@email.com', 'omas', 'hashpwd18', '1981-04-05', 'SUSPENDED'),
('Diana Sol', 'diana.sol@email.com', 'dsol', 'hashpwd19', '1990-09-22', 'ACTIVE'),
('Pablo Mier', 'pablo.mier@email.com', 'pmier', 'hashpwd20', '1985-01-15', 'ACTIVE'),
('Sara Vaca', 'sara.vaca@email.com', 'svaca', 'hashpwd21', '1992-06-03', 'ACTIVE'),
('Rene Coba', 'rene.coba@email.com', 'rcoba', 'hashpwd22', '1988-11-20', 'ACTIVE'),
('Ines Rico', 'ines.rico@email.com', 'irico', 'hashpwd23', '1995-03-08', 'INACTIVE'),
('Omar Leal', 'omar.leal@email.com', 'oleal', 'hashpwd24', '1983-07-16', 'ACTIVE'),
('Luz Caro', 'luz.caro@email.com', 'lcaro', 'hashpwd25', '1994-12-25', 'ACTIVE'),
('Ivan Mota', 'ivan.mota@email.com', 'imota', 'hashpwd26', '1987-05-09', 'ACTIVE'),
('Gema Lora', 'gema.lora@email.com', 'glora', 'hashpwd27', '1991-08-12', 'ACTIVE'),
('Alex Polo', 'alex.polo@email.com', 'apolo', 'hashpwd28', '1999-10-31', 'ACTIVE'),
('Dora Cano', 'dora.cano@email.com', 'dcano', 'hashpwd29', '1986-02-28', 'SUSPENDED'),
('Saul Vera', 'saul.vera@email.com', 'svera', 'hashpwd30', '1993-04-17', 'ACTIVE'),
('Rita Pato', 'rita.pato@email.com', 'rpato', 'hashpwd31', '1984-09-04', 'ACTIVE'),
('Noel Pela', 'noel.pela@email.com', 'npela', 'hashpwd32', '1996-11-19', 'ACTIVE'),
('Emma Cuna', 'emma.cuna@email.com', 'ecuna', 'hashpwd33', '1989-01-26', 'ACTIVE'),
('Fid Cero', 'fid.cero@email.com', 'fcero', 'hashpwd34', '1982-06-13', 'ACTIVE'),
('Iris Daza', 'iris.daza@email.com', 'idaza', 'hashpwd35', '1997-03-27', 'INACTIVE'),
('Abel Fino', 'abel.fino@email.com', 'afino', 'hashpwd36', '1985-08-05', 'ACTIVE'),
('Nora Gayo', 'nora.gayo@email.com', 'ngayo', 'hashpwd37', '1990-12-10', 'ACTIVE'),
('Tito Haya', 'tito.haya@email.com', 'thaya', 'hashpwd38', '1988-05-22', 'ACTIVE'),
('Olga Jaca', 'olga.jaca@email.com', 'ojaca', 'hashpwd39', '1994-07-06', 'ACTIVE'),
('Beto Kilo', 'beto.kilo@email.com', 'bkilo', 'hashpwd40', '1981-10-14', 'ACTIVE'),
('Alia Lazo', 'alia.lazo@email.com', 'alazo', 'hashpwd41', '1998-01-02', 'ACTIVE'),
('Ciro Mazo', 'ciro.mazo@email.com', 'cmazo', 'hashpwd42', '1986-04-11', 'SUSPENDED'),
('Cleo Nabo', 'cleo.nabo@email.com', 'cnabo', 'hashpwd43', '1992-09-18', 'ACTIVE'),
('Dino Olla', 'dino.olla@email.com', 'dolla', 'hashpwd44', '1983-02-24', 'ACTIVE'),
('Elsa Pelo', 'elsa.pelo@email.com', 'epelo', 'hashpwd45', '1995-06-07', 'ACTIVE'),
('Fito Quio', 'fito.quio@email.com', 'fquio', 'hashpwd46', '1989-11-15', 'ACTIVE'),
('Gina Ramo', 'gina.ramo@email.com', 'gramo', 'hashpwd47', '1991-03-29', 'INACTIVE'),
('Hada Sapo', 'hada.sapo@email.com', 'hsapo', 'hashpwd48', '1987-08-01', 'ACTIVE'),
('Igor Taco', 'igor.taco@email.com', 'itaco', 'hashpwd49', '1999-12-19', 'ACTIVE'),
('Jane Uvas', 'jane.uvas@email.com', 'juvas', 'hashpwd50', '1984-05-08', 'ACTIVE');

CREATE TABLE lyfter_car_rental.cars (
    id SERIAL PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    manufacture_year INT NOT NULL,
    car_status VARCHAR(20) DEFAULT 'AVAILABLE'
);

INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES
('Toyota', 'Corolla', 2022, 'AVAILABLE'),
('Hyundai', 'Elantra', 2021, 'RENTED'),
('Honda', 'Civic', 2023, 'AVAILABLE'),
('Ford', 'Focus', 2020, 'MAINTENANCE'),
('Nissan', 'Sentra', 2022, 'AVAILABLE'),
('Kia', 'Forte', 2021, 'AVAILABLE'),
('Chevrolet', 'Cruze', 2019, 'OUT_OF_SERVICE'),
('Volkswagen', 'Jetta', 2023, 'AVAILABLE'),
('Mazda', 'Mazda3', 2022, 'RENTED'),
('Subaru', 'Impreza', 2021, 'AVAILABLE');

CREATE TABLE lyfter_car_rental.rentals (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    car_id INT NOT NULL,
    rental_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    rental_status VARCHAR(20) DEFAULT 'ACTIVE',
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES lyfter_car_rental.users(id) ON DELETE CASCADE,
    CONSTRAINT fk_car FOREIGN KEY (car_id) REFERENCES lyfter_car_rental.cars(id) ON DELETE RESTRICT
);