-- Script to update the score of Bob to 10 in the table second_table
-- Only the name field is used to identify the record

UPDATE second_table
SET score = 10
WHERE name = 'Bob';
