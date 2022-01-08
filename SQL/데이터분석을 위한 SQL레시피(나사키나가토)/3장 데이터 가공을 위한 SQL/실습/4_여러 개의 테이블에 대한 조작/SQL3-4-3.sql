DROP TABLE IF EXISTS mst_users_with_card_number;
CREATE TABLE mst_users_with_card_number (
    user_id     varchar(255)
  , card_number varchar(255)
);

INSERT INTO mst_users_with_card_number
VALUES
    ('U001', '1234-xxxx-xxxx-xxxx')
  , ('U002', NULL                 )
  , ('U003', '5678-xxxx-xxxx-xxxx')
;

DROP TABLE IF EXISTS purchase_log;
CREATE TABLE purchase_log (
    purchase_id integer
  , user_id     varchar(255)
  , amount      integer
  , stamp       varchar(255)
);

INSERT INTO purchase_log
VALUES
    (10001, 'U001', 200, '2017-01-30 10:00:00')
  , (10002, 'U001', 500, '2017-02-10 10:00:00')
  , (10003, 'U001', 200, '2017-02-12 10:00:00')
  , (10004, 'U002', 800, '2017-03-01 10:00:00')
  , (10005, 'U002', 400, '2017-03-02 10:00:00')
;

-- 신용 카드 등록과 구매 이력 유무를 0과 1이라는 플래그로 나타내는 쿼리
SELECT
	m.user_id
	, m.card_number
	, COUNT(p.user_id) AS purchase_count
	-- 신용 카드 번호를 등록한 경우 1, 등록하지 않은 경우 0으로 표현하기
	, CASE WHEN m.card_number IS NOT NULL THEN 1 ELSE 0 END AS has_card
	-- 구매 이력이 있는 경우 1, 없는 경우 0으로 표현하기
	, SIGN(COUNT(p.user_id)) AS has_purchased
FROM
	mst_users_with_card_number AS m
	LEFT JOIN
		purchase_log AS p
		ON m.user_id = p.user_id
GROUP BY m.user_id, m.card_number
ORDER BY user_id
;