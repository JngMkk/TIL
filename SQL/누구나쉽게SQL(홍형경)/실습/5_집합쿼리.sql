/*
집합 쿼리

기본적으로 두 개 이상의 독립적인 SELECT 문장을 연결하는 형태.
독립적인 각 SELECT문이 반환하는 결과를 하나의 집합으로 보고,
집합 연산자를 사용해 두 집합을 교집합 형태로 가져올 것인지 합집합 형태로 가져올 것인지
처리할 수 있음. 집합 쿼리로 연결되는 독립적인 두 SELECT문이 반환하는 결과의 컬럼 수와
데이터형은 각각 모두 동일해야 함.
*/
create table emp08
    (emp_id2 number not null,
    emp_name2 varchar2(100) not null,
    gender varchar2(10),
    age number,
    hire_date date,
    etc varchar2(300),
    constraint emp08_pk primary key (emp_id2));

insert into emp08 (emp_id2, emp_name2, gender, age, hire_date)
values(1, '선덕여왕', '여성', 23, to_date('2018-02-01', 'YYYY-MM-DD'));
insert into emp08 (emp_id2, emp_name2, gender, age, hire_date)
values(2, '허난설헌', '여성', 33, to_date('2018-02-01', 'YYYY-MM-DD'));
insert into emp08 (emp_id2, emp_name2, gender, age, hire_date)
values(3, '김만덕', '여성', 43, to_date('2018-02-01', 'YYYY-MM-DD'));
insert into emp08 (emp_id2, emp_name2, gender, age, hire_date)
values(4, '장희빈', '여성', 35, to_date('2018-02-01', 'YYYY-MM-DD'));
insert into emp08 (emp_id2, emp_name2, gender, age, hire_date)
values(5, '신사임당', '여성', 45, to_date('2018-02-01', 'YYYY-MM-DD'));
commit;
select * from emp08;

/*
UNION ALL
두 집합의 모든 원소를 가져오는 합집합 개념과 같음.

SELECT col1, col2, ...
FROM ...
WHERE ...
UNION ALL
SELECT col1, col2, ...
FROM ...
WHERE ...

일반 SELECT 문장과 다른 점은 두 문장 사이에 UNION ALL이라는 집합 연산자가 추가됐다는 점.
집합 연산자로 연결되는 SELECT 문장은 각각 사용하는 컬럼 수와 데이터형이 일치해야 하지만,
SELECT 절에 명시하는 컬럼의 이름은 달라도 상관 없음.
집합 연산자를 사용한 쿼리의 최종 조회 결과는 첫 번째 SELECT 문의 컬럼 명을 기준으로 조회.
집합 연산자를 사용할 때 데이터 정렬은 일반 SELECT 문과 동일하게 ORDER BY절을 사용.
문장 맨 끝에만 쓸 수 있음
*/
select emp_id, emp_name, gender, age
from emp03
union all
select emp_id2, emp_name2, gender, age
from emp08;

SELECT emp_id, emp_name, gender, age
from emp03
union all
select emp_id2, emp_name2, gender, age
from emp08
order by 4 desc;

/*
UNION 
한 가지만 제외하면 UNION ALL과 동일.
UNION의 경우 중복 데이터가 존재할 경우 그 데이터가 1건만 조회됨.
SELECT 절에서 값이 다른 컬럼(EMP_ID나 GENDER 컬럼)을 명시할 경우 UNION을 사용하더라도
중복 데이터로 인지하지 않고 모두 조회.
*/
select age
from emp03
union all
select age
from emp08
order by 1;

select age
from emp03
union
select age
from emp08
order by 1;

/*
INTERSECT
두 집합의 공통 원소만 추출하는 교집합 역할을 함.
두 개의 쿼리 결과를 검사해 공통된 요소에 해당하는 결과를 가져오는 것.
*/
SELECT age
from emp03
intersect
select age
from emp08
order by 1;

-- MINUS 한 집합을 기준으로 다른 집합에 없는 요소만 추출하는 차집합 역할.
select age
from emp03
minus
select age
from emp08
order by 1;
