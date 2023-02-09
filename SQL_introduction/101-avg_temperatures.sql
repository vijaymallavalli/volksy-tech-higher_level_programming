SELECT city,AVG(value) AS 'avg_temp' From temperatures GROUP BY 'city' ORDER BY 'avg_temp' DESC;
