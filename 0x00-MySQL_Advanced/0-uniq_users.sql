-- creating a simple table that can run in any database

CREATE TABLE IF NOT EXISTS `users` (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255),
	email VARCHAR(255) NOT NULL UNIQUE
);
