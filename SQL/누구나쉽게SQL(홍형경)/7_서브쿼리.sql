/*
지금까지 봐온 쿼리는 단 하나의 SELECT 문장으로 이루어져 있었는데, 이를 주 쿼리 혹은
메인쿼리라고 한다. 서브쿼리는 메인쿼리 안에 있는 또 다른 SELECT 문장을 말한다.
따라서 서브쿼리를 구성하는 SELECT 문장은 항상 괄호로 둘러싸여있음.
서브쿼리는 SELECT 절에 사용되어 특정 값을 반환할 수 있고, FROM 절에 사용되어 마치
테이블처럼 사용할 수도 있음. 또, WHERE 절에서 조건 값을 비교하는 데도 사용됨.
*/

/*
스칼라 서브쿼리
메인 쿼리의 SELECT 절에서 마치 컬럼이나 표현식처럼 사용.
스칼라 서브쿼리 내의 SELECT 절에서는 단 하나의 컬럼이나 표현식만 사용할 수 있음.
물론 컬럼이나 표현식들을 +나 ||연산자로 연결해 최종 반환값이 한 개라면
여러 개를 사용할 수도 있음. 또한, 서브쿼리 하나가 하나의 컬럼이나 표현식 역할을 하므로
두 개 이상의 값, 즉 반환하는 컬럼 수가 2 이상이면 안됨. 또한 반환되는 로우 수도
반드시 1개여야 함.
*/

SELeCT a.emp_id, a.emp_name, a.gender, a.age, a.dept_id,
        (SELECT b.dept_name from dept_master b where a.dept_id = b.dept_id)
        dept_name
from emp_master a;

select a.emp_id, a.emp_name, a.gender, a.age, a.dept_id, b.dept_name
from emp_master a, dept_master b
where a.dept_id = b.dept_id(+);

/*
인라인 뷰
메인 쿼리의 from 절에서 사용하는 서브쿼리를 말함.
즉, from 절에서 서브쿼리 자체가 하나의 테이블처럼 사용되는 것.
따라서 인라인 뷰는 스칼라 서브쿼리와는 다르게 여러 개의 컬럼이나 표현식, 여러 개의 로우를
반환할 수 있음.
*/
select a.dept_id, a.dept_name, k.emp_id, k.emp_name, k.address
from dept_master a,
(select b.emp_id, b.emp_name, c.city || c.gu || c.address_name AS address, b.dept_id
from emp_master b, address_master c
where b.address_id = c.address_id) k
where a.use_yn = 'Y' and a.dept_id = k.dept_id
order by 1, 3;

/*
중첩 서브쿼리
where 절에서 사용하는 서브쿼리.
where 절에서 사용한다는 것은 조건절의 일부로 사용된다는 뜻.
메인쿼리 테이블의 특정 컬럼 값과 비교한 값을 반환하는 용도로 사용.
중첩 서브쿼리는 인라인 뷰처럼 여러 개의 컬럼, 여러 개의 로우를 반환할 수 있음.
*/
-- 단일 행 반환
select * from dept_master a
where a.dept_id = (select b.dept_id from emp_master b where b.emp_name = '세종대왕');

-- 다중 행 반환
select * from dept_master a
where a.dept_id in
(select b.dept_id from emp_master b where b.age between 40 and 49);

-- 다중 컬럼, 다중 행 반환
select * from emp_master a
where (a.gender, a.age) in
(select b.gender, b.age from emp_master b, address_master c
where b.address_id = c.address_id and c.gu in ('중구', '서대문구'));

/*
세미 조인
이전 절에서 알아본 중첩 서브쿼리에서 사용한 조인 방법.
메인쿼리에서 사용된 테이블과 서브쿼리 결과를 조인하는 것.
*/
-- exists 연산자를 사용한 세미 조인
select * from dept_master a
where exists(select 1 from emp_master b where b.age between 40 and 49 and a.dept_id = b.dept_id);

-- 안티 조인은 세미 조인과 형식은 같은데 not 연산자가 들어간다는 점이 다름.
-- not 연산자를 사용한 안티 조인
select * from dept_master a
where a.dept_id not in (Select b.dept_id from emp_master b where b.age between 40 and 49);

-- not exists를 사용한 안티 조인
select * from dept_master a
where not exists (select 1 from emp_master b where b.age between 40 and 49 and a.dept_id = b.dept_id);