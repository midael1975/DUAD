-- 1. All products
SELECT * FROM Products;

-- 2. Products with a price greater than 50000
SELECT * FROM Products
WHERE price > 50000;

-- 3. All purchases of the same product by its ID
SELECT * FROM Invoice_Items
WHERE product_id = 1;

-- 4. Purchases grouped by product (total quantity purchased)
SELECT product_id, SUM(quantity) AS total_purchased
FROM Invoice_Items
GROUP BY product_id;

-- 5. All invoices made by the same buyer
SELECT * FROM Invoices
WHERE buyer_email = 'correo@ejemplo.com';

-- 6. Invoices ordered by total amount in descending order
SELECT * FROM Invoices
ORDER BY total_amount DESC;

-- 7. Get a single invoice by its invoice number
SELECT * FROM Invoices
WHERE invoice_number = 'FAC-001';
