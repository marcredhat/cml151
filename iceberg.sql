DROP TABLE flights_csv

CREATE EXTERNAL TABLE flights_csv (month int, dayofmonth int, dayofweek int, deptime int, crsdeptime int, arrtime int, crsarrtime int, uniquecarrier string, flightnum int, tailnum string, actualelapsedtime int, crselapsedtime int, airtime int, arrdelay int, depdelay int, origin string, dest string, distance int, taxiin int, taxiout int, cancelled int, cancellationcode string, diverted string, carrierdelay int, weatherdelay int, nasdelay int, securitydelay int, lateaircraftdelay int, year int)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
STORED AS TEXTFILE  tblproperties("skip.header.line.count"="1");


LOAD DATA INPATH '/user/mchisinevski/flights.csv' INTO TABLE flights_csv;


select count(*) from flights_csv


-- CREATE ICEBERG TABLE FORMAT STORED AS PARQUET
drop table if exists flights_iceberg;

CREATE EXTERNAL TABLE flights_iceberg (
 month int, dayofmonth int, 
 dayofweek int, deptime int, crsdeptime int, arrtime int, 
 crsarrtime int, uniquecarrier string, flightnum int, tailnum string, 
 actualelapsedtime int, crselapsedtime int, airtime int, arrdelay int, 
 depdelay int, origin string, dest string, distance int, taxiin int, 
 taxiout int, cancelled int, cancellationcode string, diverted string, 
 carrierdelay int, weatherdelay int, nasdelay int, securitydelay int, 
 lateaircraftdelay int
) 
PARTITIONED BY (year int)
STORED BY ICEBERG 
STORED AS PARQUET
LOCATION '/user/mchisinevski/flights_iceberg' ;



-- LOAD DATA INTO ICEBERG TABLE FORMAT STORED AS PARQUET
INSERT INTO flights_iceberg
SELECT * FROM flights_csv
WHERE year <= 2006;


select count(*) from flights_iceberg

-- [TABLE MAINTENANCE] CREATE FLIGHTS TABLE IN ICEBERG TABLE FORMAT STORED AS PARQUET
drop table if exists flights_partitioneds;

CREATE EXTERNAL TABLE flights_partitioned (
 month int, dayofmonth int, 
 dayofweek int, deptime int, crsdeptime int, arrtime int, 
 crsarrtime int, uniquecarrier string, flightnum int, tailnum string, 
 actualelapsedtime int, crselapsedtime int, airtime int, arrdelay int, 
 depdelay int, origin string, dest string, distance int, taxiin int, 
 taxiout int, cancelled int, cancellationcode string, diverted string, 
 carrierdelay int, weatherdelay int, nasdelay int, securitydelay int, 
 lateaircraftdelay int
) 
PARTITIONED BY (year int)
STORED BY ICEBERG 
STORED AS PARQUET
LOCATION '/user/mchisinevski/flights_iceberg_partitioned'
TBLPROPERTIES ('external.table.purge'='true');


select year, count(*) from flights_iceberg
group by year
order by year desc

alter table flights_iceberg set partition spec (year, month)


describe formatted flights_iceberg

explain 
select year, month, count(*) from flights_iceberg
where year = 2006 and month = 12
group by year, month
order by year desc


select * from default.flights_iceberg.history

select * from flights_iceberg limit 1

ALTER TABLE flights_iceberg SET TBLPROPERTIES('format-version' = '2');




update flights_iceberg 
set deptime='1146' where deptime='1145' and year='2006'

select * from default.flights_iceberg.history


select * from default.flights_iceberg.snapshots

select year, month, count(*) from flights_iceberg
for system_time as of '2023-05-18 06:32:42.696 Etc/UTC'
where year = 2006  and deptime='1145'
group by year, month
order by year desc


select year, month, count(*) from flights_iceberg
for system_time as of '2023-05-18 06:32:42.696 Etc/UTC'
where year = 2006 and deptime='1146'
group by year, month
order by year desc
