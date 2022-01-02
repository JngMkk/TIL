create table subway_statistics(
    seq_id number not null,
    station_name varchar2(100) null,
    boarding_date date null,
    gubun varchar2(10) null,
    boarding_time number null,
    passenger_number number null,
    primary key(seq_id));

select * from subway_statistics;

select seq_id, station_name, boarding_time, passenger_number 
from subway_statistics;

-- AND
select * from subway_Statistics 
where station_name = '??(216)' and gubun = '??';

-- OR
select * from subway_statistics 
where station_name = '??(216)' or station_name = '??(220)';

-- AND & OR
select * from subway_statistics
where station_name = '??(216)' and (boarding_time = 7 or boarding_time = 9);

-- LIKE
select * from subway_statistics
where station_name like '??%';

-- LIKE & AND & IN
select * from subway_statistics
where station_name like '??%' and boarding_time in (7, 9);

select * from subway_statistics
where station_name like '??%' and passenger_number >= 500 and passenger_number <= 1000;

-- BETWEEN a AND b
select * from subway_statistics
where station_name like '??%' and passenger_number between 500 and 1000;

-- ORDER BY
select * from subway_statistics
order by station_name;

select * from subway_Statistics
where station_name like '??%'
order by 1, 2, 3, 4, 5, 6;