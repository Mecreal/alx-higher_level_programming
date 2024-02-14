-- AVERAGE TEMPERATURE TOP 3--

SELECT city, avg(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
