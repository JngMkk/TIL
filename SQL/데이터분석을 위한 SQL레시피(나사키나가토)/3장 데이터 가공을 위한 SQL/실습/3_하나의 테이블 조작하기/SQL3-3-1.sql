DROP TABLE IF EXISTS review;
CREATE TABLE review (
    user_id    varchar(255)
  , product_id varchar(255)
  , score      numeric
);

INSERT INTO review
VALUES
    ('U001', 'A001', 4.0)
  , ('U001', 'A002', 5.0)
  , ('U001', 'A003', 5.0)
  , ('U002', 'A001', 3.0)
  , ('U002', 'A002', 3.0)
  , ('U002', 'A003', 4.0)
  , ('U003', 'A001', 5.0)
  , ('U003', 'A002', 4.0)
  , ('U003', 'A003', 4.0)
;


-- 집약 함수를 사용해서 테이블 전체의 특징량을 계산하는 쿼리
SELECT
	COUNT(*) AS total_count
	, COUNT(DISTINCT user_id) AS user_count
	, COUNT(DISTINCT product_id) AS product_id
	, SUM(score) AS sum
	, TRUNC(AVG(score), 2) AS avg
	, MAX(score) AS max
	, MIN(score) AS min
FROM
	review
;

-- 사용자 기반으로 데이터를 분할하고 집약 함수를 적용하는 쿼리
SELECT
	user_id
	, COUNT(*) AS total_count
	, COUNT(DISTINCT product_id) AS product_count
	, SUM(score) AS sum
	, TRUNC(AVG(score), 2) AS avg
	, MAX(score) AS max
	, MIN(score) AS min
FROM
	review
GROUP BY
	user_id
;

-- 윈도 함수를 사용해 집약 함수의 결과와 원래 값을 동시에 다루는 쿼리
SELECT
	user_id
	, product_id
	-- 개별 리뷰 점수
	, score
	-- 전체 평균 리뷰 점수
	, ROUND(AVG(score) OVER(), 2) AS avg_score
	-- 사용자의 평균 리뷰 점수
	, ROUND(AVG(score) OVER(PARTITION BY user_id), 2) AS user_avg_score
	-- 개별 리뷰 점수와 사용자 평균 리뷰 점수의 차이
	, ROUND(score - AVG(score) OVER(PARTITION BY user_id), 2) AS user_avg_score_diff
FROM
	review
;