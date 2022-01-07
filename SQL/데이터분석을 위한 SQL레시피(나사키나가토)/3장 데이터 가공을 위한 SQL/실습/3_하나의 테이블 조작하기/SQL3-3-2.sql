DROP TABLE IF EXISTS popular_products;
CREATE TABLE popular_products (
    product_id varchar(255)
  , category   varchar(255)
  , score      numeric
);

INSERT INTO popular_products
VALUES
    ('A001', 'action', 94)
  , ('A002', 'action', 81)
  , ('A003', 'action', 78)
  , ('A004', 'action', 64)
  , ('D001', 'drama' , 90)
  , ('D002', 'drama' , 82)
  , ('D003', 'drama' , 78)
  , ('D004', 'drama' , 58)
;

-- 윈도 함수의 ORDER BY 구문을 사용해 테이블 내부의 순서를 다루는 쿼리
SELECT
	product_id
	, score
	-- 점수 순서로 유일한 순위를 붙임
	, ROW_NUMBER()			OVER(ORDER BY score DESC) AS row
	
	-- 같은 순위를 허용해서 순위를 붙임
	, RANK()				OVER(ORDER BY score DESC) AS rank
	
	-- 같은 순위가 있을 때 같은 순위 다음에 있는 순위를 건너 뛰고 순위를 붙임
	, DENSE_RANK()			OVER(ORDER BY score DESC) AS dense_rank
	
	-- 현재 행보다 앞에 있는 행의 값 추출하기
	, LAG(product_id)		OVER(ORDER BY score DESC) AS lag1
	, LAG(product_id, 2)	OVER(ORDER BY score DESC) AS lag2
	
	-- 현재 행보다 뒤에 있는 행의 값 추출하기
	, LEAD(product_id)		OVER(ORDER BY score DESC) AS lead1
	, LEAD(product_id, 2)	OVER(ORDER BY score DESC) AS lead2
FROM popular_products
ORDER BY row
;

-- ORDER_BY 구문과 집약 함수를 조합해서 계산하는 쿼리
SELECT
	product_id
	, score
	
	-- 점수 순서로 유일한 순위를 붙임
	, ROW_NUMBER() OVER(ORDER BY score DESC) AS row
	
	-- 순위 상위로부터의 누계 점수 계산하기
	, SUM(score)
		OVER(ORDER BY score DESC
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
    AS cum_score
    
    -- 현재 행과 앞 뒤의 행이 가진 값을 기반으로 평균 점수 계산하기
    , ROUND(AVG(score)
    	OVER(ORDER BY score DESC
            ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING), 2)
    AS local_avg
    
    -- 순위가 높은 상품 ID 추출하기
    , FIRST_VALUE(product_id)
    	OVER(ORDER BY score DESC
            ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
    AS first_value
    
    -- 순위가 낮은 상품 ID 추출하기
    , LAST_VALUE(product_id)
    	OVER(ORDER BY score DESC
            ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
    AS last_value
FROM popular_products
ORDER BY row
;

-- 윈도 프레임 지정별 상품 ID를 집약하는 쿼리
SELECT
	product_id
	
	-- 점수 순서로 유일한 순위를 붙임
	, ROW_NUMBER() OVER(ORDER BY score DESC) AS row
	
	-- 가장 앞 순위부터 가장 뒷 순위까지의 범위를 대상으로 상품 ID 집약하기
	-- PostgreSQL : array_agg
	-- Hive, SparkSQL : collect_list
	-- , collect_list(product_id)
	, array_agg(product_id)
		OVER(ORDER BY score DESC
            ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
    AS whole_agg
    
    -- 가장 앞 순위부터 현재 순위까지의 범위를 대상으로 상품 ID 집약하기
    -- , collect_list(product_id)
    , array_agg(product_id)
    	OVER(ORDER BY score DESC
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
    AS cum_agg
    
    -- 순위 1행 앞과 1행 뒤까지의 범위를 대상으로 상품 ID 집약하기
    -- , collect_list(product_id)
    , array_agg(product_id)
    	OVER(ORDER BY score DESC
            ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING)
    AS local_agg
FROM popular_products
WHERE category = 'action'
ORDER BY row
;

-- 윈도 함수를 사용해 카테고리들의 순위를 계산하는 쿼리
SELECT
	category
	, product_id
	, score
	
	-- 카테고리별로 점수 순서로 정렬하고 유일한 순위를 붙임
	, ROW_NUMBER()
		OVER(PARTITION BY category ORDER BY score DESC)
	AS row
	
	-- 카테고리별로 같은 순위를 허가하고 순위를 붙임
	, RANK()
		OVER(PARTITION BY category ORDER BY score DESC)
	AS rank
	
	-- 카테고리별로 같은 순위가 있을 때
	-- 같은 순위 다음에 있는 순위를 건너 뛰지 않고 순위를 붙임
	, DENSE_RANK()
		OVER(PARTITION BY category ORDER BY score DESC)
	AS dense_rank
FROM popular_products
ORDER BY category, row
;

-- 카테고리들의 순위 상위 2개까지의 상품을 추출하는 쿼리
SELECT *
FROM
	-- 서브 쿼리 내부에서 순위 계산하기
	(SELECT
     	category
     	, product_id
     	, score
     		-- 카테고리별로 점수 순서로 유일한 순위를 붙임
     	, ROW_NUMBER()
     		OVER(PARTITION BY category ORDER BY score DESC)
     	AS rank
     FROM popular_products)
     AS popular_products_with_rank
-- 외부 쿼리에서 순위 활용해 압축하기
WHERE rank <= 2
ORDER BY category, rank
;

-- 카테고리별 순위 최상위 상품 추출하는 쿼리
-- DISTINCT 구문을 사용해 중복 제거하기
-- DISTINCT 구문을 사용해 중복 제거하기
SELECT DISTINCT
	category
	-- 카테고리별로 순위 최상위 상품 ID 추출하기
	, FIRST_VALUE(product_id)
		OVER(PARTITION BY category ORDER BY score DESC
			ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
	AS product_id
FROM popular_products
ORDER BY category
;