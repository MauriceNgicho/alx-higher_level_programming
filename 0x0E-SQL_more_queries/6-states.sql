-- Script to create the database hbtn_0d_usa and the table states with specified constraints

-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created database
USE hbtn_0d_usa;

-- Create the table states if it doesn't already exist
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
