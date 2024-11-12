-- Eslatma insert into uchun yozilgan exampleni chatgptga yozdirdim ozim yozib chiqishga erindim qolgan hamma narsani ozom yozgaman


-- 1
CREATE TABLE authors (
    author_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    birth_date DATE,
    country VARCHAR(50)
);

CREATE TABLE publishers (
    publisher_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50),
    founded_year INT
);

CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    author_id INT REFERENCES authors(author_id),
    publisher_id INT REFERENCES publishers(publisher_id),
    genre VARCHAR(50),
    publish_date DATE,
    price NUMERIC(10, 2)
);

CREATE TABLE book_reviews (
    review_id SERIAL PRIMARY KEY,
    book_id INT REFERENCES books(book_id),
    review_text TEXT,
    rating INT,
    review_date DATE
);

-- 2
INSERT INTO authors (name, birth_date, country) VALUES
('Gabriel Garcia Marquez', '1927-03-06', 'Colombia'),
('J.K. Rowling', '1965-07-31', 'United Kingdom'),
('Haruki Murakami', '1949-01-12', 'Japan'),
('George Orwell', '1903-06-25', 'United Kingdom'),
('F. Scott Fitzgerald', '1896-09-24', 'United States');

INSERT INTO publishers (name, city, founded_year) VALUES
('Penguin Random House', 'New York', 1927),
('HarperCollins', 'New York', 1989),
('Simon & Schuster', 'New York', 1924),
('Macmillan Publishers', 'London', 1843),
('Hachette Book Group', 'Paris', 1826);

INSERT INTO books (title, author_id, publisher_id, genre, publish_date, price) VALUES
('One Hundred Years of Solitude', 1, 1, 'Magical Realism', '1967-06-05', 15.99),
('Harry Potter and the Philosopher''s Stone', 2, 1, 'Fantasy', '1997-06-26', 9.99),
('Kafka on the Shore', 3, 4, 'Magical Realism', '2002-09-12', 14.99),
('1984', 4, 5, 'Dystopian', '1949-06-08', 8.99),
('The Great Gatsby', 5, 2, 'Classic', '1925-04-10', 10.99),
('Norwegian Wood', 3, 4, 'Romance', '1987-09-04', 12.99),
('Animal Farm', 4, 2, 'Satire', '1945-08-17', 6.99),
('The Catcher in the Rye', 5, 3, 'Classic', '1951-07-16', 7.99),
('Love in the Time of Cholera', 1, 5, 'Romance', '1985-09-07', 11.99),
('Brave New World', 4, 1, 'Dystopian', '1932-08-30', 9.49);

INSERT INTO book_reviews (book_id, review_text, rating, review_date) VALUES
(1, 'Amazing book!', 5, '2023-01-15'),
(2, 'Loved every moment!', 4, '2023-02-20'),
(3, 'A surreal experience.', 5, '2023-03-10'),
(4, 'Very thought-provoking.', 4, '2023-04-12'),
(5, 'A timeless classic.', 5, '2023-05-07');

-- 3

-- SELECT
SELECT * FROM books;

-- Column Aliases
SELECT title AS "Book Title", genre AS "Genre", price AS "Price" FROM books;

-- ORDER BY
SELECT * FROM books ORDER BY price DESC;

-- WHERE
SELECT * FROM books WHERE genre = 'Fantasy';

-- LIMIT va FETCH
SELECT * FROM books LIMIT 3;

-- IN
SELECT * FROM books WHERE genre IN ('Dystopian', 'Romance');

-- BETWEEN
SELECT * FROM books WHERE price BETWEEN 8 AND 12;

-- LIKE
SELECT * FROM books WHERE title LIKE '%World%';

-- IS NULL
SELECT * FROM book_reviews WHERE review_text IS NULL;

-- GROUP BY
SELECT genre, COUNT(*) FROM books GROUP BY genre;

-- 4

-- JOIN
SELECT b.title, a.name AS author_name, p.name AS publisher_name
FROM books b
JOIN authors a ON b.author_id = a.author_id
JOIN publishers p ON b.publisher_id = p.publisher_id;

-- Aggregate funksiyalar
SELECT COUNT(*) AS total_books, AVG(price) AS avg_price, SUM(price) AS total_price FROM books;
