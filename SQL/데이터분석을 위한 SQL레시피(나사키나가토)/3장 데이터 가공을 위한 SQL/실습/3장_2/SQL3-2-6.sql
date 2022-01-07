-- inet 자료형을 사용한 IP 주소 비교 쿼리
SELECT
	CAST('127.0.0.1' AS inet) < CAST('127.0.0.2' AS inet) AS lt
	, CAST('127.0.0.1' AS inet) > CAST('192.168.0.1' AS inet) AS gt
;

-- inet 자료형을 사용해 IP 주소 범위를 다루는 쿼리
SELECT CAST('127.0.0.1' AS inet) << CAST('127.0.0.0/8' AS inet) AS is_contained;

-- IP 주소에서 4개의 10진수 부분을 추출하는 쿼리
SELECT
	ip
	-- Postgre : split_part로 문자열 분해
	, CAST(split_part(ip, '.', 1) AS integer) AS ip_part1
	, CAST(split_part(ip, '.', 2) AS integer) AS ip_part2
	, CAST(split_part(ip, '.', 3) AS integer) AS ip_part3
	, CAST(split_part(ip, '.', 4) AS integer) AS ip_part4
	-- Hive, SparkSQL : split 함수을 이용해 배열로 분해, n번째 요소 추출
	-- '.'이 특수 문자이기 때문에 이스케이프 처리
	-- , CAST(split(ip, '\\.')[0] AS int) ip_part1
	-- , CAST(split(ip, '\\.')[1] AS int) ip_part2
	-- , CAST(split(ip, '\\.')[2] AS int) ip_part3
	-- , CAST(split(ip, '\\.')[3] AS int) ip_part4
-- FROM
-- 	(SELECT '192.168.0.1' AS ip) AS t
FROM
	(SELECT CAST('192.168.0.1' AS text) AS ip) AS t
;

-- IP 주소를 정수 자료형 표기로 변환하는 쿼리
SELECT
	ip
	-- PostgreSQL : split_part
	, CAST(split_part(ip, '.', 1) AS integer) * 2^24
		+ CAST(split_part(ip, '.', 2) AS integer) * 2^16
		+ CAST(split_part(ip, '.', 3) AS integer) * 2^8
		+ CAST(split_part(ip, '.', 4) AS integer) * 2^0
	AS ip_integer
	
	-- Hive, SparkSQL : split으로 분해, n번째 요소 추출
	-- '.' 특수문자. 이스케이프 처리
	-- , CAST(split(ip, '\\.')[0] AS int) * pow(2, 24)
	-- 	+ CAST(split(ip, '\\.')[1] AS int) * pow(2, 16)
	-- 	+ CAST(split(ip, '\\.')[2] AS int) * pow(2, 8)
	-- 	+ CAST(split(ip, '\\.')[3] AS int) * pow(2, 0)
	-- AS ip_integer
-- FROM
-- 	(SELECT '192.168.0.1' AS ip) AS t
FROM
	(SELECT CAST('192.168.0.1' AS text) AS ip) As t
;

-- IP 주소를 0으로 메운 문자열로 변환하는 쿼리
SELECT
	ip
	-- PostgreSQL : lpad 함수로 0 채우기
	, lpad(split_part(ip, '.', 1), 3, '0')
		|| lpad(split_part(ip, '.', 2), 3, '0')
		|| lpad(split_part(ip, '.', 3), 3, '0')
		|| lpad(split_part(ip, '.', 4), 3, '0')
	AS ip_padding
	
	-- Hive, SparkSQL : split
-- 	, CONCAT(
--     	lpad(split(ip, '\\.')[0], 3, '0')
--     	, lpad(split(ip, '\\.')[1], 3, '0')
--     	, lpad(split(ip, '\\.')[2], 3, '0')
--     	, lpad(split(ip, '\\.')[3], 3, '0'))
--     AS ip_padding
-- FROM
-- 	(SELECT '192.168.0.1' AS ip) AS t
FROM
	(SELECT CAST('192.168.0.1' AS text) AS ip) AS t
;
