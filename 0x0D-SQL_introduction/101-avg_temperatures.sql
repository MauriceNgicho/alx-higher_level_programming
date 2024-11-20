-- Script to display the average temperature by city, ordered by temperature

SELECT city, 
       ROUND(AVG(temperature), 4) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
