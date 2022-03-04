-- 20220203 SQL 강의(MYSQL)
-- docker 사용
mysql -u root -p
SHOW databases;
USE mysql;
SHOW tables;

-- 데이터베이스 생성
CREATE database multi;
USE multi;
SET AUTOCOMMIT = 0;

-- Table 생성
-- AUTO_INCLEMENT 숫자 자동 증가 옵션
DROP TABLE IF EXISTS students;
CREATE TABLE students(
    id          integer,
    name        varchar(100),
    phone       char(13),
    address     varchar(1000)
)
;
DESC students;

INSERT INTO students
VALUES(1, 'hong-gd', '010-1111-1111', 'seoul')
;

ALTER TABLE students
ADD job     varchar(100)
;

INSERT INTO students(id, name, address, job)
VALUES(2, 'kim-sd', 'suwon', 'engineer')
;

INSERT INTO students
VALUES(3, 'aaa', NULL, 'namyangju', 'unemployed')
;

UPDATE students
SET
    phone = '010-2222-2222'
WHERE id = 2;

COMMIT;

DELETE FROM students
WHERE id = 3;

ROLLBACK;

ALTER TABLE students
MODIFY job      varchar(1000)
;

DROP TABLE students;

DROP DATABASE multi;

-- mysql 제공 employees 데이터 사용
-- docker에서 mysql 제공 데이터 사용하는 법(구글 따라해봄)
docker exec -it mysql bash
apt update
apt install git
git clone https://github.com/datacharmer/test_db.git
cd test_db
mysql -uroot -p
CREATE DATABASE employees;
USE employees;
source employees.sql

SELECT * FROM employees;

-- 조건절
SELECT * FROM salaries
WHERE salary >= 150000;

SELECT *
FROM salaries
WHERE salary > 100000
AND salary <= 150000
;

-- 1960년생
SELECT *
FROM employees
WHERE YEAR(birth_date) = 1960
;

-- 1960년생
SELECT *
FROM employees
WHERE EXTRACT(YEAR FROM birth_date) = 1960
;

-- 급여 오름차순
SELECT *
FROM salaries
ORDER BY salary
LIMIT 1000;

-- 급여 내림차순
SELECT *
FROM salaries
ORDER BY salary desc
LIMIT 100;

-- 취업시기 내림차순, 생일 오름차순
SELECT *
FROM employees
ORDER BY
    hire_date desc
    , birth_date
LIMIT 100;

-- GROUP BY
SELECT title
FROM titles
GROUP BY title;

SELECT
    title
    , COUNT(*) AS cnt
FROM titles
GROUP BY title;

-- GROUP BY 하지 않은 데이터는 출력 불가
SELECT 
    title
    , emp_no
FROM titles
GROUP BY title;

-- 집계함수 조건 사용 시, WHERE 대신 HAVING 사용
SELECT
    COUNT(*) AS cnt
FROM employees
WHERE gender = 'M';

SELECT
    dept_no
    , COUNT(dept_no) AS cnt
FROM dept_emp
GROUP BY dept_no;

SELECT
    dept_no
    , COUNT(dept_no) AS cnt
FROM dept_emp
GROUP BY dept_no
HAVING cnt >= 50000;

-- 권한
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost'
WITH GRANT OPTION;

-- root 권한 가진 user 만들기
-- % : 어디서든 접근 가능
CREATE user 'root'@'%'
identified by 'pw'
GRANT all prvileges on *.* to 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
COMMIT;

-- 현재 근무하고 있는 직원들의 전체 신상 명세
-- SELECT * FROM employees;
-- SELECT * FROM dept_emp;
SELECT
    emp.emp_no
    , emp.first_name
    , emp.gender
    , de.dept_no
    , de.to_date
FROM
    employees AS emp

    INNER JOIN
        dept_emp AS de
        -- 조건
        ON emp.emp_no = de.emp_no
LIMIT 100
;

SELECT
    emp.emp_no
    , emp.first_name
    , emp.gender
    , de.dept_no
    , de.to_date
FROM
    employees AS emp

    INNER JOIN
        dept_emp AS de
        ON emp.emp_no = de.emp_no
        WHERE de.to_date = '9999-01-01'
LIMIT 100
;

-- 현재 근무하고 있는 직원들의 이름과 부서 출력
SELECT
    e.emp_no
    , e.first_name
    , d.dept_no
FROM
    employees AS e
    INNER JOIN
        dept_emp AS d
        ON e.emp_no = d.emp_no
        WHERE d.to_date = '9999-01-01'
LIMIT 100
;

-- 전체 직원들의 이름과 직업 출력
SELECT
    e.first_name
    , t.title
FROM
    employees AS e
    INNER JOIN
        titles AS t
        ON e.emp_no = t.emp_no
LIMIT 100
;

SELECT
    e.first_name
    , t.title
FROM
    employees AS e
    -- INNER JOIN이 default
    JOIN
        titles AS t
        ON e.emp_no = t.emp_no
LIMIT 100
;

-- USING(같은 값으로 연결할 때)
SELECT
    *
FROM employees
    JOIN
        titles
        USING(emp_no)
LIMIT 100
;

-- NATURAL JOIN(연결 될 수 있는 컬럼이 하나일 때)
SELECT
    emp_no
    , e.first_name
    , t.title
FROM
    employees AS e
    NATURAL JOIN
        titles AS t
LIMIT 100
;

SELECT
    COUNT(*) AS cnt
FROM employees
    JOIN
        titles
        USING(emp_no)
;

-- 카테시안 곱
SELECT
    COUNT(*) AS cnt
FROM employees
    JOIN
        titles
;

-- CROSS JOIN(카톄시안 곱)
SELECT
    COUNT(*) AS cnt
FROM employees
    CROSS JOIN
        titles
;

-- 현재 근무하고 있는 (9999-01-01) 직원들의 이름과 월급 출력
SELECT
    e.first_name
    , e.last_name
    , s.salary
FROM employees AS e
    JOIN
        salaries AS s
        ON e.emp_no = s.emp_no
        WHERE s.to_date = '9999-01-01'
LIMIT 100
;

SELECT
    e.first_name
    , e.last_name
    , s.salary
FROM employees AS e
    NATURAL JOIN
        salaries AS s
        WHERE s.to_date = '9999-01-01'
LIMIT 100
;

SELECT
    e.first_name
    , e.last_name
    , s.salary
FROM employees AS e
    JOIN
        salaries AS s
        USING(emp_no)
        WHERE s.to_date = '9999-01-01'
LIMIT 100
;

-- 현재 부서 이름과 관리자 이름을 출력
SELECT
    d.dept_name
    , e.first_name

FROM departments AS d

    JOIN
        dept_manager AS dm
        ON d.dept_no = dm.dept_no
        
    JOIN
        employees AS e
        ON dm.emp_no = e.emp_no
        WHERE dm.to_date = '9999-01-01'
;

SELECT
    d.dept_name
    , e.first_name

FROM departments AS d

    JOIN
        dept_manager AS dm
        USING(dept_no)
        
    JOIN
        employees AS e
        USING(emp_no)
        WHERE dm.to_date = '9999-01-01'
;

SELECT
    d.dept_name
    , e.first_name

FROM departments AS d

    NATURAL JOIN
        dept_manager AS dm
        
    NATURAL JOIN
        employees AS e
        WHERE dm.to_date = '9999-01-01'
;

CREATE TABLE join_a(
    aa      INTEGER,
    ab      CHAR(3)
);

CREATE TABLE join_b(
    bb      INTEGER,
    ab      CHAR(3)
);

INSERT INTO join_a
INSERT INTO join_b
VALUES
    (1, 'aaa')
    , (2, 'bbb')
    , (3, 'ccc')
    , (7, 'ddd')
;

INSERT INTO join_b
VALUES
    (4, 'aaa')
    , (5, 'bbb')
    , (6, 'ccc')
    , (8, 'eee')
;

SELECT
    *
FROM
    join_a
    INNER JOIN
        join_b
        USING(ab)
;

-- LEFT JOIN
SELECT
    *
FROM
    join_a
    LEFT JOIN
        join_b
        USING(ab)
;

-- RIGHT JOIN
SELECT
    *
FROM
    join_a
    RIGHT JOIN
        join_b
        USING(ab)
;

-- 서브쿼리
-- last_name이 Haraldson인 사원의 월급 출력
SELECT
    salary
FROM salaries
WHERE emp_no IN
    (SELECT emp_no
    FROM employees
    WHERE last_name = 'Haraldson')
;