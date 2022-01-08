DROP TABLE IF EXISTS mst_categories;
CREATE TABLE mst_categories (
    category_id integer
  , name        varchar(255)
);

INSERT INTO mst_categories
VALUES
    (1, 'dvd' )
  , (2, 'cd'  )
  , (3, 'book')
;

DROP TABLE IF EXISTS category_sales;
CREATE TABLE category_sales (
    category_id integer
  , sales       integer
);

INSERT INTO category_sales
VALUES
    (1, 850000)
  , (2, 500000)
;

DROP TABLE IF EXISTS product_sale_ranking;
CREATE TABLE product_sale_ranking (
    category_id integer
  , rank        integer
  , product_id  varchar(255)
  , sales       integer
);

INSERT INTO product_sale_ranking
VALUES
    (1, 1, 'D001', 50000)
  , (1, 2, 'D002', 20000)
  , (1, 3, 'D003', 10000)
  , (2, 1, 'C001', 30000)
  , (2, 2, 'C002', 20000)
  , (2, 3, 'C003', 10000)
;

-- 여러 개의 테이블을 결합해서 가로로 정렬하는 쿼리
SELECT
	m.category_id
	, m.name
	, s.sales
	, r.product_id AS sale_product
FROM
	mst_categories AS m
	JOIN
	-- 카테고리별로 매출액 결합하기
	category_sales AS s
	ON m.category_id = s.category_id
	JOIN
	-- 카테고리별로 상품 결합하기
	product_sale_ranking AS r
	ON m.category_id = r.category_id
;

-- 마스터 테이블의 행 수를 변경하지 않고 여러 개의 테이블을 가로로 정렬하는 쿼리
SELECT
	m.category_id
	, m.name
	, s.sales
	, r.product_id AS top_sale_product
FROM
	mst_categories AS m
	-- LEFT JOIN을 사용해서 결합한 레코드를 남김
	LEFT JOIN
		-- 카테고리별 매출액 결합하기
		category_sales AS s
		ON m.category_id = s.category_id
	-- LEFT JOIN을 사용해서 결합하지 못한 레코드를 남김
	LEFT JOIN
		-- 카테고리별 최고 매출 상품 하나만 추출해서 결합하기
		product_sale_ranking AS r
		ON m.category_id = r.category_id
		AND r.rank = 1
;

-- 상관 서브쿼리 여러 개의 테이블을 가로로 정렬하는 쿼리
SELECT
	m.category_id
	, m.name
	-- 상관 서브쿼리를 사용해 카테고리별로 매출액 추출하기
	, (SELECT s.sales
      FROM category_sales AS s
      WHERE m.category_id = s.category_id
      ) AS sales
    -- 상관 서브쿼리를 사용해 카테고리별로 최고 매출 상품을 하나 추출하기(순위로 따로 압축하지 않아도 됨)
    , (SELECT r.product_id
      FROM product_sale_ranking AS r
      WHERE m.category_id = r.category_id
      ORDER BY sales DESC
      LIMIT 1
      ) AS top_sale_product
FROM
	mst_categories AS m
;