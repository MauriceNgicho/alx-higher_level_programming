-- Create the database hbtn_0d_2 and the user user_0d_2 with SELECT privilege only


-- create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create user if it doesn't exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grent SELECT privilege to the user on the database.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply changes
FLUSH PRIVILEGES
