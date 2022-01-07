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

DROP TABLE IF EXISTS purchase_log;
CREATE TABLE purchase_log (
    purchase_id integer
  , product_ids varchar(255)
);

INSERT INTO purchase_log
VALUES
    (100001, 'A001,A002,A003')
  , (100002, 'D001,D002')
  , (100003, 'A001')
;

-- 일련 번호를 가진 피벗 테이블을 사용해 행으로 변환하는 쿼리
SELECT
	q.year
	-- q1~q4 레이블 이름 출력하기
	, CASE
		WHEN p.idx = 1 THEN 'q1'
		WHEN p.idx = 2 THEN 'q2'
		WHEN p.idx = 3 THEN 'q3'
		WHEN p.idx = 4 THEN 'q4'
	END AS quarter
	-- q1~q4 매출 출력하기
	, CASE
		WHEN p.idx = 1 THEN q.q1
		WHEN p.idx = 2 THEN q.q2
		WHEN p.idx = 3 THEN q.q3
		WHEN P.idx = 4 THEN q.q4
	END AS sales
FROM
	quarterly_sales AS q
	CROSS JOIN
		-- 행으로 전개하고 싶은 열의 수만큼 순번 테이블 만들기
		(SELECT 1 AS idx
        UNION ALL SELECT 2 AS idx
        UNION ALL SELECT 3 AS idx
        UNION ALL SELECT 4 AS idx
        ) AS p
;

-- 테이블 함수를 사용해 병열을 행으로 전개하는 쿼리
SELECT unnest(ARRAY['A001', 'A002', 'A003', 'D001', 'D002']) AS product_id;

	-- Hive, SparkSQL : explode
	-- SELECT explode(ARRAY['A001', 'A002', 'A003', 'D001', 'D002']) AS product_id;

-- 테이블 함수를 사용해 쉼표로 구분된 문자열 데이터를 행으로 전개하는 쿼리
SELECT
	purchase_id
	, product_id
FROM
	purchase_log AS p
	-- string_to_array 함수로 문자열을 배열로 변환하고, unnest 함수로 테이블로 변환하기
	CROSS JOIN unnest(string_to_array(product_ids, ',')) AS product_id
	
	-- Hive, SparkSQL : LATERAL VIEW explode
	-- LATERAL VIEW explode(split(product_ids, ',')) e AS product_id;
;

-- PostgreSQL에서 쉼표로 구분된 데이터를 행으로 전개하는 쿼리
SELECT
	purchase_id
	-- 쉼표로 구분된 문자열을 한 번에 행으로 전개하기
	, regexp_split_to_table(product_ids, ',') AS product_id
FROM purchase_log
;