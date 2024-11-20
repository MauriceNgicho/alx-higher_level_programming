-- Script to create the table force_name with id and a NOT NULL name column

CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL
);
