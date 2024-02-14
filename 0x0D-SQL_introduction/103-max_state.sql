-- Max TEMPERATURE TOP 3--

SELECT city, max(value) AS max_temp FROM temperatures GROUP BY `state` ORDER BY `state`;
