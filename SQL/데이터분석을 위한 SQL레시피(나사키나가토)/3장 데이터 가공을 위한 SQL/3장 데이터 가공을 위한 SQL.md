# 3장 데이터 가공을 위한 SQL

## 하나의 값 조작하기

> 수집한 데이터 일부는 원래 분석 용도가 아니어서 분석에 활용하기 어려운 경우가 있다
>
> 이러한 경우 데이터를 가공해서 분석하기 쉽게 유지해두는 편이 좋다

- 데이터를 가공해야 하는 이유

  - 다룰 데이터가 데이터 분석 용도로 상정되지 않은 경우

    ```
    업무 데이터를 다루는 경우 데이터베이스에 코드 값을 저장하고,
    이러한 코드 값의 의미를 다른 테이블에서 관리하는 경우가 있다.
    만약 이러한 코드를 사용해 리포트를 작성한다면, 리포트의 코드가 무엇을 의미하는지 정확하게 알 수 없음
    
    추가로 접근 로그는 어떤 행동을 하나의 문자열로 표하는 경우가 많다.
    예를 들어 관례에 따라서 여러 개의 정보가 하나의 문자열로 저장되어 있다면,
    이를 SQL에서 다루기는 어려우므로 데이터 분석에 적합한 형태로 미리 가공해서 저장해두어야 한다.
    ```

  - 연산할 때 비교 가능한 상태로 만들고 오류를 회피하기 위한 경우

    ```
    로그 데이터와 업무 데이터를 함께 다루는 경우, 각 데이터에 있는 데이터 형식이 일치하지 않을 수 있다.
    따라서 두 데이터를 모두 활용해 집계한다면 데이터 형식을 통일해두는 것이 좋다.
    
    추가로 어떤 값과 NULL을 연산하면 결과가 NULL이 나올 수 있다.
    이로 인해 오류가 발생해 원하는 결과를 얻을 수 없는 경우가 꽤 많으므로,
    미리 데이터를 가공해 NULL이 발생하지 않게 만들어두는 것이 좋다.
    ```



### 1. 코드 값을 레이블로 변경하기

> CASE 식

```
로그 데이터 또는 업무 데이터로 저장된 코드 값을 그대로 집계에 사용하면 리포트의 가독성이 낮아진다.
따라서 리포트를 작성할 때 변환하는 등의 작업을 해야 한다.
집계할 때 미리 코드 값을 레이블로 변경하는 방법을 살펴보자.

다음 데이터처럼 회원 등록 때 사용한 장치를 저장하는 컬럼(register_device)이
코드 값(1:Desktop 2:Smartphone 3:Application)으로 저장되어 있다.
이를 레이블로 바꿔보자.

코드값을 레이블로 변경하는 것처럼 특정 조건 기반으로 값을 결정할 때는 CASE 식을 사용한다.
CASE 식의 구문은 CASE 뒤에 'WHEN <조건식> THEN <조건을 만족할 때의 값>'을 나열하고, 마지막을 END로 끝내는 형태.
만약 조건식에 해당하는 경우가 없다면 NULL이 되지만,
마지막에 'ELSE <값>'형태를 사용해서 디폴트 값을 별도로 지정해줄 수 있다.
```

- 사용자 마스터(mst_users) 테이블

| user_id | register_date | register_device |
| ------- | ------------- | --------------- |
| U001    | 2016-08-26    | 1               |
| U002    | 2016-08-26    | 2               |
| U003    | 2016-08-27    | 3               |

- 코드를 레이블로 변경하는 쿼리

```SQL
SELECT
	user_id
	, CASE
		WHEN register_device = 1 THEN 'Desktop'
		WHEN register_device = 2 THEN 'Smartphone'
		WHEN register_device = 3 THEN 'Application'
		-- 디폴트 값을 지정할 경우 ELSE 구문 사용
		-- ELSE ''
	END AS device_name
FROM mst_users
;
```

- 실행결과

| user_id | device_name |
| ------- | ----------- |
| U001    | Desktop     |
| U002    | Smartphone  |
| U003    | Application |

- 정리
```
CASE 식은 기본적인 SQL 구문이지만, 데이터 변환에 굉장히 많이 사용된다.
복잡한 구문과 CASE 식을 조합해서 사용하는 경우가 많으므로,
CASE 식을 어떻게 사용하는지 확실히 기억해야 한다.
```



### 2. URL에서 요소 추출하기

> URL 함수, 정규 표현식

```
분석 현장에서는 서비스 런칭 때에 로그 조건과 분석 요건을 제대로 검토하지 못하고,
일단 최소한의 요건으로 레퍼러와 페이지 URL을 저장해두는 경우가 있다.
그리고 이후에 저장한 URL을 기반으로 요소들을 추출한다.
```



- 접근 로그(access_log) 테이블

| stamp               | referrer                                              | url                                        |
| ------------------- | ----------------------------------------------------- | ------------------------------------------ |
| 2016-08-26 12:02:00 | http://www.other.com/path1/index.php?k1=v1&k2=v2#Ref1 | http://www.example.com/video/detail?id=001 |
| 2016-08-26 12:02:01 | http://www.other.net/path1/index.php?k1=v1&k2=v2#Ref1 | http://www.example.com/video#ref           |
| 2016-08-26 12:02:01 | https://www.other.com/                                | http://www.example.com/book/detail?id=002  |

#### 2-1. 레퍼러로 어떤 웹 페이지를 거쳐 왔는지 판별하기


```
어떤 웹 페이지를 거쳐 넘어왔는지 판별할 때는 레퍼러를 집계한다.
하지만 이를 위 테이블처럼 페이지 단위로 집계하면 밀도가 너무 작아 복잡해지므로,
호스트 단위로 집계하는 것이 일반적이다.

참고로 Hive 또는 BigQuery에는 URL을 다루는 함수가 있다.
하지만 구현되지 않은 미들웨어에서는 정규 표현식으로 호스트 이름의 패턴을 추출해야 한다.
```

- 레퍼러 도메인을 추출하는 쿼리

```sql
SELECT
	stamp
	-- referrer의 호스트 이름 부분 추출하기
	-- PostgreSQL의 경우 substring 함수와 정규 표현식 사용하기
	, substring(referrer from 'https?://([^/]*)') AS referrer_host
	-- Hive, SparkSQL의 경우 parse_url 함수로 호스트 이름 추출하기
	-- , pasre_url(referrer, 'HOST') AS referrer_host
FROM access_log
;
```

- 실행결과

| stamp               | referrer_host |
| ------------------- | ------------- |
| 2016-08-26 12:02:00 | www.other.com |
| 2016-08-26 12:02:01 | www.other.net |
| 2016-08-26 12:02:01 | www.other.com |



#### 2-2. URL에서 경로와 요청 매개변수 값 추출하기

```
상품과 관련된 리포트를 작성할 때, 어떤 상품이 열람되는지 특정하는 ID를 데이터로 따로 저장해두지 않은 경우가 있을 수 있다.
그래도 URL을 로그 데이터로 저장해두었다면 URL경로를 가공해서 상품 리포트를 만들 수 있다.

다음 코드 예는 URL 경로와 GET 요청 매개변수에 있는 특정 키를 추출하는 쿼리
```

- URL 경로와 GET 매개변수에 있는 특정 키 값을 추출하는 쿼리

```SQL
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
```

- 실행결과

| stamp               | url                                        | path          | id     |
| ------------------- | ------------------------------------------ | ------------- | ------ |
| 2016-08-26 12:02:00 | http://www.example.com/video/detail?id=001 | /video/detail | 001    |
| 2016-08-26 12:02:01 | http://www.example.com/video#ref           | /video        | [null] |
| 2016-08-26 12:02:01 | http://www.example.com/book/detail?id=002  | /book/detail  | 002    |

- 정리

```
URL 처리는 웹 서비스 로그 분석에서 자주 사용되는 기술이다.
하지만 미들웨어에 따라서 함수 이름이 다르거나,
정규 표현식의 작성 방법이 달라 자주 문제가 발생하는 부분이다.
```



### 3. 문자열을 배열로 배분하기

> split_part 함수, substring 함수, (Hive, SparkSQL) parse_url 함수

```
빅데이터 분석에서 가장 많이 사용되는 자료형은 문자열이지만,
문자열 자료형은 범용적인 자료형이므로 더 세부적으로 분해해서 사용해야 하는 경우가 많다.
예를 들어 영어 문장을 공백으로 분할해서 하나하나의 단어로 구분하는 경우,
쉼표로 연결된 데이터를 잘라 하나하나의 값을 추출하는 경우 등

앞에서 사용한 접근 로그 샘플을 기반으로 페이지 계층을 나누어 보자.
다음 코드에는 URL 경로를 슬래시로 분할해서 계층을 추출하는 쿼리다.
```

- URL 경로를 슬래시로 분할해서 계층을 추출하는 쿼리

```SQL
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
```

- 실행결과

| stamp               | url                                        | path1 | path2  |
| ------------------- | ------------------------------------------ | ----- | ------ |
| 2016-08-26 12:02:00 | http://www.example.com/video/detail?id=001 | video | detail |
| 2016-08-26 12:02:01 | http://www.example.com/video#ref           | video |        |
| 2016-08-26 12:02:01 | http://www.example.com/book/detail?id=002  | book  | detail |



### 4. 날짜와 타임스탬프 다루기

> 날짜/시간 함수, 날짜 자료형, 타임스탬프 자료형, 문자열 함수

```
로그 데이터를 처리할 때는 날짜 또는 타임 스탬프 등의 시간 정보가 굉장히 많이 활용된다.
하지만 미들웨어에 따라서 시간 정보를 다루는 자료형 또는 함수에 큰 차이가 있다.
지금부터 날짜와 타임스탬프를 다룰 때 사용하는 방법을 살펴보자.
```

#### 4-1. 현재 날짜와 타임스탬프 추출하기

```
미들웨어에 따라 추출 방법이 다르다.
추가로 같은 쿼리를 작성해도 미들웨어마다 리턴 값이 달라지는 경우가 있다.

PostgreSQL에서는 CURRENT_TIMESTAMP의 리턴 값으로 타임존이 적용된 타임스탬프 자료형이 나온다.
하지만 이 이외의 미들웨어는 타임존 없는 타임스탬프를 리턴한다.
따라서 리턴 값의 자료형을 맞출 수 있게 PostgreSQL에서는 LOCALTIMESTAMP를 사용하는 것이 좋다.
```

- 현재 날짜와 타임스탬프를 추출하는 쿼리

```SQL
SELECT
	-- PostgreSQL, Hive의 경우
	-- CURRENT_DATE 상수와 CURRENT_TIMESTAMP 상수 사용하기
	CURRENT_DATE AS dt
    , CURRENT_TIMESTAMP AS stamp
    -- Hive, SparkSQL의 경우
    -- CURRENT_DATE() 함수와 CURRENT_TIMESTAMP() 함수 사용하기
    -- CURRENT_DATE() AS dt
    -- , CURRENT_TIMESTAMP() AS stamp
    -- PostgreSQL의 경우 CURRENT_TIMESTAMP는 타임존이 적용된 타임스탬프
    -- 타임존을 적용하고 싶지 않으면 LOCALTIMESTAMP 사용
    -- , LOCALTIMSTAMP AS stamp
;
```

- 실행결과 (CURRENT_TIMESTAMP)

| dt         | stamp                         |
| ---------- | ----------------------------- |
| 2022-01-04 | 2022-01-04 23:50:39.078843+09 |

- 실행결과 (LOCALTIMESTAMP)

| dt         | stamp                      |
| ---------- | -------------------------- |
| 2022-01-04 | 2022-01-04 23:50:55.499099 |



#### 4-2. 지정한 값의 날짜/시각 데이터 추출하기

```
현재 시각이 아니라 문자열로 지정한 날짜와 시각을 기반으로
날짜 자료형과 타임스탬프 자료형의 데이터를 만드는 경우가 있다.
미들웨어에 따라 다양한 방법이 있지만 CAST 함수를 사용하는 방법이 가장 범용적이다.
```

- 문자열을 날짜 자료형, 타임스탬프 자료형으로 변환하는 쿼리

```SQL
SELECT
	-- PostgreSQL, Hive, SparkSQL 모두 'CAST(vale AS type)' 사용
	CAST('2021-12-31' AS date) AS dt
	, CAST('2021-12-31 23:59:59' AS timestamp) AS stamp
	
	-- Hive의 경우 'type(value)' 사용하기
	-- date('2021-12-31') AS dt
	-- , timestamp('2021-12-31 23:59:59') AS stamp
	
	-- PostgreSQL, Hive, SparkSQL 모두 'type value' 사용
	-- 다만 value는 상수이므로 컬럼 이름으로 지정할 수 없음
	-- date '2021-12-31' AS dt
	-- , timestamp '2021-12-31 23:59:59' AS stamp
	
	-- PostgreSQL의 경우 'value::type' 사용
	-- '2021-12-31'::date AS dt
	-- , '2021-12-31 23:59:59'::timestamp AS stamp
;
```

- 실행결과

| dt         | stamp               |
| ---------- | ------------------- |
| 2021-12-31 | 2021-12-31 23:59:59 |



#### 4-3. 날짜/시각에서 특정 필드 추출하기

```
타임스탬프 자료형의 데이터에서 년과 월 등의 특정 필드 값을 추출할 때는 EXTRACT 함수 사용.
EXTRACT 함수를 지원하지 않는 Hive와 SparkSQL은 각각의 필드를 추출하는 별도의 함수가 제공.
```

- 타임스탬프 자료형의 데이터에서 연, 월, 일 등을 추출하는 쿼리

```sql
SELECT
	stamp
	-- PostgreSQL의 경우 EXTRACT 함수 사용
	, EXTRACT(YEAR FROM stamp) AS year
	, EXTRACT(MONTH FROM stamp) AS month
	, EXTRACT(DAY FROM stamp) AS day
	, EXTRACT(HOUR FROM stamp) AS hour
	
	-- Hive, SparkSQL의 경우
	-- , YEAR(stamp) AS year
	-- , MONTH(stamp) AS month
	-- , DAY(stamp) AS day
	-- , HOUR(stamp) AS hour
FROM
	(SELECT CAST('2022-01-01 00:00:00' AS timestamp) AS stamp) As t
;
```

- 실행결과

| stamp               | year | month | day  | hour |
| ------------------- | ---- | ----- | ---- | ---- |
| 2022-01-01 00:00:00 | 2022 | 1     | 1    | 0    |

---



```
날짜 자료형과 타임 스탬프 자료형을 사용하지 않아도,
타임스탬프를 단순한 문자열처럼 취급해서 문자열 조작을 통해 필드를 추출할 수 있다.

다음 코드는 substing 함수를 사용해 문자열을 추출하는 쿼리.
연과 월을 동시에 추출해서 월별 리포트를 만들 때 많이 사용한다.
참고로 이처럼 문자열을 사용하는 코드는 미들웨어에 따라 큰 차이가 없다.
```

- 타임스탬프를 나타내는 문자열에서 연, 월, 일 등을 추출하는 쿼리

```sql
SELECT
	stamp
	-- PostgreSQL, Hive, SparkSQL에서는 substring 함수 사용
	, substring(stamp, 1, 4) AS year
	, substring(stamp, 6, 2) AS month
	, substring(stamp, 9, 2) AS day
	, substring(stamp, 12, 2) AS hour
	-- 연과 월을 함께 추출
	, substring(stamp, 1, 7) AS year_month
	
	-- PostgreSQL, Hive, SparkSQL에서는 substr 함수 사용
	-- , substr(stamp, 1, 4) AS year
	-- , substr(stamp, 6, 2) AS month
	-- , substr(stamp, 9, 2) AS day
	-- , substr(stamp, 12, 2) AS hour
	-- , substr(stamp, 1, 7) AS year_month
FROM
	-- PostgreSQL의 경우 문자열 자료형으로 text 사용
	(SELECT CAST('2022-02-02 02:02:02' AS text) AS stamp) AS t
	-- Hive, SparkSQL의 경우 문자열 자료형으로 string 사용
	-- (SELECT CAST('2022-02-02 02:02:02' AS string) AS stamp) AS t
;
```

- 실행결과

| stamp               | year | month | day  | hour | year_month |
| ------------------- | ---- | ----- | ---- | ---- | ---------- |
| 2022-02-02 02:02:02 | 2022 | 02    | 02   | 02   | 2022-02    |

- 정리

```
날짜와 시간 정보는 로그 데이터에서 빠지지 않는 정보이다.
타임존을 고려해야 하고, 미들웨어들의 차이를 주의해야 한다.
```



### 5. 결손 값을 디폴트 값으로 대치하기

> COALESCE 함수

```
문자열 또는 숫자를 다룰 때 중간에 NULL이 들어있는 경우를 주의해야 한다.
NULL과 문자열을 결합하면 NULL이 되며, NULL과 숫자를 사칙 연산해도 NULL이 된다.
처리 대상인 데이터가 우리가 원하는 형태가 아닐 경우에는 반드시 데이터를 가공해야 한다.

구매액과 NULL을 포함하는 쿠폰 금액이 저장된 테이블이 있을 때,
다음 코드는 쿠폰으로 할인했을 때 매출 금액을 구하는 쿼리이다.
```

- 쿠폰 사용 여부가 함께 있는 구매 로그(purchase_log_with_coupon) 테이블

| purchase_id | amount | coupon |
| ----------- | ------ | ------ |
| 10001       | 3280   | [null] |
| 10002       | 4650   | 500    |
| 10003       | 3870   | [null] |

- 구매액에서 할인 쿠폰 값을 제외한 매출 금액을 구하는 쿼리

```sql
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
```

- 실행결과
| purchase_id | amount | coupon | discount_amount1 | discount_amount2 |
| ----------- | ------ | ------ | ---------------- | ---------------- |
| 10001       | 3280   | [null] | [null]           | 3280             |
| 10002       | 4650   | 500    | 4150             | 4150             |
| 10003       | 3870   | [null] | [null]           | 3870             |

```
이 코드 예에서 discount_price1은 price에서 coupon을 그대로 뺀 값이다.
따라서 coupon이 NULL 레코드라면 NULL이 된다.
discount_price2는 coupon이 NULL일 때 COALESCE 함수를 사용해 0으로 대치하므로,
coupon을 사용하지 않은 경우에도 제대로 된 값이 계산된다.
```

