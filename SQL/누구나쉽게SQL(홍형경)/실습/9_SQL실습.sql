-- SQL 실습
-- 나눔로또 분석
-- lotto_master 테이블 생성
CREATE TABLE lotto_master(
    seq_no NUMBER NOT NULL, -- 로또회차
    draw_date DATE,         -- 추첨일
    num1 NUMBER,            -- 당첨번호1
    num2 NUMBER,            -- 당첨번호2
    num3 NUMBER,            -- 당첨번호3
    num4 NUMBER,            -- 당첨번호4
    num5 NUMBER,            -- 당첨번호5
    num6 NUMBER,            -- 당첨번호6
    bonus NUMBER);          -- 보너스번호
    
ALTER TABLE lotto_master
ADD CONSTRAINTS lotto_master_pk PRIMARY KEY (seq_no);

-- lotto_detail 테이블 생성
CREATE TABLE lotto_detail(
    seq_no NUMBER NOT NULL,     -- 로또회차
    rank_no NUMBER NOT NULL,    -- 등수
    win_person_no NUMBER,       -- 당첨자 수
    win_money NUMBER);          -- 1인당 당첨금액
    
ALTER TABLE lotto_detail
ADD CONSTRAINTS lotto_detail_pk PRIMARY KEY (seq_no, rank_no);

select * from lotto_master order by 1;

-- 중복 번호 조회
-- 중복된 로또 번호 존재 여부 조회(GROUP BY)
select num1, num2, num3, num4, num5, num6, count(*)
from lotto_master
group by num1, num2, num3, num4, num5, num6;

-- 중복된 로또 번호 존재 여부 조회(GROUP BY & HAVING)
select num1, num2, num3, num4, num5, num6, count(*)
from lotto_master
group by num1, num2, num3, num4, num5, num6
having count(*) > 1;
-- 조회된 데이터 없음. 이로써 827회까지 중복된 당첨번호는 없음을 알 수 있음.

-- 가장 많이 당첨된 당첨번호 조회 (보너스번호 제외)
-- num1 컬럼 값의 당첨 건수 조회
select num1 lotto_num, count(*) cnt
from lotto_master group by num1 order by 2 desc;

-- 가장 많은 당첨번호 조회
select lotto_num, sum(cnt) as cnt
from (select num1 lotto_num, count(*) cnt
        from lotto_master
        group by num1
        union all
        select num2 lotto_num, count(*) cnt
        from lotto_master
        group by num2
        union all
        select num3 lotto_num, count(*) cnt
        from lotto_master
        group by num3
        union all
        select num4 lotto_num, count(*) cnt
        from lotto_master
        group by num4
        union all
        select num5 lotto_num, count(*) cnt
        from lotto_master
        group by num5
        union all
        select num6 lotto_num, count(*) cnt
        from lotto_master
        group by num6)
        group by lotto_num
        order by 2 desc;

-- 가장 많은 당첨금이 나온 회차와 번호, 금액 조회
-- 최대 당첨금과 당첨번호 조회
select a.seq_no
        ,a.draw_date
        ,b.win_person_no
        ,b.win_money
        ,a.num1, a.num2, a.num3, a.num4, a.num5, a.num6, a.bonus
        from lotto_master a, lotto_detail b
        where a.seq_no = b.seq_no
        and b.rank_no = 1
        order by b.win_money desc;


-- 교통사고 분석
-- 국가교통 DB(www.ktdb.go.kr)
-- traffic_accident 테이블 생성
create table traffic_accident(
    year number not null,               -- 연도
    trans_type varchar2(30) not null,   -- 교통수단
    total_acct_num number,              -- 사고 건수
    death_person_num number);           -- 사망자 수
    
alter table traffic_accident
add constraints traffic_accident_pk primary key (year, trans_type);

select * from traffic_accident;

-- 연대, 교통수단별 총 사고 건수 조회
-- 연대, 교통수단별 사고, 사망 건수 조회
select case when year between 1980 and 1989 then '1980년대'
            when year between 1990 and 1999 then '1990년대'
            when year between 2000 and 2009 then '2000년대'
            when year between 2010 and 2019 then '2010년대'
            end as years
            ,trans_type
            ,sum(total_acct_num) as 사고건수
            ,sum(death_person_num) as 사망자수
    from traffic_accident
    where 1 = 1
    group by case when year between 1980 and 1989 then '1980년대'
                  when year between 1990 and 1999 then '1990년대'
                  when year between 2000 and 2009 then '2000년대'
                  when year between 2010 and 2019 then '2010년대'
                 end, trans_type
    order by 1, 2;
    
-- 연대별 추이 분석
-- 교통수단별 사고 건수 연대별 추이
-- 별칭은 숫자로 시작할 수 없다. "" 로 감싸야 함.
SELECT trans_type
      ,SUM(CASE WHEN year BETWEEN 1980 AND 1989 THEN total_acct_num ELSE 0 END) "1980년대"
      ,SUM(CASE WHEN year BETWEEN 1990 AND 1999 THEN total_acct_num ELSE 0 END) "1990년대"
      ,SUM(CASE WHEN year BETWEEN 2000 AND 2009 THEN total_acct_num ELSE 0 END) "2000년대"
      ,SUM(CASE WHEN year BETWEEN 2010 AND 2019 THEN total_acct_num ELSE 0 END) "2010년대"
FROM traffic_accident
WHERE 1=1
GROUP BY trans_type
ORDER BY trans_type;

-- 교통수단별 사망자 수 연대별 추이
select trans_type,
    sum(case when year between 1980 and 1989 then death_person_num else 0 end) "1980년대",
    sum(case when year between 1990 and 1999 then death_person_num else 0 end) "1990년대",
    sum(case when year between 2000 and 2009 then death_person_num else 0 end) "2000년대",
    sum(case when year between 2010 and 2019 then death_person_num else 0 end) "2010년대"
    from traffic_accident
    where 1 = 1
    GROUP BY trans_type
    ORDER BY trans_type;
    
-- 교통수단별 가장 많은 사망자 수가 발생한 연도 구하기
-- 교통수단별 사망자 수 연도별 추이
-- 서브쿼리 사용
select a.*
from traffic_accident a,
    (select trans_type,
    max(death_person_num) death_per
    from traffic_accident
    group by trans_type) b
    where a.trans_type = b.trans_type
    and a.death_person_num = b.death_per;
    
-- 서울시 미세먼지 분석
-- 에어코리아(https://www.airkorea.or.kr)
-- fine_dust 테이블 생성
create table fine_dust(
    gu_name varchar2(50) not null,          -- 구 명
    mea_station varchar2(30) not null,      -- 측정소
    mea_date date not null,                 -- 측정일자
    pm10 number,                            -- 미세먼지 농도
    pm25 number);                           -- 초미세먼지 농도

alter table fine_dust
add constraints fine_dust_pk primary key (gu_name, mea_station, mea_date);

-- fine_dust_standard 테이블 생성 (미세농도 기준 테이블)
-- 미세먼지와 초미세먼지 농도에 따른 미세먼지 기준 데이터를 담고 있음
create table fine_dust_standard(
    org_name varchar2(50) not null,     -- 기관명
    std_name varchar2(30) not null,     -- 미세먼지 기준(좋음, 보통, 나쁨, 매우나쁨)
    pm10_start number,                  -- 미세먼지 농도(시작 값)
    pm10_end number,                    -- 미세먼지 농도(끝 값)
    pm25_start number,                  -- 초미세먼지 농도(시작 값)
    pm25_end number);                   -- 초미세먼지 농도(끝 값)
    
alter table fine_dust_standard
add constraints fine_dust_standard_pk primary key (org_name, std_name);

-- 월간 미세먼지와 초미세먼지의 최소, 최대, 평균값 구하기
-- 월간 미세먼지의 최소, 최대, 평균값
select to_char(a.mea_date, 'YYYY-MM') months
    ,round(min(a.pm10), 0) pm10_min
    ,round(max(a.pm10), 0) pm10_max
    ,round(avg(a.pm10), 0) pm10_avg
    ,round(min(a.pm25), 0) pm25_min
    ,round(max(a.pm25), 0) pm25_max
    ,round(avg(a.pm25), 0) pm25_avg
    from fine_dust a
    where pm10 > 0
    and pm25 > 0
    group by to_char(mea_date, 'YYYY-MM')
    order by 1;
    
-- 월평균 미세먼지 현황
-- 월평균 미세먼지 상태
select a.months, a.pm10_avg,
        (select b.std_name
        from fine_dust_standard b
        where b.org_name = 'WHO'
        and a.pm10_avg between b.pm10_start and b.pm10_end) "미세먼지 상태"
        ,a.pm25_avg,
        (select b.std_name
        from fine_dust_standard b
        where b.org_name = 'WHO'
        and a.pm25_avg between b.pm25_start and b.pm25_end) "초미세먼지 상태"
    from (select to_char(a.mea_date, 'YYYY-MM') months
    ,round(avg(a.pm10), 0) pm10_avg
    ,round(avg(a.pm25), 0) pm25_avg
    from fine_dust a
    where a.pm10 > 0
    and a.pm25 > 0
    group by to_char(mea_date, 'YYYY-MM')) a
    order by 1;