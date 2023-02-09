-- SQL
SELECT city,AVG(value) AS avg_temp
FROM temperatures WHERE month = 7 or month = 8
GROUP BY cities
ORDER BY avg_temp DESC
LIMIT 3;
