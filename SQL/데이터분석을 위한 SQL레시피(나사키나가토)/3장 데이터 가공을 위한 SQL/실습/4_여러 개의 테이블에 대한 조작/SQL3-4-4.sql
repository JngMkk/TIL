DROP TABLE IF EXISTS product_sales;
CREATE TABLE product_sales (
    category_name varchar(255)
  , product_id    varchar(255)
  , sales         integer
);

INSERT INTO product_sales
VALUES
    ('dvd' , 'D001', 50000)
  , ('dvd' , 'D002', 20000)
  , ('dvd' , 'D003', 10000)
  , ('cd'  , 'C001', 30000)
  , ('cd'  , 'C002', 20000)
  , ('cd'  , 'C003', 10000)
  , ('book', 'B001', 20000)
  , ('book', 'B002', 15000)
  , ('book', 'B003', 10000)
  , ('book', 'B004',  5000)
;

-- 
WITH
product_sale_ranking AS(
	SELECT
		category_name
		, product_id
		, sales
		, ROW_NUMBER() OVER(PARTITION BY category_name ORDER BY sales DESC) AS rank
	FROM
		product_sales
)
SELECT * 
FROM product_sale_ranking
;

-- 카테고리들의 순위에서 유니크한 순위 목록을 계산하는 쿼리
WITH
product_sale_ranking AS (
	SELECT
		category_name
		, product_id
		, sales
		, ROW_NUMBER() OVER(PARTITION BY category_name ORDER BY sales DESC) AS rank
	FROM
		product_sales
)
, mst_rank AS(
	SELECT DISTINCT rank
	FROM product_sale_ranking
)
SELECT *
FROM mst_rank
;

-- 카테고리들의 순위를 횡단적으로 출력하는 쿼리
WITH
product_sale_ranking AS (
	SELECT
		category_name
		, product_id
		, sales
		, ROW_NUMBER() OVER(PARTITION BY category_name ORDER BY sales DESC) AS rank
	FROM
		product_sales
)
, mst_rank AS(
	SELECT DISTINCT rank
	FROM product_sale_ranking
)
SELECT
	m.rank
	, r1.product_id AS dvd
	, r1.sales		AS dvd_sales
	, r2.product_id	AS cd
	, r2.sales		AS cd_sales
	, r3.product_id	AS book
	, r3.sales		AS book_sales
FROM
	mst_rank AS m
	LEFT JOIN
		product_sale_ranking AS r1
		ON m.rank = r1.rank
		AND r1.category_name = 'dvd'
	LEFT JOIN
		product_sale_ranking AS r2
		ON m.rank = r2.rank
		AND r2.category_name = 'cd'
	LEFT JOIN
		product_sale_ranking AS r3
		ON m.rank = r3.rank
		AND r3.category_name = 'book'
ORDER BY m.rank
;