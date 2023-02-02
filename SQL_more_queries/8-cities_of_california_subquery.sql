-- A script that lists all the cities of California that can be f
SELECT id, name
FROM cities
WHERE state_id IN (SELECT id
      	    FROM states
	    WHERE name = 'California')
ORDER BY id ASC;
