DROP TABLE IF EXISTS mst_users;
CREATE TABLE mst_users(
    user_id         varchar(255)
  , register_date   varchar(255)
  , register_device integer
);

INSERT INTO mst_users
VALUES
    ('U001', '2016-08-26', 1)
  , ('U002', '2016-08-26', 2)
  , ('U003', '2016-08-27', 3)
;

-- 코드를 레이블로 변경하는 쿼리
SELECT
	user_id
	, CASE
		WHEN register_device = 1 THEN 'Desktop'
		WHEN register_device = 2 THEN 'Smartphone'
		WHEN register_device = 3 THEN 'Application'
		-- 디폴트 값을 지정할 경우 ELSE 구문을 사용
		-- ELSE ''
	END AS device_name
FROM mst_users
;