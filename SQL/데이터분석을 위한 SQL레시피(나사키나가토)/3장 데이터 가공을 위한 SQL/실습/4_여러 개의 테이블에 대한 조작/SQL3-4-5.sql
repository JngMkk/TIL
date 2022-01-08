-- 디바이스 ID와 이름의 마스터 테이블을 만드는 쿼리
WITH
mst_devices AS(
			  SELECT 1 AS device_id, 'PC' AS device_name
	UNION ALL SELECT 2 AS device_id, 'SP' AS device_name
	UNION ALL SELECT 3 AS device_id, 'Application' AS device_name
)
SELECT *
FROM mst_devices
;

-- 유사 테이블을 사용해 코드를 레이블로 변환하는 쿼리
WITH
mst_devices AS(
			  SELECT 1 AS device_id, 'PC' AS device_name
	UNION ALL SELECT 2 AS device_id, 'SP' AS device_name
	UNION ALL SELECT 3 AS device_id, 'Application' AS device_name
)
SELECT
	u.user_id
	, d.device_name
FROM
	mst_users AS u
	LEFT JOIN
		mst_devices AS d
		ON u.register_device = d.device_id
;

-- VALUES 구문을 사용해 동적으로 테이블을 만드는 쿼리
WITH
mst_devices(device_id, device_name) AS (
	VALUES
		(1, 'PC')
		,(2, 'SP')
		,(3, 'Application')
)
SELECT *
FROM mst_devices
;

-- 순번을 가진 유사 테이블을 작성하는 쿼리
WITH
series AS (
	-- 1부터 5까지의 순번 생성하기
	-- PostgreSQL : generate_series 사용
	SELECT generate_series(1, 5) AS idx
)
SELECT *
FROM series
;