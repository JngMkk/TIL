SELECT
	CURRENT_DATE AS dt
	, CURRENT_TIMESTAMP AS stamp
;

SELECT
	CURRENT_DATE AS dt
	, LOCALTIMESTAMP AS stamp
;

SELECT
	-- PostgreSQL, Hive, SparkSQL 모두 'CAST(vale AS type)' 사용
	CAST('2021-12-31' AS date) AS dt
	, CAST('2021-12-31 23:59:59' AS timestamp) AS stamp
	
	-- Hive의 경우 'type(value)' 사용하기
	-- date('2021-12-31') AS dt
	-- , timestamp('2021-12-31 23:59:59') AS stamp
	
	-- PostgreSQL, Hive, SparkSQL 모두 'type value' 사용
	-- 다만 value는 상수이므로 컬럼 이름으로 지정할 수 없음
	-- date '2021-12-31' AS dt
	-- , timestamp '2021-12-31 23:59:59' AS stamp
	
	-- PostgreSQL의 경우 'value::type' 사용
	-- '2021-12-31'::date AS dt
	-- , '2021-12-31 23:59:59'::timestamp AS stamp
;

SELECT
	date '2021-12-31' AS dt
	, timestamp '2021-12-31 23:59:59' AS stamp
;

SELECT
	-- PostgreSQL의 경우 'value::type' 사용
	'2021-12-31'::date AS dt
	, '2021-12-31 23:59:59'::timestamp AS stamp
;