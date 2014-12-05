FROM wikiall r
SELECT r.name, SUM(r.views) AS totalview
WHERE r.dt BETWEEN 20110101 AND 20110131
GROUP BY r.name
SORT BY totalview DESC limit 10;

