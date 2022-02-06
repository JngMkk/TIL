-- 데이터 입력과 삭제 그리고 수정
-- 1. INSERT
-- SELECT 문과 결합하면 한 번에 여러 개의 로우 데이터를 입력할 수 있음.

-- CREATE TABLE ... AS 구문을 사용한 테이블 생성
create table subway_dml_test as
select * from subway_statistics where rownum < 1;

alter table subway_dml_test add primary key (seq_id);
/*
SELECT 절에서 조회된 결과 형태로 자동으로 테이블이 만들어짐과 동시에 데이터까지 복사됨.
여기서는 WHERE < 1이란 조건 때문에 데이터는 하나도 만들어지지 않음.
ROWNUM이랑 오라클에서만 사용할 수 있는 의사컬럼으로 SELECT 문에서 반환되는 로우 수를 말함
CREATE TABLE ... AS 구문으로 테이블을 생성하면 일일이 컬럼 정의를 명시하지 않아도 됨
단점은 인덱스나 기본 키는 만들 수 없다는 점
따라서 ALTER TABLE 문장을 사용해 기본 키를 생성해야함
기본 키 혹은 컬럼을 추가하거나 컬럼 정의 내용을 변경, 컬럼을 삭제할 때도 ALTER TABLE 사용
*/

-- 종합운동장역 데이터 입력
insert into subway_dml_test
select * from subway_statistics where station_name like '종합운동장%';

commit;

select * from subway_dml_test;

-- subway_dml_test 테이블에 subway_statistics 전체 데이터 입력
insert into subway_dml_test
select * from subway_statistics;
-- 오류 발생 ORA-00001: 무결성 제약 조건(C##JNGMK.SYS_C008333)에 위배됩니다
-- SYS_C008333 : subway_dml_test 테이블의 기본 키를 의미
-- 종합운동장역이 원래 들어가 있는데 다시 입력하려다 보니 seq_id 값이 중복되어 오류

-- 중복데이터 제외하고 데이터 입력
insert into subway_dml_test
select * from subway_statistics where station_name not like '종합운동장%';

commit;

-- 기본 키와 충돌하지 않게 데이터 입력
insert into subway_dml_test
select a.* from subway_statistics a
where not exists (select 1 from subway_dml_test b where a.seq_id = b.seq_id);

-- 2. DELETE
/*
DELETE 문은 INSERT 문과 다르게 SELECT 문장과 연결하는 형태는 없음
테이블에서 데이터를 삭제하므로 SELECT  문이 필요 없음
하지만 어떤 데이터를 삭제할 것인지 WHERE 절을 추가해 조건을 걸 수 있음
*/

-- 종합운동장역 데이터 삭제
delete from subway_dml_test
where station_name like '종합운동장%';

commit;

-- 3. UPDATE
-- 데이터 수정
/*
UPDATE 테이블 명
SET COLUMN1 = 값1
    ,COLUMN2 = 값2
    , ...
WHERE 절;

UPDATE 다음 수정할 테이블 명을 명시하고 SET 다음에 수정할 컬럼과 수정할 값을 '컬럼 = 값'
형태로 명시. 여러 개의 컬럼 값을 수정하려면 콤마(,)로 구분해 계속 추가하면 됨
여기서 '='기호는 WHERE 조건절에서 사용했던 동등 연산자가 아니라 '='를 기준으로 오른쪽 값을
왼쪽 컬럼 값에 할당하라는 의미. 또한, 테이블에서 특정 데이터만 수정해야 할 경우에는
WHERE 절을 추가해 적절한 조건을 주면 됨
*/

-- 변겅 전 삼성역 데이터
SELECT * FROM subway_dml_test
WHERE station_name LIKE '삼성%'
ORDER BY seq_id;

-- UPDATE 문
UPDATE subway_dml_test
SET passenger_number = passenger_number + 10
    , boarding_date = ADD_MONTHS(boarding_date, 1)
WHERE station_name LIKE '삼성%';

commit;

-- 변경 후 삼성역 데이터
select * from subway_dml_test
where station_name like '삼성%'
order by seq_id;
