-- 2022/03/04 ORACLE 강의
--DROP TABLE DEPT;
--DROP TABLE EMP;
--DROP TABLE SALGRADE;
CREATE TABLE DEPT (
	DEPTNO NUMBER(2) CONSTRAINT PK_DEPT PRIMARY KEY, 
	DNAME VARCHAR2(14) , 
	LOC VARCHAR2(13) 
);
INSERT INTO DEPT VALUES (10,'ACCOUNTING','NEW YORK'); 
INSERT INTO DEPT VALUES (20,'RESEARCH','DALLAS'); 
INSERT INTO DEPT VALUES (30,'SALES','CHICAGO'); 
INSERT INTO DEPT VALUES (40,'OPERATIONS','BOSTON');
-- EMP 
CREATE TABLE EMP(    
	EMPNO NUMBER(4) CONSTRAINT PK_EMP PRIMARY KEY, 
	ENAME VARCHAR2(10), 
	JOB VARCHAR2(9), 
	MGR NUMBER(4), 
	HIREDATE DATE, 
	SAL NUMBER(7,2), 
	COMM NUMBER(7,2),
	DEPTNO NUMBER(2) CONSTRAINT FK_DEPTNO REFERENCES DEPT
);
INSERT INTO EMP VALUES (7369,'SMITH','CLERK',7902,to_date('17-12-1980','dd-mm-yyyy'),800,NULL,20); 
INSERT INTO EMP VALUES (7499,'ALLEN','SALESMAN',7698,to_date('20-2-1981','dd-mm-yyyy'),1600,300,30); 
INSERT INTO EMP VALUES (7521,'WARD','SALESMAN',7698,to_date('22-2-1981','dd-mm-yyyy'),1250,500,30);
INSERT INTO EMP VALUES (7566,'JONES','MANAGER',7839,to_date('2-4-1981','dd-mm-yyyy'),2975,NULL,20); 
INSERT INTO EMP VALUES (7654,'MARTIN','SALESMAN',7698,to_date('28-9-1981','dd-mm-yyyy'),1250,1400,30); 
INSERT INTO EMP VALUES (7698,'BLAKE','MANAGER',7839,to_date('1-5-1981','dd-mm-yyyy'),2850,NULL,30); 
INSERT INTO EMP VALUES (7782,'CLARK','MANAGER',7839,to_date('9-6-1981','dd-mm-yyyy'),2450,NULL,10); 
INSERT INTO EMP VALUES (7839,'KING','PRESIDENT',NULL,to_date('17-11-1981','dd-mm-yyyy'),5000,NULL,10); 
INSERT INTO EMP VALUES (7844,'TURNER','SALESMAN',7698,to_date('8-9-1981','dd-mm-yyyy'),1500,0,30); 
INSERT INTO EMP VALUES (7900,'JAMES','CLERK',7698,to_date('3-12-1981','dd-mm-yyyy'),950,NULL,30); 
INSERT INTO EMP VALUES (7902,'FORD','ANALYST',7566,to_date('3-12-1981','dd-mm-yyyy'),3000,NULL,20); 
INSERT INTO EMP VALUES (7934,'MILLER','CLERK',7782,to_date('23-1-1982','dd-mm-yyyy'),1300,NULL,10);
-- SALGRADE 
CREATE TABLE SALGRADE (    
	GRADE NUMBER, 
	LOSAL NUMBER, 
	HISAL NUMBER 
);
INSERT INTO SALGRADE VALUES (1,700,1200); 
INSERT INTO SALGRADE VALUES (2,1201,1400); 
INSERT INTO SALGRADE VALUES (3,1401,2000); 
INSERT INTO SALGRADE VALUES (4,2001,3000); 
INSERT INTO SALGRADE VALUES (5,3001,9999);

-- select
SELECT * FROM DEPT;
SELECT * FROM EMP; 
SELECT * FROM SALGRADE;

CREATE OR REPLACE VIEW V_EMP AS SELECT * FROM emp;
SELECT * FROM v_emp;

-- 자동으로 값+ 해주고 싶을 때 SEQUENCE 사용
CREATE SEQUENCE seq_test;

-- dual : 임시 테이블
SELECT seq_test.nextval FROM dual;

-- 테이블 복제
CREATE TABLE myemp AS SELECT * FROM EMP;
SELECT * FROM myemp;
DROP TABLE myemp;

-- 원하는 컬럼 복제
CREATE TABLE emps AS SELECT ENAME, EMPNO FROM EMP;
SELECT * FROM EMPS;
DROP TABLE EMPS;

-- 구조(컬컴)만 복제
-- WHERE 절을 거짓으로 하면 구조만 가져옴
CREATE TABLE TEST AS SELECT * FROM EMP WHERE 1 = 2;
SELECT * FROM TEST;
DROP TABLE TEST;

CREATE TABLE TABLE_NOTNULL01(
    ID      CHAR(3) NOT NULL,
    NAME    VARCHAR2(20)
);

-- null값이라 오류
INSERT INTO TABLE_NOTNULL01 VALUES('', 'a');
-- 오류 x
INSERT INTO TABLE_NOTNULL01 VALUES(' ', 'a');

INSERT INTO TABLE_NOTNULL01 VALUES ('HI', 'HIHI');

CREATE TABLE TABLE_NOTNULL02(
    ID          CHAR(3),
    NAME        VARCHAR2(20),
    CONSTRAINT  TN02_ID_NN NOT NULL (ID)
    -- NOT NULL은 컬럼 정의할 때만 가능 -> 오류
)

-- UNIQUE
-- null은 값이 없는 것이므로 unique에 영향받지 않음
CREATE TABLE table_unique01(
	ID		CHAR(3) UNIQUE,
	NAME	VARCHAR2(20)
);

CREATE TABLE table_unique02(
	ID			CHAR(3),
	NAME		VARCHAR2(20),
	CONSTRAINT	TU02_ID_UNQ UNIQUE (ID)
);

INSERT INTO table_unique02 VALUES('100', 'oracle');
-- ORA-00001: unique constraint (SYSTEM.TU02_ID_UNQ) violated
-- 무결성 제약조건에 위배됨
INSERT INTO table_unique02 VALUES('100', 'oracle');

CREATE TABLE table_unique03(
	ID			CHAR(3),
	NAME		VARCHAR2(20),
	-- 묶여져 있는 값이 unique 하다.
	CONSTRAINT	TU03_ID_UNQ UNIQUE (ID, NAME)
);

INSERT INTO table_unique03 VALUES('100', 'oracle');

INSERT INTO table_unique03 VALUES('100', 'python');

CREATE TABLE table_unique04(
	ID			CHAR(4),
	NAME		VARCHAR2(20),
	CONSTRAINT	tu04_id_unq	UNIQUE(ID),
	CONSTRAINT	tu04_nm_unq UNIQUE(NAME)
);

INSERT INTO table_unique04 VALUES ('100', 'oracle');

-- 오류
INSERT INTO table_unique04 VALUES ('100', 'python');

-- 기본 키
CREATE TABLE table_pk01(
	ID		CHAR(3) PRIMARY KEY,
	NAME	VARCHAR2(20)
);

INSERT INTO table_pk01 VALUES('100', 'oracle');

INSERT INTO table_pk01 VALUES('200', 'python');

-- unique constraint (SYSTEM.SYS_C007006) violated
INSERT INTO table_pk01 VALUES('200', 'hadoop');


CREATE TABLE table_pk02(
	ID			CHAR(3),
	NAME		VARCHAR2(20),
	CONSTRAINT	TP02_ID_PK PRIMARY KEY (ID)
);

INSERT INTO table_pk02 VALUES('100', 'oracle');

INSERT INTO table_pk02 VALUES('200', 'python');

-- unique constraint (SYSTEM.TP02_ID_PK) violated
INSERT INTO table_pk02 VALUES('200', 'hadoop');

-- 슈퍼키(복합키)
CREATE TABLE table_pk03(
	ID			CHAR(3),
	NAME		VARCHAR(20),
	CONSTRAINT	TP03_ID_PK PRIMARY KEY (ID, NAME)
);

INSERT INTO table_pk03 VALUES('100', 'oracle');

INSERT INTO table_pk03 VALUES('100', 'python');

-- cannot insert NULL into ("SYSTEM"."TABLE_PK03"."ID")
INSERT INTO table_pk03(NAME) VALUES('hadoop');

-- foreign key
CREATE TABLE table_fk01(
	ID			CHAR(3),
	NAME		VARCHAR(20),
	PKID		CHAR(3) REFERENCES TABLE_PK01(ID)
);

-- integrity constraint (SYSTEM.SYS_C007014) violated - parent key not                                                        found 
-- table_pk01에 500이 없음
INSERT INTO table_fk01 VALUES('500', 'oracle', '500');

INSERT INTO table_fk01 VALUES('500', 'oracle', '100');


CREATE TABLE table_fk02(
	ID			CHAR(3),
	NAME		VARCHAR2(20),
	PKID		CHAR(3),
	CONSTRAINT	TF02_ID_FK FOREIGN KEY (ID) REFERENCES table_pk02(ID)
);

-- integrity constraint (SYSTEM.TF02_ID_FK) violated - parent key not                                                         found
-- foreign key가 id를 가리키고 있음
INSERT INTO table_fk02 VALUES('300', 'hadoop', '200');

CREATE TABLE table_check01(
	ID			CHAR(3),
	NAME		VARCHAR2(20),
	MARRIAGE	CHAR(1) CHECK(MARRIAGE IN ('Y', 'N'))
);

CREATE TABLE table_check02(
	ID			CHAR(3),
	NAME		VARCHAR2(20),
	MARRIAGE	CHAR(1),
	CONSTRAINT	TC02_MG_CK	CHECK(MARRIAGE IN ('Y', 'N'))
);

INSERT INTO table_check01 VALUES('100', 'oracle', 'Y');

-- check constraint (SYSTEM.SYS_C007016) violated
INSERT INTO table_check01 VALUES('200', 'python', 'n');

-- Quiz

-- SIZE가 10인 가변길이 문자형 컬럼 ID와 SIZE가 10인 고정길이 문자형 컬럼 PW를 가진 TEST 테이블을 생성하자
CREATE TABLE test(
	ID		VARCHAR2(10),
	PW		CHAR(10)
);

-- 사원테이블(EMP)의 모든 구조와 데이터를 복사하여 TEST01 테이블을 생성하자
CREATE TABLE test01
	AS SELECT * FROM emp;

-- 사원테이블에서 사원번호와 이름을 복사하여 TEST02 테이블을 생성하자
CREATE TABLE test02
	AS SELECT empno, ename FROM emp;

-- 사원테이블에서 사원번호의 컬럼명을 M1, 이름의 컬럼명을 M2로 변경 하면서 복사하여 TEST03 테이블을 생성하자
CREATE TABLE test03(
	M1,
	M2
) AS SELECT empno, ename FROM emp;

-- 사원테이블의 구조만 복사하여 TEST04 테이블을 생성하자
CREATE TABLE test04
	AS SELECT *
	FROM emp
	WHERE 1 = 2
;

-- 부서테이블(DEPT)의 구조만 복사하여 TEST05 테이블을 생성하자
CREATE TABLE test05
	AS SELECT *
	FROM dept
	WHERE 1 = 2
;

SELECT deptno FROM dept UNION SELECT deptno FROM emp;

SELECT deptno FROM dept UNION ALL SELECT deptno FROM emp;

SELECT deptno FROM dept INTERSECT SELECT deptno FROM emp;

SELECT deptno FROM dept MINUS SELECT deptno FROM emp;

-- 문자열 합체
SELECT empno || ename FROM emp;

-- AS : alias(별칭)
SELECT empno || ename AS test FROM emp;

-- 연산
SELECT sal + comm FROM emp;

-- 현재 날짜(시간)
-- 현재 위치에 따라 다름
SELECT SYSDATE FROM dual;

-- update
SELECT * FROM test01;
-- 이름이 WARD인 사원의 월급을 2000으로 바꾸자
UPDATE test01
SET sal = 2000
WHERE ename = 'WARD';
-- 이름이 WARD인 사원의 직업을 manager로 바꾸고 부서를 20으로 바꾸자.
UPDATE test01
SET
	JOB = 'MANAGER',
	DEPTNO = 20
WHERE ENAME = 'WARD';

-- Quiz
-- 사원테이블의 모든 데이터를 출력하자.
SELECT * FROM emp;

-- 사원테이블에서 사원의 이름(ENAME), 사원번호(EMPNO), 월급(SAL)을 출력하자.
SELECT
	ename,
	empno,
	sal
FROM emp
;

-- 사원테이블에서 사원의 이름과 연봉을 출력하자.
SELECT
	ename,
	sal * 12 + COALESCE(comm, 0)
FROM emp
;

-- 사원테이블에서 사원의 이름, 입사일(HIREDATE), 부서번호(DEPTNO)를 출력하자.
SELECT
	ename,
	hiredate,
	deptno
FROM emp
;

-- 사원테이블에서 사원의 이름과, 사원을 관리하고 있는 관리자번호(MGR)를 출력하자.
SELECT
	ename,
	MGR
FROM emp
;

-- 사원테이블에서 사원의 이름, 월급, 커미션(COMM)을 출력하자.
SELECT
	ename,
	sal,
	comm
FROM emp
;

-- 사원테이블의 모든 데이터를 “oo님이 oo에 입사를 하고 oo의 월급을 받습니다.” 형식의 컬럼 하나로 출력하자.
SELECT
	(ename || ' nim ' || hiredate || ' ipsa ' || sal || ' wolgeup') AS test
	FROM emp
;

-- 부서테이블(DEPT)의 구조를 출력하자
DESC DEPT;

-- 사원테이블에서 사원번호가 ‘7844’인 사원의 사원번호, 이름, 월급을 출력하자.
SELECT
	empno,
	ename,
	sal
FROM emp
WHERE empno='7844'
;

-- 사원테이블에서 ‘SMITH’의 사원번호, 이름, 월급을 출력하자.
SELECT
	empno,
	ename,
	sal
FROM emp
WHERE ename='SMITH'
;

-- 사원테이블에서 입사일이 1980년 12월 17일인 사원의 모든 데이터를 출력하자.
SELECT
	*
FROM emp
WHERE hiredate=TO_DATE('17-12-1980','dd-mm-yyyy')
;

-- 사원테이블에서 1980년 부터 1982년 사이에 입사한 사원의 이름과 입사일을 출력하자.
SELECT
	ename,
	hiredate
FROM emp
WHERE hiredate BETWEEN TO_DATE('01-01-1980', 'dd-mm-yyyy') AND TO_DATE('31-12-1982', 'dd-mm-yyyy')
;

-- 사원테이블에서 월급이 2000 이하인 사원의 이름과 월급을 출력하자.
SELECT
	ename,
	sal
FROM emp
WHERE sal <= 2000;

-- 사원테이블에서 월급이 1000 에서 2000 사이인 사원의 이름과 월급을 출력하자.
SELECT
	ename,
	sal
FROM emp
WHERE sal BETWEEN 1000 AND 2000
;

-- 사원번호가 7369 이거나, 7499 이거나, 7521인 사원들의 이름과 월급을 출력하자.
SELECT
	ename,
	sal
FROM emp
WHERE
	empno=7369
	OR empno=7499
	OR empno=7521
;
SELECT
	ename,
	sal
FROM emp
WHERE empno
	IN (7369, 7499, 7521)
;

-- 사원테이블에서 사원의 이름과 월급을 출력하되, 월급을 내림차순으로 정렬하자.
SELECT
	ename,
	sal
FROM emp
ORDER BY sal DESC
;

-- 사원테이블에서 직업별 평균 월급을 출력하되 컬럼 alias를 ‘평균’으로 하고, 평균 월급이 높은 순으로 정렬하자.
SELECT
	job,
	AVG(sal) AS job_avg
FROM emp
GROUP BY job
ORDER BY job_avg
;

-- 사원테이블에서 전체 사원의 평균 월급을 출력하자.
SELECT
	AVG(sal) AS all_avg
FROM emp
;

-- 사원테이블에서 부서번호가 10인 부서에 근무하고 있는 사원들의 부서번호와 평균 월급을 출력하자.
SELECT
	deptno,
	AVG(sal) AS avg_10
FROM emp
WHERE deptno=10
GROUP BY deptno
;

-- 사원테이블에서 직업별 평균 월급을 구하자.
SELECT
	job,
	AVG(sal) AS job_avg
FROM emp
GROUP BY job
;

-- 사원테이블에서 10번 부서의 최대 월급을 출력하자.
SELECT
	MAX(sal) AS max_sal_10
FROM emp
WHERE deptno=10
;

-- 사원테이블에서 부서 별 최대 월급을 출력하자.
SELECT
	deptno,
	MAX(sal) AS max_sal_dept
FROM emp
GROUP BY deptno
;

-- 사원테이블에서 직업별 총 월급을 구하고, 총 월급이 5000 이상인 직업만 출력하자.
SELECT
	job
FROM emp
HAVING SUM(sal) >= 5000
GROUP BY job
;

-- 사원테이블에서 부서별 총 월급을 출력하되, 30번 부서를 제외하고, 총 월급이 8000 이상인 부서만, 총 월급이 높은 순으로 정렬하자.
SELECT
	deptno,
	SUM(sal) AS sum_sal
FROM emp
HAVING
	deptno != 30
	AND
	SUM(sal) >= 8000
GROUP BY deptno
ORDER BY sum_sal DESC
;