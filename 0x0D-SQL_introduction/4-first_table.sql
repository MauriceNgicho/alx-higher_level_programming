-- A Script to create a table called first_table in the current database
-- Ensures the script does not fail if the table already exists


CREATE TABLE IF NOT EXITS first_table(
	id INT,
	name VARCHAR(256)
);
