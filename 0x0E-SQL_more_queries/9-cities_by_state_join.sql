-- Lists all cities along with their state names, sorted by cities.id
SELECT 
    cities.id, 
    cities.name, 
    states.name 
FROM 
    cities, states 
WHERE 
    cities.state_id = states.id 
ORDER BY 
    cities.id ASC;
