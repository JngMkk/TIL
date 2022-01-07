DROP TABLE IF EXISTS mst_users_with_dates;
CREATE TABLE mst_users_with_dates (
    user_id        varchar(255)
  , register_stamp varchar(255)
  , birth_date     varchar(255)
);

INSERT INTO mst_users_with_dates
VALUES
    ('U001', '2016-02-28 10:00:00', '2000-02-29')
  , ('U002', '2016-02-29 10:00:00', '2001-03-29')
  , ('U003', '2016-03-01 10:00:00', '2002-04-29')
;

-- 미래 또는 과거의 날짜/시간을 계산하는 쿼리
SELECT
	user_id
	-- PostgreSQL의 경우 interval 자료형의 데이터에 사칙 연산 적용
	, register_stamp::timestamp AS register_stamp
	, register_stamp::timestamp + '1 hour'::interval AS after_1_hour
	, register_stamp::timestamp - '30 minutes'::interval AS before_30_minutes
	
	, register_stamp::date AS register_date
	, (register_stamp::date + '1 day'::interval)::date AS after_1_day
	, (register_stamp::date - '1 month'::interval)::date AS before_1_month
	
	-- Hive, SparkSQL의 경우 날짜/시각을 계산하기 함수가 제공되지 않으므로
	-- 한 번 unixtime으로 변환하고 초 단위로 계산을 적용한 뒤 다시 타임스탬프로 변환하기
	-- , CAST(register_stamp AS timestamp) AS register_stamp
	-- , from_unixtime(unix_timestamp(register_stamp) + 60 * 60) AS after_1_hour
	-- , from_unixtime(unix_timestamp(register_stamp) - 30 * 60) AS before_30_minutes
	
	-- 타임스탬프 문자열을 날짜로 변환할 때는 to_date 함수 사용
	-- , to_date(register_stamp) AS register_date
	
	-- 일과 월을 계산할 때는 date_add 함수와 add_months 함수 사용하기
	-- 다만 연을 계산하는 함수는 구현되어 있지 않음
	-- , date_add(to_date(register_stamp), 1) AS after_1_day
	-- , add_months(to_date(register_stamp), -1) AS before_1_month
FROM mst_users_with_dates
;

-- 두 날짜의 차이를 계산하는 쿼리
SELECT
	user_id
	-- PostgreSQL의 경우 날짜 자료형끼리 뺄 수 있음
	, CURRENT_DATE AS today
	, register_stamp::date AS register_date
	, CURRENT_DATE - register_stamp::date AS diff_days
	
	-- Hive, SparkSQL의 경우 datediff 함수 사용
	-- , CURRENT_DATE() AS today
	-- , to_date(register_stamp) AS register_date
	-- , datediff(CURRENT_DATE(), to_date(register_stamp)) AS diff_days
FROM mst_users_with_dates
;

-- age 함수를 사용해 나이를 계산하는 쿼리
SELECT
	user_id
	, CURRENT_DATE AS today
	, register_stamp::date AS register_date
	, birth_date::date AS birth_date
	, EXTRACT(YEAR FROM age(birth_date::date)) AS current_age
	, EXTRACT(YEAR FROM age(register_stamp::date, birth_date::date)) AS register_age
	
	-- 한국 나이
	, (EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM birth_date::date)) + 1 AS korean_age
FROM mst_users_with_dates
;

-- 생일이 2000년 2월 29일인 사람의 2021년 1월 5일 시점의 나이 계산하기
SELECT floor((20210105 - 20000229) / 10000) AS age;

-- 등록 시점과 현재 시점의 나이를 문자열로 계산하는 쿼리
SELECT
	user_id
	, substring(register_stamp, 1, 10) AS register_date
	, birth_date
	
	-- 등록 시점의 나이 계산하기
	, floor(
    	(CAST(replace(substring(register_stamp, 1, 10), '-', '') AS integer)
    	- CAST(replace(birth_date, '-', '') AS integer)
    	) / 10000) AS register_age
    
    -- 현재 시점의 나이 계산하기
    , floor(
    	(CAST(replace(CAST(CURRENT_DATE AS text), '-', '') AS integer)
        - CAST(replace(birth_date, '-', '') AS integer)) / 10000) AS current_age
    
    -- Hive, SparkSQL의 경우 replace를 regexp_replace, text를 string, integer를 int로 바꾸기
    -- SparkSQL의 경우는 추가로 CURRENT_DATE를 CURRENT_DATE()로 바꾸기
    -- (CAST(regexp_replace(CAST(CURRENT_DATE() AS string), '-', '') AS int)
    -- 		- CAST(regexp_replace(birth_date, '-', '') AS int) / 10000) AS current age
FROM mst_users_with_dates
;