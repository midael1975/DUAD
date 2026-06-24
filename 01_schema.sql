-- Tabla Products
CREATE TABLE Products (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    code TEXT NOT NULL UNIQUE,
    name varchar(255) NOT NULL,
    price REAL NOT NULL,
    entry_date TEXT NOT NULL,
    brand TEXT,
    stock INTEGER NOT NULL
);

-- Tabla Invoices
CREATE TABLE Invoices (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    invoice_number TEXT NOT NULL UNIQUE,
    purchase_date TEXT NOT NULL,
    buyer_email TEXT NOT NULL,
    total_amount REAL NOT NULL
);

-- Tabla Invoice_Items
CREATE TABLE Invoice_Items (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    invoice_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    total_amount REAL NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES Invoices(id),
    FOREIGN KEY (product_id) REFERENCES Products(id)
);

-- Tabla Shopping_Cart
CREATE TABLE Shopping_Cart (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    buyer_email TEXT NOT NULL
);

-- Tabla Shopping_Cart_Products
CREATE TABLE Shopping_Cart_Products (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    cart_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (cart_id) REFERENCES Shopping_Cart(id),
    FOREIGN KEY (product_id) REFERENCES Products(id)
);
