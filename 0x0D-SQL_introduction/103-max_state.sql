-- Max TEMPERATURE TOP 3--

SELECT city, max(value) as max_temp from temperatures group by city ORDER BY max_temp DESC Limit 3;
