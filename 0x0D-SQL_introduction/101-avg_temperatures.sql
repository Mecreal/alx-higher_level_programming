-- AVERAGE TEMPERATURE --

SELECT city, avg(value) from temperatures group by city;
