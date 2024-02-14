-- AVERAGE TEMPERATURE TOP 3--

SELECT city, avg(value) as avg_value from temperatures group by city ORDER BY avg_value DESC Limit 3;
