-- || 두 문자 결합
select 'A' || 'B' from dual;

-- 숫자형 함수
select ABS(-1) from dual;

-- ceil(n) n과 같거나 큰 최소 정수 반환
select ceil(10.6) from dual;

-- exp(n) e의 n승을 반환
select exp(10) from dual;

-- floor(n) n과 같거나 작은 최대 정수 반환
select floor(10.6) from dual;

-- ln(n) n의 자연로그 값을 반환, n은 0보다 커야 함
select ln(10) from dual;

-- log(n2, n1) n2는 밑, n1은 진수. n1 > 0, n2는 0과 1이 아닌 양수
select log(10, 100) from dual;

-- mod(n2, n1) n2를 n1로 나눈 나머지 반환
select mod(11, 4) from dual;

-- power(n2, n1) n2의 n1승을 반환
select power(3, 2) from dual;

-- round(n, i) n의 소수점 기준 (i+1)번째에서 반올림한 값을 반환, 
-- 정수로 만들 시 i는 0
select round(10.5453, 2) from dual;

-- sign(n) n의 부호 반환, n이 양수이면 1 음수이면 -1 0이면 0 반환
select sign(-3) from dual;

select sqrt(3) from dual;
-- trunc(n1, n2) n1의 소수점 기준 n2 자리에서 절삭, n2 생략 시 0
select trunc(10.5454, 2) from dual;

select round(565.545, -1) first,
    round(565.545, -2) second,
    round(565.545, -3) third
    from dual;

-- 문자형 함수
-- chr(n) n은 숫자로 n 값에 해당되는 문자를 반환
select chr(65) || chr(66) || chr(67) from dual;

-- concat(char1, char2) char1과 char2 문자를 결합한 결과를 반환, ||연산자와 같은 기능
select concat('A', 'B') from dual;

-- initcap(char) char의 첫 번째 문자를 대문자로 변환
select initcap('the') from dual;

-- lower(char) char을 소문자로 변환
select lower('THE') from dual;

-- upper(char) char을 대문자로 변환
select upper('the') from dual;

-- lpad(expr1, n, expr2) expr1을 반환하는데, 
-- expr2를 (n - expr1 길이)만큼 왼쪽을 채워 반환
select lpad('THE', 5, '*') from dual;

-- rpad(expr1, n, expr2) expr1을 반환하는데, 
-- expr2를 (n - expr1 길이)만큼 오른쪽을 채워 반환
select rpad('THE', 5, '*') from dual;

-- ltrim(expr1, expr2) expr1의 왼쪽에서 expr2를 제거한 결과를 반환
select ltrim('**THE**', '*') from dual;

-- rtrim(expr1, expr2) expr1의 오른쪽에서 expr2를 제거한 결과를 반환
select rtrim('**THE**', '*') from dual;

/*
substr(char, n1, n2)
- char에서 n1 위치에서 시작해 n2 길이만큼을 잘라낸 결과를 반환
- n1을 0으로 명시하면 1이 적용
- n1이 음수이면 char 오른쪽 끝에서부터 거꾸로 세어 가져옴
- n2를 생략하면 n1부터 끝까지 반환
- n2 값을 1 미만으로 지정하면 NULL값을 반환
*/
select substr('ABCDEFG', 3, 2) from dual;
select substr('ABCDEFG', -3) from dual;

select substr('ABCDEFG', 1, 3) first,
    substr('ABCDEFG', 0, 3) second,
    substr('ABCDEFG', 1) third,
    substr('ABCDEFG', -2) fourth,
    substr('ABCDEFG', -2, 1) fifth,
    substr('ABCDEFG', 2, -1) sixth
    from dual;

-- trim(char) char의 양쪽 끝 공백을 제거한 결과를 반환
select trim('  ABCD EFG  ') from dual;

-- ascii(char) char 문자의 ASCII 코드 값을 반환, CHR 함수와 반대 기능
select ascii('A') from dual;

/*
instr(char1, char2, n1, n2)
- char1에서 char2 문자를 찾아 그 시작 위치를 반환함
- n1은 char1에서 몇 번째 문자부터 찾을 것인지를 나타내는 위치이며 생략 시 1이 적용
- n2는 char1에서 char2문자를 찾을 때 일치하는 문자의 몇 번째 위치를 반환할지를 나타냄. 
- 생략 시 1이 적용
*/
select instr('ABABAB', 'A', 2) from dual;

select instr('ABABAB', 'A') first,
    instr('ABABAB', 'A', 2) second,
    instr('ABABAB', 'A', 2, 1) third,
    instr('ABABAB', 'A', 2, 2) fourth
    from dual;

-- length(char) char 문자의 글자 수를 반환
select length('the') from dual;

-- 날짜형 함수 DATE / TIMESTAMP
-- sysdate 현재 일자와 시간을 반환
select sysdate from dual;
select to_char(sysdate, 'YYYY-MM-DD/HH24:MI:SS') from dual;

-- add_months(date, n) date 날짜에 n개월을 더한 날짜를 반환.
-- n이 음수이면 더하지 않고 뺀 날짜를 반환
select add_months(sysdate, 1) from dual;

-- months_between(date1, date2)
-- date1과 date2 두 날짜 사이의 개월 수를 반환.
-- date1이 date2보다 이후 날짜면 양수, 반대면 음수 반환
select months_between(sysdate + 31, sysdate) from dual;

-- last_day(date) date가 속한 월의 마지막 일자를 반환
select last_day(sysdate) from dual;

-- next_day(date, expr) date 날짜를 기준으로 expr에 명시한 날짜 반환.
-- expr은 요일을 나타내는데, '월요일' 형태로 쓸 수도 있고 1~7까지 숫자를 쓸 수도 있음.
-- 1은 일요일, 7은 토요일
select next_day(sysdate, 2) from dual;

-- round(date, format) date를 format 기준으로 반올림한 날짜 반환.
-- format은 YEAR, MONTH, DD, HH, HH224, MI 등 사용 가능
select round(sysdate, 'YEAR') from dual;

-- trunc(date, format) date를 format 기준으로 잘라낸 날짜 반환.
-- format은 round 함수와 동일하게 사용 가능
select trunc(sysdate, 'YEAR') from dual;

-- 형변환 함수
-- to_number(char) char을 숫자로 반환
select to_number('12345') from dual;

-- to_char(n, number_format) 숫자인 n을 number_format에 맞게 문자로 변환
-- number_format은 생략 가능
select to_char(12345, '99,999') from dual;

-- to_char(date, date_format) 날짜인 date를 date_format에 맞게 문자로 변환
-- date_format은 생략 가능
select to_char(sysdate, 'YYYY-MM-DD HH24:MI:SS') from dual;
-- 요일까지 표현
select to_char(sysdate, 'DL') from dual;

-- to_date(char, date_format) 문자 char을 date_format에 맞게 날짜로 변환
-- date_format은 생략 가능
select to_date('2018-04-02 23:52:01', 'YYYY-MM-DD HH24:MI:SS') from dual;

-- 명시적 형변환
CREATE TABLE emp04
(
    emp_id NUMBER NOT NULL,
    emp_name VARCHAR2(100) NOT NULL,
    gender VARCHAR2(10) NULL,
    age NUMBER NULL,
    hire_date DATE NULL,
    etc VARCHAR2(300) NULL,
    PRIMARY KEY(emp_id)
);
insert into emp04 (emp_id, emp_name, gender, age, hire_date)
values(1, 'Chris', 'Man', 28, to_date('2021-12-22', 'YYYY-MM-DD'));
select * from emp04;

-- 기타 함수
-- NULL 관련 함수
/*
NVL(expr1, expr2) :
epxr1 값이 NULL인 경우 expr2를 반환하는 함수로 꽤 많이 사용되는 함수 중 하나.
쓰임새는 매우 다양, NULL 허용 컬럼 값을 조회할 때 해당 컬럼에 데이터가 있는 경우(expr1)는
그대로 보여주고, 데이터가 없는 NULL인 경우는 대체 값(expr2)을 보여줄 때 주로 사용
*/

-- NVL2(expr1, expr2, exp3) expr1 값이 NULL인 경우 expr3을
-- NULL이 아닌 경우에는 expr2를 반환하는 함수

-- COALESCE(expr1, expr2, ...) 매개변수인 expr1, expr2, ... 에서 첫 번째로
-- NULL이 아닌 값을 반환

-- NULLIF(expr1, expr2) 매개변수인 expr1과 expr2 값을 비교해 두 값이 같으면 NULL을,
-- 같지 않으면 expr1을 반환.
select NVL(NULL, 'N/A'),
    NVL2(1, 2, 3),
    COALESCE(NULL, NULL, 5, 4, NULL),
    NULLIF('NL', 'nl')
    from dual;

-- 기타 함수
/*
GREATEST(expr1, expr2, ...)
매개변수 expr1, expr2, ... 중 가장 큰 값을 찾아 반환. 매개변수 값에 대해 내부적으로
비교 연산을 수행해 그 중 큰 값을 결과로 반환하므로 expr에 문자, 숫자, 날짜가 올 수 있음.
문자끼리 혹은 숫자끼리의 비교뿐만 아니라 문자와 숫자가 동시에 올 수 있음.
이때 이 함수의 반환 값의 데이터형은 첫 번째 매개변수인 expr1을 따름
*/
select greatest('a', 2, 3, 4) from dual;
-- 아스키 코드 값으로 비교 but 첫 번째 숫자 그 뒤 문자는 비교 x

-- LEAST(expr1, expr2, ...) 가장 작은 값 반환

/*
DECODE(expr, comp_val1, result1, comp_val2, result2, ..., default_value)
첫 번째 매개변수인 expr 값이 comp_val1과 같으면 result1을 반환하고,
comp_val2와 같으면 result2를 반환하는 식. 어느 것과도 같지 않으면 맨 끝에 명시한
default_value를 반환하는데, 이를 생략하면 NULL을 반환.
이 함수의 매개변수는 expr, default_value를 포함해 255개까지 사용 가능.
*/

-- CASE 표현식 DECODE 함수 대체 가능
/*
단순형 CASE 표현식 구문

CASE expr WHEN comparision_expr1 THEN return_expr1
          WHEN comparision_expr2 THEN return_expr2
          ...
          ELSE else_expr
END

단순형 CASE 표현식은 expr 값이 WHEN 다음의 comparision_expr1과 같으면 return_expr1을,
comparision_expr2와 같으면 return_expr2를 반환하는 식으로 처리됨.
모든 WHEN 절과 비교해 같지 않으면 ELSE 절로 제어권이 넘어와 else_expr을 반환.
주의할 점은 return_expr1, return_expr2, ..., else_expr은 모두 같은 데이터형이어야 함.
*/

/*
검색형 CASE 표현식 구문

CASE WHEN condition1 THEN return_expr1
     WHEN condition2 THEN return_expr2
     ...
     ELSE else_expr
END

검색형 CASE 표현식은 WHEN 절 자체에 비교 조건이 들어가고 나머지는 단순형과 쓰임새가 동일.
단순형은 expr 값이 WHEN 절 이하의 값과 같은 경우만 체크할 수 있는 반면,
검색형 CASE 표현식은 WHEN 절에서 조건식을 사용할 수 있어 다양한 조건 비교가 가능해
그 활용 범위가 더 넓음. 다양한 연산자를 사용해 비교 범위를 넓힐 수 있음.
*/
select emp_name, age,
    case when age between 0 and 19 then '10대'
         when age between 20 and 29 then '20대'
         when age between 30 and 39 then '30대'
         when age between 40 and 49 then '40대'
         when age between 50 and 59 then '50대'
         else '60대 이상'
    end ages
from emp04;
commit;