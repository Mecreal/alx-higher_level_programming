-- AVERAGE TEMPERATURE --

SELECT city, avg(value) as avg_temp from temperatures group by city ORDER BY avg_temp DESC;
