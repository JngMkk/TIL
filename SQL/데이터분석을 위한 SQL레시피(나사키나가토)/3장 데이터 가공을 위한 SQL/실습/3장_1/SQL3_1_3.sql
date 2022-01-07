-- URL 경로를 슬래시로 분할해서 계층을 추출하는 쿼리
SELECT
	stamp
	, url
	-- 경로를 슬래시로 잘라 배열로 분할하기
	-- 경로가 반드시 슬래시로 시작하므로 2번째 요소가 마지막 계층
	-- PostgreSQL의 경우 split_part로 n번째 요소 추출하기
	, split_part(substring(url from '//[^/]+([^?#]+)'), '/', 2) AS path1
	, split_part(substring(url from '//[^/]+([^?#]+)'), '/', 3) AS path2
	-- Hive, SparkSQL도 split 함수를 사용해 배열로 자름
	-- 다만 배열의 인덱스가 0부터 시작하므로 주의하기
	-- , split(parse_url(url, 'PATH'), '/')[1] AS path1
	-- , split(parse_url(url, 'PATH'), '/')[2] AS path2
FROM access_log
;