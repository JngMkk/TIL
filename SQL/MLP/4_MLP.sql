-- 2022/03/08 ORACLE 강의
--사원의 FULL_NAME(FIRST_NAME + LAST_NAME) 과 이메일을 출력하자 
--(이메일@HR.COM 으로 출력하자) 
SELECT 
    first_name || ' ' || last_name AS fullname, 
    email || '@HR.COM' AS mail
FROM employees;

--06년 이후에 입사한 사원의 이름(FIRST_NAME) 과 사원번호 (EMPLOYEE_ID)를 출력하자
SELECT
    first_name,
    employee_id
FROM employees
WHERE hire_date >= TO_DATE('06', 'YY');

--사원의 이름(FIRST_NAME), 부서이름(DEPARTMENT_NAME), 부서가 있는 거리(STREET_ADDRESS), 부서가 있는 나라(COUNTRY_NAME) 를 출력하자
SELECT
    first_name,
    DEPARTMENT_NAME,
    STREET_ADDRESS,
    COUNTRY_NAME
FROM
    employees
    JOIN departments
    USING(department_id)
    JOIN locations
    USING(location_id)
    JOIN countries
    USING(country_id)
; 

--'부서번호가 90이고, 전화번호가 515로 시작하면서, 끝자리가 4567인 사원'이 관리하는 사원의 사번과 이름을 출력하자
SELECT
    employee_id,
    first_name
FROM
    employees
WHERE
    manager_id
    IN (SELECT
            employee_id
        FROM employees
        WHERE
            department_id = 90
            AND
            phone_number LIKE '515%4567'
        )   
;

--전화번호가 650.121.8009인 사원의 이름과, 사원이 속한 부서가 위치한 도시, 주소(STREET_ADDRESS + POSTAL_CODE) 를 출력하자
SELECT
    first_name,
    city,
    street_address || ' ' || postal_code AS addr
FROM
    employees
    JOIN departments
    USING(department_id)
    JOIN locations
    USING(location_id)
WHERE
    phone_number = '650.121.8009'
;

--Canada 에서 일하고 있는 사원의 이름과, 도시, 월급을 출력하자
SELECT
    first_name,
    city,
    salary
FROM
    employees
    JOIN departments
    USING(department_id)
    JOIN locations
    USING(location_id)
    JOIN countries
    USING(country_id)
WHERE country_name = 'Canada'
;

--이름이 Guy 인 사원과 같은 부서에서 일하면서, Guy와 직업(JOB_ID)이 다른 사원의 모든 것을 출력하자
WITH
guy_emp AS (
    SELECT
        department_id AS d,
        job_id AS j
    FROM
        employees
    WHERE
        first_name = 'Guy'
)

SELECT *
FROM employees
WHERE
    department_id IN (SELECT d
                      FROM guy_emp)
    AND
    job_id NOT IN (SELECT j
                   FROM guy_emp)
;

--직업이 06년 7월 24일에 변경된 사원의 이름과, 과거 직업, 현재 직업을 출력하자
WITH
emp AS (
    SELECT
        employee_id,
        job_id,
        job_title AS old_job
    FROM
        job_history
        JOIN jobs
        USING(job_id)
    WHERE
        end_date = '24/JUL/06'
)
SELECT
    es.first_name,
    e.old_job,
    j.job_title AS current_job
FROM
    emp e,
    employees es
    JOIN jobs j
    ON es.job_id = j.job_id
WHERE
    es.employee_id IN (SELECT employee_id FROM emp)
;

--관리자가 없는 부서의 이름과 부서번호를 출력하자
SELECT
    department_name,
    department_id
FROM
    departments
WHERE
    manager_id IS NULL
;


--IT 부서 관리자의 성(LAST_NAME)과, 월급을 출력하자 (JOIN 사용하지 않고)
SELECT
    last_name,
    salary
FROM
    employees
WHERE
    employee_id
    IN
    (SELECT manager_id
     FROM departments
     WHERE department_name = 'IT')
;

--관리자가 존재하는 부서의 장소 중 가장 많은 장소의 도시 이름을 출력하자 (ROWNUM 사용)
WITH
loc AS (
    SELECT
        location_id,
        COUNT(*) AS cnt
    FROM
        departments
    WHERE
        manager_id IS NOT NULL
    GROUP BY location_id
)
, ranking AS (
    SELECT 
        location_id,
        ROW_NUMBER() OVER(ORDER BY cnt DESC) AS rank
    FROM loc
)
SELECT city
FROM locations
WHERE location_id
    IN
    (SELECT location_id
     FROM ranking
     WHERE rank=1)
;

--18년도가 근속 10주년인 사원의 이름과 입사일을 출력하자 ?
SELECT
    first_name,
    hire_date
FROM employees
WHERE
    EXTRACT(YEAR FROM hire_date) = 2008
;

--사원 이름이 'S'로 시작하는 사원의 이름과 사원번호, 전화번호를 출력하자
SELECT
    first_name,
    employee_id,
    phone_number
FROM
    employees
WHERE
    first_name LIKE 'S%'
;

--입사년도가 04년 이후인 사원들중 Seattle 에서 근무중인 사원들의 월급 총 합을 출력하자
WITH
emp AS (
    SELECT
        employee_id,
        salary,
        city
    FROM
        employees
        JOIN departments
        USING(department_id)
        JOIN locations
        USING(location_id)
    WHERE
        EXTRACT(YEAR FROM hire_date) >= 2004
)
SELECT SUM(salary) AS sum
FROM emp
WHERE city = 'Seattle'
;

--전체 평균 월급보다 월급을 많이 받는 사원들 중 9월에 입사한 사원들의 이름과 월급을 출력하자
WITH
emp AS (
    SELECT
        first_name
    FROM
        employees
    WHERE
        salary > (SELECT AVG(salary) FROM employees)
)
SELECT first_name, salary
FROM employees
WHERE first_name IN (SELECT * FROM emp)
      AND
      EXTRACT(MONTH FROM hire_date) = 9
;


--LAST_NAME 의 세번째 글자가 c인 사원들의 풀네임을 출력하자
SELECT
    first_name || ' ' || last_name AS fullname
FROM
    employees
WHERE
    SUBSTR(last_name, 3, 1) = 'c'
;

--부서 번호가 없는 사원의 이름(FIRST_NAME)과 직업(JOB_ID) 입사날(HIRE_DATE)을 출력하자
SELECT
    first_name,
    job_id,
    hire_date
FROM
    employees
WHERE
    department_id IS NULL
;

--Kevin보다 월급을 많이 받고 Susan 보다 적게 받는 사원의 이름과 월급을 출력하자
SELECT
    first_name,
    salary
FROM
    employees
WHERE
    salary > ALL(SELECT salary FROM employees WHERE first_name = 'Kevin')
    AND
    salary < (SELECT salary FROM employees WHERE first_name = 'Susan')
;

--Asia에 속해있는 도시이름과 나라 이름을 출력하자
SELECT
    city,
    country_name
FROM
    locations
    JOIN countries
    USING(country_id)
    JOIN regions
    USING(region_id)
WHERE region_name = 'Asia'
;

--월급이 4000이상인 사원의 이름과 부서명, 월급을 출력하자
SELECT
    first_name,
    department_name,
    salary
FROM
    employees
    LEFT JOIN departments
    USING(department_id)
WHERE
    salary >= 4000
;

--부서의 평균월급이 전체 평균월급보다 높은 부서의 부서이름과 평균월급을 출력하자
WITH
dept AS (
    SELECT
        department_id,
        department_name,
        AVG(salary) AS avg
    FROM employees
        JOIN departments
        USING(department_id)
    GROUP BY department_id, department_name
)
, gt_avg AS (
    SELECT
        AVG(salary) AS total_avg
    FROM employees
)
SELECT
    department_name,
    avg
FROM dept, gt_avg g
WHERE avg > g.total_avg
ORDER BY 2 DESC
;

--월급을 가장 많이 받는 사원의 전화번호를 출력하자
WITH
max_sal AS (
    SELECT MAX(salary) AS max
    FROM employees
)
SELECT
    phone_number
FROM
    employees, max_sal m
WHERE
    salary = m.max
;

--Seattle 에 근무하는 사원중 이름이 'l' (엘)로 끝나는 사원의 이름과 직업을 출력하자
SELECT
    first_name,
    job_title
FROM
    employees e
    JOIN departments
    USING(department_id)
    JOIN locations
    USING(location_id)
    JOIN jobs j
    USING(job_id)
WHERE
    first_name LIKE '%l'
    AND
    city = 'Seattle'
;

--입사한 년도(hire_date) 별로 인원수를 출력하자
WITH
year_emp AS (
    SELECT
        employee_id,
        TO_CHAR(hire_date, 'YYYY') AS hireyr
    FROM
        employees
)
SELECT
    hireyr,
    COUNT(*) AS cnt
FROM
    year_emp
GROUP BY hireyr
ORDER BY 1
;

--Canada에서 일하는 직원의 수를 출력하자
SELECT
    COUNT(*) AS cnt
FROM
    employees
    JOIN departments
    USING(department_id)
    JOIN locations
    USING(location_id)
    JOIN countries
    USING(country_id)
WHERE
    country_name = 'Canada'
;

--입사 후 직업의 변경이 없는 사원의 사원 번호, 이름, 입사일, 월급, 부서 이름을 출력하자
SELECT
    employee_id,
    first_name,
    hire_date,
    salary,
    department_name
FROM
    employees e
    JOIN departments d
    ON e.department_id = d.department_id
WHERE
    employee_id
    NOT IN
    (SELECT employee_id
     FROM job_history)
;

--각 부서 별 커미션이 책정되지 않은 사원의 수를 출력하자
SELECT
    department_id,
    COUNT(employee_id) AS cnt
FROM
    employees
WHERE commission_pct IS NULL
GROUP BY department_id
ORDER BY 1
;

--핸드폰 번호가 011 로 시작하는 사원의 이름, 전화번호, 이메일을 출력하자
SELECT
    first_name,
    phone_number,
    email
FROM
    employees
WHERE
    phone_number LIKE '011%'
;

--이름이 Britney 인 사원과 같은 부서에서 일하면서, Britney와 직업(JOB_ID)도 같은 사원의 모든 것을 출력하라.
SELECT *
FROM employees
WHERE
    (department_id, job_id)
    IN
    (SELECT
        department_id,
        job_id
     FROM employees
     WHERE
        first_name = 'Britney')
;

--IT 부서의 관리자의 연봉(commission_pct 생각하기) 보다 더 많은 평균 월급?을 받는 부서의 부서번호와 부서이름을 출력하자
WITH
emp AS (
    SELECT
        employee_id,
        salary * 12 + (salary * 12 * NVL(commission_pct, 0)) AS sal,
        department_id
    FROM employees
)
, dept AS (
    SELECT
        department_id,
        department_name,
        AVG(sal) AS avg_sal
    FROM emp
        JOIN departments
        USING(department_id)
    GROUP BY department_id, department_name
)
, IT_sal AS (
    SELECT
        sal 
    FROM
        emp
        JOIN departments
        USING(department_id)
    WHERE
        employee_id
        IN (SELECT manager_id
            FROM departments
            WHERE department_name='IT')
)
SELECT
    department_id,
    department_name
FROM dept, IT_sal i
WHERE
    avg_sal > i.sal
ORDER BY 1
;