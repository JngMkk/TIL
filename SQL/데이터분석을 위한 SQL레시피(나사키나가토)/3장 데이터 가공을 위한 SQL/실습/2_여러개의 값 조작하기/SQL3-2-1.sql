DROP TABLE IF EXISTS mst_user_location;
CREATE TABLE mst_user_location (
    user_id   varchar(255)
  , pref_name varchar(255)
  , city_name varchar(255)
);

INSERT INTO mst_user_location
VALUES
    ('U001', '서울특별시', '강서구')
  , ('U002', '경기도수원시', '장안구'  )
  , ('U003', '제주특별자치도', '서귀포시')
;

-- 문자열을 연결하는 쿼리
SELECT
	user_id
	-- PostgreSQL, Hive, SparkSQL 모두 CONCAT 함수 사용 가능
	, CONCAT(pref_name, city_name) AS pref_city
	-- PostgreSQL의 경우 || 연산자도 사용 가능
	-- , pref_name || city_name AS pref_city
	
	-- 지역 이름 사이 띄어쓰기 넣는 법?
	-- PostgreSQL, Hive, SparkSQL
	-- , CONCAT(pref_name, ' ', city_name)
FROM
	mst_user_location
;

-- || 연산자 사용
SELECT
	user_id
	-- PostgreSQL의 경우 || 연산자도 사용 가능
	, pref_name || city_name AS pref_city
FROM
	mst_user_location
;

-- 지역 이름에 띄어쓰기 추가
SELECT
	user_id
	-- 지역 이름 사이 띄어쓰기 넣는 법?
	-- PostgreSQL, Hive, SparkSQL
	, CONCAT(pref_name, ' ', city_name) AS pref_city
FROM
	mst_user_location
;