-- 2022/03/07 ORACLE 강의
-- LPAD, RPAD(컬럼, 길이, 값)
-- 해당 컬럼을 길이만큼 오른쪽, 왼쪽 정렬함
-- 정렬 후 빈 공간은 값으로 채움
SELECT
    LPAD(ename, 7, '*') AS LPAD,
    RPAD(ename, 7, '*') AS RPAD
FROM emp;
--  LPAD			  RPAD
-- --------        ----------
-- **SMITH 		     SMITH**
-- **ALLEN 		     ALLEN**
-- ***WARD 		     WARD***
-- **JONES 		     JONES**
-- *MARTIN 		     MARTIN*
-- **BLAKE 		     BLAKE**
-- **CLARK 		     CLARK**
-- ***KING 		     KING***
-- *TURNER 		     TURNER*
-- **JAMES 		     JAMES**
-- ***FORD 		     FORD***
-- *MILLER 		     MILLER*


-- LTRIM, RTRIM(문자열, 제거할 문자(열))
-- 문자열에서 제거할 문자(열) 제거
SELECT LTRIM('xyxzyyTech6 327', 'xyz') AS LTRIM FROM dual;
SELECT RTRIM('xyxzyyTech6 327', '0123456789') AS RTRIM FROM dual;
SELECT RTRIM('xyxzyyTech6 327', '0123456789 ') AS RTRIM FROM dual;

-- TRIM(제거할 문자(하나) FROM 문자열)
-- 문자열 양쪽에서 제거할 문자 제거
SELECT TRIM('x' FROM 'xyxzyyTech6 327') AS TRIM FROM dual;

-- SUBSTR(컬럼 or 문자열, 시작위치 [, 반환할 갯수])
SELECT
    SUBSTR(ename, 2, 1) AS c1,
    SUBSTR(ename, -2) AS c2
FROM emp;

-- INSTR(컬럼 or 문자열, 찾는 문자(열) [, 시작위치 [, 횟수]])
-- 찾는 문자(열)이 [시작위치부터 [횟수만큼]] 나타난 시작위치 반환
SELECT
    ename,
    INSTR(ename, 'S', 1, 1) AS INSTR
FROM emp;

SELECT
    ename,
    INSTR(ename, 'L', -1, 2) AS INSTR
FROM emp;

SELECT INSTR('abcccva', 'a', -1, 2) AS INSTR FROM dual;

-- LENGTH, LENGTHB
-- 주어진 컬럼의 문자 길이를 반환
-- 컬럼 타입이 CHAR인 경우, 데이터와 상관 없이 컬럼의 전체 길이 반환

-- ROUND, TRUNC(컬럼 or 숫자 [, 소수점 자리지정])
-- 지정한 자리에서 반올림 / 버림
-- 자리 지정은 반드시 정수 (생략하면 0)
SELECT 
    ROUND(123.456),
    ROUND(123.456, 1),
    TRUNC(123.456, 1),
    TRUNC(123.456, -1)
FROM dual;

-- CEIL, FLOOR()
-- 올림, 버림
SELECT
    CEIL(sal / 1000),
    FLOOR(sal / 1000),
    sal
FROM emp;

-- ADD_MONTHS(날짜, 더하려는 개월)
-- 지정한 날짜부터 개월 수를 더한 날짜 반환
SELECT
    ename,
    hiredate,
    ADD_MONTHS(hiredate, 240)
FROM emp;

-- MONTHS_BETWEEN(날짜 1, 날짜 2)
-- 지정한 두 날짜의 개월 수 반환
SELECT
    ename,
    job,
    hiredate,
    TRUNC(MONTHS_BETWEEN(TO_DATE('2000/01/01', 'yyyy-mm-dd'), hiredate) / 12) AS t
FROM emp
WHERE MONTHS_BETWEEN(TO_DATE('2000/01/01', 'yyyy-mm-dd'), hiredate) > 120;

-- TO_CHAR(입력 타입 [, 형식])
SELECT
    TO_CHAR(1234, '99999') AS c1,
    TO_CHAR(1234, '00000') AS c2,
    TO_CHAR(1234, 'L9999') AS c3,
    TO_CHAR(1234, '9,999') AS c4
FROM dual;

SELECT
    TO_CHAR(sysdate, 'HH24:MI:SS') AS c1,
    TO_CHAR(sysdate, 'MON DY, YYYY') AS c2,
    TO_CHAR(sysdate, 'YYYY-FMMM-DD DAY') AS c3,
    TO_CHAR(sysdate, 'YYYY-MM-DD') AS c4,
    TO_CHAR(sysdate, 'YEAR, Q') AS c5
FROM dual;

-- TO_DATE(입력 타입 [, 형식])
SELECT TO_DATE('20100101', 'YYYYMMDD') AS d FROM dual;
SELECT TO_CHAR(TO_DATE('20100101', 'YYYYMMDD'), 'YYYY, MON') AS d FROM dual;
SELECT TO_CHAR(TO_DATE('210830 143001', 'YYMMDD HH24MISS'), 'YY-MM-DD PM FMHH:MI:SS') AS d FROM dual;

-- TO_NUMBER(입력 타입 [, 형식])
SELECT
    ename,
    TO_NUMBER(SUBSTR(TO_CHAR(hiredate, 'YYYY-MM-DD'), 1, 4)) AS year,
    TO_NUMBER(SUBSTR(TO_CHAR(hiredate, 'YYYY-MM-DD'), 6, 2)) AS mon
FROM emp;

-- DECODE(컬럼 OR 문자열, 비교 값, 같을 때 반환 값 [, 비교값, 같을 때 반환 값, ...] [, 다를 때 기본 값])
SELECT
    ename,
    job,
    DECODE(job, 'MANAGER', 1, 'SALESMAN', 2, 0) AS d
FROM emp;
-- ENAME	   JOB		      D
-- ---------- --------- ----------
-- SMITH	   CLERK	      0
-- ALLEN	   SALESMAN	      2
-- WARD	       SALESMAN	      2
-- JONES	   MANAGER	      1
-- MARTIN	   SALESMAN	      2
-- BLAKE	   MANAGER	      1
-- CLARK	   MANAGER	      1
-- KING	       PRESIDENT	  0
-- TURNER	   SALESMAN	      2
-- JAMES	   CLERK	      0
-- FORD	       ANALYST	      0
-- MILLER	   CLERK	      0


-- CASE WHEN 조건 ... THEN 참일 때 반환 값 END
-- CASE WHEN 조건 ... THEN 참일 때 반환 값 ELSE 거짓일 때 반환 값 END
SELECT
    ename,
    sal,
    CASE
        WHEN sal <= 1000 THEN 'chogeup'
        WHEN sal <= 2000 THEN 'joonggeup'
        ELSE 'gogeup'
        END
FROM emp;

-- 집계함수 : COUNT, MAX, MIN, SUM, AVG, ...
-- 연산에서 NULL은 제외
-- 집계함수 조건문 사용 시 -> HAVING
SELECT
    COUNT(comm),
    COUNT(NVL(comm, 0))
FROM emp;

-- 그룹함수 : ROLLUP, CUBE, GROUPING SETS
-- ROLLUP : 순서에 맞게 중간 집계 추가
-- A B 집계
-- UNION ALL
-- A 집계
-- UNION ALL
-- 전체 집계
SELECT
    job,
    deptno,
    AVG(sal)
FROM emp
GROUP BY ROLLUP(job, deptno)
;

-- CUBE : 모든 중간 집계 추가
-- 전체 집계
-- UNION ALL
-- B 집계
-- UNION ALL
-- A 집계
-- UNION ALL
-- A B 집계
SELECT
    JOB, DEPTNO, AVG(SAL)
FROM EMP
GROUP BY CUBE(JOB, DEPTNO);


-- GROUPING SETS : 그룹함수의 결과에 원하는 결과를 추가
-- A B 집계
-- UNION ALL
-- A 집계
-- UNION ALL
-- 전체 집계
-- B 집계
SELECT
    JOB, DEPTNO, AVG(SAL)
FROM EMP
GROUP BY GROUPING SETS(ROLLUP(JOB, DEPTNO), DEPTNO);

-- ROWID, ROWNUM
-- 식별자로 사용 ( 수정 불가 )
CREATE TABLE ROWTEST(NO NUMBER);
INSERT INTO ROWTEST VALUES(111);
INSERT INTO ROWTEST VALUES(222);
INSERT INTO ROWTEST VALUES(333);

SELECT
    -- 내부 식별자
    ROWID,
    -- 행 번호
    ROWNUM,
    NO
FROM ROWTEST;
-- ROWID		       ROWNUM	      NO
-- ------------------ ---------- ----------
-- AAAE5kAABAAALCZAAA	    1	     111
-- AAAE5kAABAAALCZAAB	    2	     222
-- AAAE5kAABAAALCZAAC	    3	     333

SELECT
    ename,
    sal,
    ROWNUM
FROM emp
ORDER BY sal DESC;
-- ENAME		  SAL	  ROWNUM
-- ---------- ---------- ----------
-- KING		     5000	       8
-- FORD		     3000	      11
-- JONES		 2975	       4
-- BLAKE		 2850	       6
-- CLARK		 2450	       7
-- ALLEN		 1600	       2
-- TURNER		 1500	       9
-- MILLER		 1300	      12
-- MARTIN		 1250	       5
-- WARD		     1250	       3
-- JAMES		  950	      10
-- SMITH		  800	       1

SELECT
    ename,
    sal,
    ROWNUM
FROM
    ( SELECT ename, sal
        FROM emp
        ORDER BY sal DESC )
;
/*

ENAME		  SAL	  ROWNUM
---------- ---------- ----------
KING		 5000	       1
FORD		 3000	       2
JONES		 2975	       3
BLAKE		 2850	       4
CLARK		 2450	       5
ALLEN		 1600	       6
TURNER		 1500	       7
MILLER		 1300	       8
MARTIN		 1250	       9
WARD		 1250	      10
JAMES		  950	      11
SMITH		  800	      12

ROWNUM은 oracle 내부에서 정하는 개수를 말함.
so, WHERE ROWNUM = 3 하면 3개를 가져와야 하는데 하나만 지정하였으므로 못가져옴.

*/

SELECT
    ename,
    sal,
    rn
FROM( SELECT ename, sal, ROWNUM AS rn
        FROM (SELECT ename, sal FROM emp ORDER BY sal DESC))
WHERE rn >= 3 AND rn <= 5
;

-- 순위함수 RANK, DENSE_RANK, ROW_NUMBER
SELECT
    ename,
    sal,
    RANK()          OVER(ORDER BY sal DESC) AS rank,
    DENSE_RANK()    OVER(ORDER BY sal DESC) AS dense,
    ROW_NUMBER()    OVER(ORDER BY sal DESC) AS rn
FROM emp;
/*

ENAME		  SAL	    RANK      DENSE	    RN
---------- ---------- ---------- ---------- ----------
KING		 5000	       1	  1	     1
FORD		 3000	       2	  2	     2
JONES		 2975	       3	  3	     3
BLAKE		 2850	       4	  4	     4
CLARK		 2450	       5	  5	     5
ALLEN		 1600	       6	  6	     6
TURNER		 1500	       7	  7	     7
MILLER		 1300	       8	  8	     8
MARTIN		 1250	       9	  9	     9
WARD		 1250	       9	  9	    10
JAMES		  950	      11	 10	    11
SMITH		  800	      12	 11	    12

*/

-- 사원테이블에서 사원의 이름을 첫글자는 대문자로, 나머지는 소문자로 출력하자.
SELECT
    INITCAP(ename) AS name
FROM emp;

-- 사원테이블에서 사원의 이름을 출력하고, 이름의 두번째 글자부터 네번째 글자까지만 출력하자.
SELECT
    ename,
    SUBSTR(ename, 2, 3) AS substr
FROM emp;

-- 사원테이블에서 사원 이름과 근무일수(고용일 ~ 현재 날짜)를 출력하자. (한달을 30일로 계산)
SELECT
    ename,
    FLOOR(MONTHS_BETWEEN(SYSDATE, hiredate) * 30) AS t1,
    FLOOR(SYSDATE - hiredate) AS t2
FROM emp;

-- 사원테이블에서 각 사원 이름의 철자 개수를 출력하자.
SELECT
    ename,
    LENGTH(ename)
FROM emp;

-- 사원테이블에서 사원의 이름이 M으로 시작하는 사원들의 이름을 출력하자.
SELECT
    ename
FROM emp
WHERE ename LIKE 'M%'
;

-- 서브쿼리

-- SINGLE ROW SUBQUERY
-- JONES 보다 더 많은 월급을 받는 사원의 이름과 월급을 출력하자
SELECT
    ename,
    sal
FROM emp
WHERE sal >
    (
    SELECT sal
    FROM emp
    WHERE ename = 'JONES'
    )
;

-- MULTI ROW SUBQUERY
-- 부하직원이 없는 사원의 사원번호와 이름을 출력하자
SELECT
    empno,
    ename
FROM emp
WHERE
    empno
    NOT IN
    (
    SELECT
        NVL(mgr, 0)
    FROM emp
    )
;

-- MULTI COLUMN SUBQUERY
SELECT
    ename,
    sal,
    deptno
FROM emp
WHERE
    (deptno, sal)
    IN
    (
    SELECT
        deptno,
        sal
    FROM emp
    WHERE job = 'SALESMAN'
    )
;

-- INLINE VIEW
-- 결과가 가상테이블로 사용
SELECT
    e.ename,
    e.sal,
    mydept.deptno,
    myavg
FROM
    emp e,
    (
    SELECT
        deptno,
        AVG(sal) AS myavg
    FROM emp
    GROUP BY deptno
    ) mydept
WHERE
    e.deptno = mydept.deptno
    AND
    e.sal > mydept.myavg
;

-- ‘CHICAGO’에서 근무하는 사원들과 같은 부서에서 근무하는 사원의 이름과 월급을 출력하자.
SELECT
    ename,
    deptno,
    sal
FROM emp
WHERE deptno IN (SELECT deptno
                 FROM dept
                 WHERE loc = 'CHICAGO')
;

-- 관리자의 이름이 ‘KING’인 사원의 이름과 월급을 출력하자.
SELECT
    ename,
    sal
FROM emp
WHERE mgr IN (SELECT empno
              FROM emp
              WHERE ename = 'KING')
;

-- 전체 사원 중, 20번 부서의 사원 중 가장 많은 월급을 받는 사원보다 더 많은 월급을 받는 사원들의 이름과 월급을 출력하자.
SELECT
    ename,
    sal
FROM emp
WHERE sal > (SELECT MAX(sal)
             FROM emp
             WHERE deptno = 20)
;

-- 전체 사원 중, 직업이 ‘SALESMAN’인 사원 중 가장 많은 월급을 받는 사원보다 더 많은 월급을 받는 사원들의 이름과 월급을 출력하되,
-- MAX()함수를 사용하지 말자. (ANY, ALL 연산자)
SELECT
    ename,
    sal
FROM emp
WHERE
    sal > ALL(SELECT sal
              FROM emp
              WHERE job = 'SALESMAN')
;

-- ‘BLAKE’가 근무하는 부서의 위치(LOC)를 출력하자.
SELECT loc
FROM dept
WHERE deptno IN (SELECT deptno
                 FROM emp
                 WHERE ename = 'BLAKE')
;

-- 이름에 ’S’가 들어가는 사원과 동일한 부서에서 근무하는 사원 중, 자신의 월급이 전체 사원의 평균 월급보다 많은 사원들의
-- 사원번호, 이름, 월급을 출력하자.
SELECT
    e.deptno,
    e.ename,
    e.sal,
    avg_sal
FROM emp e,
     (SELECT AVG(sal) AS avg_sal
      FROM emp)
WHERE
    deptno
    IN (SELECT deptno
        FROM emp
        WHERE ename LIKE '%S%')
    AND
        e.sal > avg_sal
;

-- 사원번호가 7369인 사원과 같은 직업이고, 사원번호가 7876인 사원보다 많이 받는 사원의 이름과 직업을 출력하자.
SELECT
    ename,
    job
FROM emp
WHERE
    job IN (SELECT job
            FROM emp
            WHERE empno = 7369)
        AND sal > 
            (SELECT sal
             FROM emp
             WHERE empno = 7876)
;

-- JOIN
-- 테이블과 테이블을 연결
-- JOIN할 두 테이블에 일치하는 값이 있는 컬럼이 없을 때
SELECT
    ename,
    sal,
    grade
FROM
    emp e
  JOIN
    salgrade sg
  ON
    (sal BETWEEN losal AND hisal)
;

-- SELF JOIN
SELECT
    e.ename,
    e.empno,
    mgr.ename,
    mgr.empno
FROM
    emp e,
    emp mgr
WHERE
    e.mgr = mgr.empno
;

SELECT
    e.ename,
    e.empno,
    mgr.ename,
    mgr.empno
FROM
    emp e
  LEFT OUTER JOIN
    emp mgr
  ON
    e.mgr = mgr.empno
;

-- 사원들의 이름, 부서번호, 부서이름을 출력하자.
SELECT
    ename,
    e.deptno,
    dname
FROM
    emp e
    JOIN dept d
    ON e.deptno = d.deptno
ORDER BY 2
; 

SELECT
    ename,
    deptno,
    dname
FROM emp
    JOIN dept
    USING(deptno)
;

-- ‘DALLAS’에서 근무하는 사원의 이름, 직업, 부서번호, 부서이름을 출력하자.
SELECT
    ename,
    job,
    e.deptno,
    dname
FROM emp e
    JOIN dept d
    ON e.deptno = d.deptno
    WHERE d.loc = 'DALLAS'
;

-- 이름에 ‘A’가 들어가는 사원들의 이름과 부서이름을 출력하자.
SELECT
    ename,
    dname
FROM emp e
    JOIN dept d
    ON e.deptno = d.deptno
    WHERE e.ename LIKE '%A%'
;

-- 사원의 이름과 부서이름, 월급을 출력하되, 월급이 3000 이상인 사원들만 출력하자.
SELECT
    e.ename,
    d.dname,
    e.sal
FROM emp e
    JOIN dept d
    ON e.deptno = d.deptno
    WHERE e.sal >= 3000
ORDER BY 3 DESC
;

-- 사원테이블과 급여테이블(SALGRADE)에서 커미션이 책정된 사원들의 사원번호, 이름, 연봉, 연봉+커미션, 급여등급(SALGRADE)을 출력하자.
SELECT
    empno,
    ename,
    sal * 12 AS sal, 
    sal * 12 + comm AS sal_comm,
    grade
FROM emp
    JOIN salgrade
    ON sal BETWEEN losal AND hisal
WHERE comm IS NOT NULL
ORDER BY 4 DESC
;

-- 부서번호가 10번인 사원들의 부서번호, 부서이름, 사원이름, 월급, 급여등급을 출력하자.
SELECT
    e.deptno,
    dname,
    ename,
    sal,
    grade
FROM emp e
    JOIN salgrade
    ON sal BETWEEN losal AND hisal
    JOIN dept d
    ON e.deptno = d.deptno
    WHERE e.deptno = 10
ORDER BY 4 DESC
;

-- 부서번호가 10번이거나 20번인 사원들의 부서번호, 부서이름, 사원이름, 급여등급을 출력하되,
-- 부서번호가 낮은 순으로, 월급이 높은 순으로 출력하자.
SELECT
    e.deptno,
    dname,
    ename,
    grade
FROM emp e
    JOIN salgrade
    ON sal BETWEEN losal AND hisal
    JOIN dept d
    ON e.deptno = d.deptno
    WHERE e.deptno IN (10, 20)
ORDER BY 1, 4 DESC
;

-- 사원번호와 이름, 관라자의 사원번호와 관리자이름을 출력하자.
SELECT
    e.ename,
    e.empno,
    mgr.ename AS mgr_name,
    mgr.empno AS mgr_empno
FROM
    emp e
    JOIN emp mgr
    ON e.mgr = mgr.empno
;

-- 부서이름, 위치, 각 부서의 사원수, 평균 월급을 출력하자.
SELECT
    dname,
    loc,
    COUNT(ename) AS cnt,
    NVL(AVG(sal), 0) AS avg
FROM emp e
    RIGHT JOIN dept d
    ON e.deptno = d.deptno
GROUP BY dname, loc
;