DROP TABLE IF EXISTS advertising_stats;
CREATE TABLE advertising_stats (
    dt          varchar(255)
  , ad_id       varchar(255)
  , impressions integer
  , clicks      integer
);

INSERT INTO advertising_stats
VALUES
    ('2017-04-01', '001', 100000,  3000)
  , ('2017-04-01', '002', 120000,  1200)
  , ('2017-04-01', '003', 500000, 10000)
  , ('2017-04-02', '001',      0,     0)
  , ('2017-04-02', '002', 130000,  1400)
  , ('2017-04-02', '003', 620000, 15000)
;

-- 정수 자료형의 데이터를 나누는 쿼리
SELECT
	dt
	, ad_id
	-- PostgreSQL의 경우 점수를 나누면 소수점이 잘리므로 명시적으로 자료형 변환
	, CAST(clicks AS double precision) / impressions AS ctr
	-- 실수를 상수로 앞에 두고 계산하면 암묵적으로 자료형 변환이 일어남
	-- 소수점 둘째 자리에서 반올림
	, ROUND(100.0 * clicks / impressions, 2) AS ctr_as_percent
	
	-- Hive, SparkSQL의 경우
	-- clicks / impressions AS ctr
	-- PostgreSQL 결과 -> ctr 0 & ctr_as_percent 3.0000000
FROM
	advertising_stats
WHERE
	dt = '2017-04-01'
ORDER BY
	dt, ad_id
;

-- 0으로 나누는 것을 피해 CTR을 계산하는 쿼리
SELECT
	dt
	, ad_id
	-- 방법 1 CASE 식 사용 -> 분모가 0일 경우 분기해서, 0으로 나누지 않게 만드는 방법
	, CASE
		WHEN impressions > 0 THEN ROUND(100.0 * clicks / impressions, 2)
	END AS ctr_as_percent_by_case

	-- 방법 2 분모가 0이라면 NULL로 변환해서, 0으로 나누지 않게 만드는 방법
	-- PostgreSQL, SparkSQL의 경우 NULLIF 함수 사용
	, ROUND(100.0 * clicks / NULLIF(impressions, 0), 2) AS ctr_as_percent_by_null
	-- Hive의 경우 NULLIF 대신 CASE 식 사용
	-- , 100.0 * clicks / CASE WHEN impressions = 0 THEN NULL ELSE impressions
	-- END AS ctr_as_percent_by_null
FROM
	advertising_stats
ORDER BY
	dt, ad_id
;



