-- Users table: who can buy
CREATE TABLE users (
    id          SERIAL PRIMARY KEY,
    full_name   TEXT        NOT NULL,
    email       TEXT        NOT NULL UNIQUE,
    created_at  TIMESTAMP   NOT NULL DEFAULT NOW()
);

-- Products table: what we sell
CREATE TABLE products (
    id          SERIAL PRIMARY KEY,
    name        TEXT        NOT NULL,
    sku         TEXT        NOT NULL UNIQUE,
    price       NUMERIC(10,2) NOT NULL CHECK (price >= 0),
    stock       INT         NOT NULL CHECK (stock >= 0),
    created_at  TIMESTAMP   NOT NULL DEFAULT NOW()
);

-- Bills table: invoice header
CREATE TABLE bills (
    id          SERIAL PRIMARY KEY,
    user_id     INT         NOT NULL REFERENCES users(id),
    total       NUMERIC(10,2) NOT NULL CHECK (total >= 0),
    status      TEXT        NOT NULL DEFAULT 'Created', -- later: 'Returned'
    created_at  TIMESTAMP   NOT NULL DEFAULT NOW()
);

-- Bill items: products inside each bill
CREATE TABLE bill_items (
    id          SERIAL PRIMARY KEY,
    bill_id     INT         NOT NULL REFERENCES bills(id) ON DELETE CASCADE,
    product_id  INT         NOT NULL REFERENCES products(id),
    quantity    INT         NOT NULL CHECK (quantity > 0),
    unit_price  NUMERIC(10,2) NOT NULL CHECK (unit_price >= 0),
    line_total  NUMERIC(10,2) NOT NULL CHECK (line_total >= 0)
);
