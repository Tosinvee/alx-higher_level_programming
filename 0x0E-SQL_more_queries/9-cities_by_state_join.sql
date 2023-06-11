-- a script that lists all cities contained in the database hbtn_0d_us
-- list all rows that contains in a database
SELECT cities.id, cities.name, states.name 
FROM cities
INNER JOIN states
ON cities.state_id = state.id
ORDER BY cities.id;
