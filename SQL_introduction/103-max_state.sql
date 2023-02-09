-- SQL
SELECT  state MAX(value) AS max_temp
FROM temperature
GROUP BY state
ORDER BY state;
