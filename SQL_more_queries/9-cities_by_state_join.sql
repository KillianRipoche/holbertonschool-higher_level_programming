-- List all cities with their id, city name, and the corresponding state name, sorted by cities.id in ascending order using only one SELECT statement
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
