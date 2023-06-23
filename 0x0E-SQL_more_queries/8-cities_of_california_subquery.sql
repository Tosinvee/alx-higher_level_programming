-- list all the states in california
SELECT id, name
FROM cities
WHERE cities.state_id = (SELECT id
        FROM states
        WHERE name = 'california')
ORDER BY cities.id ASC;
