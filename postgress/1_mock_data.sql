INSERT INTO statuses (id, name, slug) VALUES
(1, 'Nou', 'nou');

-- Restablecer la secuencia para la tabla statuses en PostgreSQL
SELECT SETVAL('statuses_id_seq', (SELECT MAX(id) FROM statuses));

-- Insertar registros en la tabla categories
INSERT INTO categories (id, name, slug) VALUES
(1, 'Electrònica', 'electronica'),
(2, 'Roba', 'roba'),
(3, 'Joguines', 'joguines');

-- Restablecer la secuencia para la tabla categories en PostgreSQL
SELECT SETVAL('categories_id_seq', (SELECT MAX(id) FROM categories));

-- Insertar registros en la tabla users
INSERT INTO users (id, name, email, role, verified, password) VALUES
(1, 'Joan Pérez', 'joan@example.com', 'admin', TRUE, 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4'),
(2, 'Anna García', 'anna@example.com', 'moderator', TRUE, 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4'),
(3, 'Elia Rodríguez', 'elia@example.com', 'wanner', TRUE, 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4'),
(4, 'Kevin Salardú', 'kevin@example.com', 'wanner', TRUE, 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4');

-- Restablecer la secuencia para la tabla users en PostgreSQL
SELECT SETVAL('users_id_seq', (SELECT MAX(id) FROM users));

-- Insertar registros en la tabla products
INSERT INTO products (id, title, description, photo, price, category_id, status_id, seller_id) VALUES
(1, 'Telèfon mòbil', 'Un telèfon intel·ligent d''última generació.', 'no_image.png', 599.99, 1, 1, 3),
(2, 'Samarreta', 'Una samarreta de cotó de color blau.', 'no_image.png', 19.99, 2, 1, 3),
(3, 'Ninot de peluix', 'Un ninot de peluix suau.', 'no_image.png', 9.99, 3, 1, 4);

-- Restablecer la secuencia para la tabla products en PostgreSQL
SELECT SETVAL('products_id_seq', (SELECT MAX(id) FROM products));

-- Insertar registros en la tabla orders
INSERT INTO orders (product_id, buyer_id, offer) VALUES 
(1, 3, 50.00);

-- Restablecer la secuencia para la tabla orders en PostgreSQL
SELECT SETVAL('orders_id_seq', (SELECT MAX(id) FROM orders));