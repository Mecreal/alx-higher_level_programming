-- Max TEMPERATURE TOP 3--

SELECT city, max(value) AS max_temp FROM temperatures GROUP BY city ORDER BY max_temp DESC LIMIT 3;
