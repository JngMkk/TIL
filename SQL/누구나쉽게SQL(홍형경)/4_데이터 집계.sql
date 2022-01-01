-- GROUP BY 절과 집계 함수
/*
SELECT expr1, expr2, ...
    FROM ...
    WEHRE ...
    AND ...
    GROUP BY expr1, expr2, ...
    ORDER BY ...

집계할 대상 컬럼이나 표현식을 명시하면 됨.
GROUP BY 절에 명시한 모든 컬럼이나 표현식은 SELECT 절에도 명시해야 함.
집계 함수와 같이 사용해야 의미가 있다.

COUNT(expr) expr의 전체 개수를 구해 반환. 보통 *. 해당 select문에서 조회된 전체 데이터
MAX(expr) expr의 최댓값을 반환
MIN(expr) wxpr의 최솟값을 반환
SUM(expr) expr의 합계를 반환
AVG(expr) expr의 평균값을 반환
VARIANCE(expr) expr의 분산을 반환
STDDEV(expr) expr의 표준편차를 반환
집계 함수는 select 절에서만 사용할 수 있음.
*/
select station_name from subway_statistics
    where gubun = '승차'
    group by station_name
    order by station_name;

select count(*) cnt,
    MIN(passenger_number) min_value,
    MAX(passenger_number) max_value,
    SUM(passenger_number) sum_value,
    AVG(passenger_number) avg_value
    from subway_statistics;
    
-- 지하철역별 승차 인원 통계
select station_name, count(*) cnt,
    min(passenger_number) min_value,
    max(passenger_number) max_value,
    sum(passenger_number) sum_value,
    avg(passenger_number) avg_value
FROM subway_statistics
where gubun = '승차'
group by station_name
order by station_name;

-- 구로디지털단지역 시간별 승하차 인원 조회
select station_name,
    boarding_time,
    gubun,
    min(passenger_number) min_value,
    max(passenger_number) max_value,
    sum(passenger_number) sum_value
    from subway_statistics
    where station_name in ('구로디지털단지(232)')
    group by station_name, boarding_time, gubun
    order by station_name, boarding_time, gubun;

-- 하차 인원이 많은 순서로 조회
select station_name,
    boarding_time,
    gubun,
    min(passenger_number) min_value,
    max(passenger_number) max_value,
    sum(passenger_number) sum_value
    from subway_statistics
    group by station_name, boarding_time, gubun
    order by 6 desc;
    
-- HAVING 절 집계 쿼리의 조건절
SELECT station_name,
    boarding_time,
    gubun,
    min(passenger_number) min_value,
    max(passenger_number) max_value,
    sum(passenger_number) sum_value
    from subway_statistics
    group by station_name, boarding_time, gubun
    having sum(passenger_number) between 15000 and 16000
    order by 6 desc;

-- DISTINCT 중복 값을 제외한 유일한 값들만 조회되어 group by 절을 사용한 효과가 남.
select distinct station_name
from subway_statistics
order by 1;

