DROP TABLE IF EXISTS purchase_log_with_coupon;
CREATE TABLE purchase_log_with_coupon (
    purchase_id varchar(255)
  , amount      integer
  , coupon      integer
);

INSERT INTO purchase_log_with_coupon
VALUES
    ('10001', 3280, NULL)
  , ('10002', 4650,  500)
  , ('10003', 3870, NULL)
;

-- 구매액에서 할인 쿠폰 값을 제외한 매출 금액을 구하는 쿼리
SELECT
	purchase_id
	, amount
	, coupon
	, amount - coupon AS discount_amount1
	-- COALESCE(value, 0) : value가 NULL일 때 0으로 대치한다.
	, amount - COALESCE(coupon, 0) AS discount_amount2
FROM
	purchase_log_with_coupon
;
