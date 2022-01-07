DROP TABLE IF EXISTS quarterly_sales;
CREATE TABLE quarterly_sales (
    year integer
  , q1   integer
  , q2   integer
  , q3   integer
  , q4   integer
);

INSERT INTO quarterly_sales
VALUES
    (2015, 82000, 83000, 78000, 83000)
  , (2016, 85000, 85000, 80000, 81000)
  , (2017, 92000, 81000, NULL , NULL )
;

-- q1, q2 컬럼을 비교하는 쿼리
SELECT
	year
	, q1
	, q2
	-- q1과 q2의 매출 변화 평가하기
	, CASE
		WHEN q1 < q2 THEN '+'
		WHEN q1 = q2 THEN ' '
		ELSE '-'
	END AS judge_q1_q2
	
	-- q1과 q2의 매출액 차이 계산하기
	, q2 - q1 AS diff_q2_q1
	
	-- q1과 q2의 매출 변화를 1, 0, -1로 표현하기
	, SIGN(q2 - q1) AS sign_q2_q1
FROM
	quarterly_sales
ORDER BY
	year
;

-- 연간 최대/최소 4분기 매출을 찾는 쿼리
SELECT
	year
	-- q1~q4의 최대 매출 구하기
	, greatest(q1, q2, q3, q4) AS greatest_sales
	
	-- q1~q4 최소 매출 구하기
	, least(q1, q2, q3, q4) AS least_sales
FROM
	quarterly_sales
ORDER BY
	year
;

-- 단순한 연산으로 평균 4분기 매출을 구하는 쿼리
SELECT
	year
	, (q1 + q2 + q3 + q4) / 4 AS average
FROM
	quarterly_sales
ORDER BY
	year
;

-- COALESCE를 사용해 NULL을 0으로 변환하고 평균값을 구하는 쿼리
SELECT
	year
	, (COALESCE(q1, 0) + COALESCE(q2, 0) + COALESCE(q3, 0) + COALESCE(q4, 0)) / 4 AS average
FROM
	quarterly_sales
ORDER BY
	year
;

-- NULL이 아닌 컬럼만을 사용해서 평균값을 구하는 쿼리
SELECT
	year
	, (COALESCE(q1, 0) + COALESCE(q2, 0) + COALESCE(q3, 0) + COALESCE(q4, 0))
	/ (SIGN(COALESCE(q1, 0)) + SIGN(COALESCE(Q2,0)) + SIGN(COALESCE(Q3, 0)) + SIGN(COALESCE(q4,0)))
	AS average
FROM
	quarterly_sales
ORDER BY
	year
;