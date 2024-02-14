-- AVERAGE TEMPERATURE TOP 3--

SELECT city, avg(value) as avg_temp from temperatures group by city ORDER BY avg_temp DESC Limit 3;
