DROP TABLE IF EXISTS access_log ;
CREATE TABLE access_log (
    stamp    varchar(255)
  , referrer text
  , url      text
);

INSERT INTO access_log 
VALUES
    ('2016-08-26 12:02:00', 'http://www.other.com/path1/index.php?k1=v1&k2=v2#Ref1', 'http://www.example.com/video/detail?id=001')
  , ('2016-08-26 12:02:01', 'http://www.other.net/path1/index.php?k1=v1&k2=v2#Ref1', 'http://www.example.com/video#ref'          )
  , ('2016-08-26 12:02:01', 'https://www.other.com/'                               , 'http://www.example.com/book/detail?id=002' )
;

-- 레퍼러 도메인을 추출하는 쿼리
SELECT
	stamp
	-- referrer의 호스트 이름 부분 추출하기
	-- PostgreSQL의 경우 substring 함수와 정규 표현식 사용하기
	, substring(referrer from 'https?://([^/]*)') AS referrer_host
	-- Hive, SparkSQL의 경우 parse_url 함수로 호스트 이름 추출하기
	-- , pasre_url(referrer, 'HOST') AS referrer_host
FROM access_log
;


-- URL 경로와 GET 매개변수에 있는 특정 키 값을 추출하는 쿼리
SELECT
	stamp
	, url
	-- URL 경로 또는 GET 매개변수의 ID 추출하기
	-- PostgreSQL의 경우 substring 함수와 정규 표현식 사용
	, substring(url from '//[^/]+([^?#]+)') AS path
	, substring(url from 'id=([^&]*)') AS id
	-- Hive, SparkSQL의 경우 parse_url 함수로 URL 경로 부분 또는 쿼리 매개변수 부분의 값 추출
	-- , parse_url(url, 'PATH') AS path
	-- , parse_url(url, 'QUERY', 'id') AS id
FROM access_log
;


