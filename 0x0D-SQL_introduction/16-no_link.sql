-- Script to list all records of second_table where name is not empty
-- Results display score and name, ordered by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
