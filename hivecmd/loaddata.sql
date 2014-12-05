FROM janraw r
INSERT OVERWRITE TABLE wikiall PARTITION(dt=20110130)
SELECT r.name, SUM(r.views)
WHERE r.day=20110130
GROUP BY r.name;

FROM janraw r
INSERT OVERWRITE TABLE wikiall PARTITION(dt=20110131)
SELECT r.name, SUM(r.views)
WHERE r.day=20110131
GROUP BY r.name;