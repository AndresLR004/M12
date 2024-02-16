-- Insertar datos en la tabla statuses
INSERT INTO statuses (id, name, slug) VALUES
(1, 'Nou', 'nou');

-- Reiniciar la secuencia de la tabla statuses en MySQL
ALTER TABLE statuses AUTO_INCREMENT = 2;

-- Insertar datos en la tabla categories
INSERT INTO categories (id, name, slug) VALUES
(1, 'Electrònica', 'electronica'),
(2, 'Roba', 'roba'),
(3, 'Joguines', 'joguines');

-- Reiniciar la secuencia de la tabla categories en MySQL
ALTER TABLE categories AUTO_INCREMENT = 4;

-- Insertar datos en la tabla users
INSERT INTO users (id, name, email, role, verified, password) VALUES
(1, 'Joan Pérez', 'joan@example.com', 'admin', 1, 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4'),
(2, 'Anna García', 'anna@example.com', 'moderator', 1, 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4'),
(3, 'Elia Rodríguez', 'elia@example.com', 'wanner', 1, 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4'),
(4, 'Kevin Salardú', 'kevin@example.com', 'wanner', 1, 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4');

-- Reiniciar la secuencia de la tabla users en MySQL
ALTER TABLE users AUTO_INCREMENT = 5;

-- Insertar datos ficticios en la tabla products
INSERT INTO products (id, title, description, photo, price, category_id, status_id, seller_id) VALUES
(1, 'Telèfon mòbil', 'Un telèfon intel·ligent d''última generació.', 'no_image.png', 599.99, 1, 1, 3),
(2, 'Samarreta', 'Una samarreta de cotó de color blau.', 'no_image.png', 19.99, 2, 1, 3),
(3, 'Ninot de peluix', 'Un ninot de peluix suau.', 'no_image.png', 9.99, 3, 1, 4);

-- Reiniciar la secuencia de la tabla products en MySQL
ALTER TABLE products AUTO_INCREMENT = 4;
