CREATE TABLE wikiall (
	name STRING,
	views INT )
PARTITIONED BY(dt INT)
STORED AS SEQUENCEFILE;

