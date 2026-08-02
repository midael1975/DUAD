--1. Get all books and their authors (if they have one)

SELECT
    b.ID AS BookID,
    b.Name AS BookName,
    a.Name AS AuthorName
FROM Books b
LEFT JOIN Authors a ON b.Author = a.ID;

--2. Get all books that do not have an author

SELECT
    b.ID,
    b.Name
FROM Books b
WHERE b.Author IS NULL;

--3. Get all authors that do not have any books

SELECT
    a.ID,
    a.Name
FROM Authors a
LEFT JOIN Books b ON a.ID = b.Author
WHERE b.ID IS NULL;

--4. Get all books that have been rented at least once

SELECT DISTINCT
    b.ID,
    b.Name
FROM Books b
INNER JOIN Rents r ON b.ID = r.BookID;

--5. Get all books that have not been rented yet

SELECT
    b.ID,
    b.Name
FROM Books b
LEFT JOIN Rents r ON b.ID = r.BookID
WHERE r.BookID IS NULL;

--6. Get all customers that have rented books

SELECT
    c.ID,
    c.Name,
    c.Email
FROM Customers c
LEFT JOIN Rents r ON c.ID = r.CustomerID
WHERE r.ID IS NULL;

--7. Get all books that have been rented and are currently in Overdue status

SELECT DISTINCT
    b.ID,
    b.Name
FROM Books b
INNER JOIN Rents r ON b.ID = r.BookID
WHERE r.State = 'Overdue';