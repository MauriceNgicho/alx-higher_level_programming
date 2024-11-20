-- Script to list the number of records with the same score in the table second_table
-- Results display score and number (count), ordered by number (descending)

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
