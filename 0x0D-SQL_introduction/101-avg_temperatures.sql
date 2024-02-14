-- AVERAGE TEMPERATURE --

SELECT city, avg(value) as avg_value from temperatures group by city ORDER BY avg_value DESC;
