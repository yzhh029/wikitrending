FROM janraw r
INSERT OVERWRITE TABLE wikiall PARTITION(dt=${hiveconf:CURRENT_DATE})
SELECT r.name, SUM(r.views)
WHERE r.day=${hiveconf:CURRENT_DATE}
GROUP BY r.name;

