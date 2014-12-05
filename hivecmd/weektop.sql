FROM wikiall r
SELECT r.name, SUM(r.views) AS totalview
WHERE r.dt BETWEEN 20110123 AND 20110129
GROUP BY r.name
SORT BY totalview DESC limit 15;

