-- || �� ���� ����
select 'A' || 'B' from dual;

-- ������ �Լ�
select ABS(-1) from dual;

-- ceil(n) n�� ���ų� ū �ּ� ���� ��ȯ
select ceil(10.6) from dual;

-- exp(n) e�� n���� ��ȯ
select exp(10) from dual;

-- floor(n) n�� ���ų� ���� �ִ� ���� ��ȯ
select floor(10.6) from dual;

-- ln(n) n�� �ڿ��α� ���� ��ȯ, n�� 0���� Ŀ�� ��
select ln(10) from dual;

-- log(n2, n1) n2�� ��, n1�� ����. n1 > 0, n2�� 0�� 1�� �ƴ� ���
select log(10, 100) from dual;

-- mod(n2, n1) n2�� n1�� ���� ������ ��ȯ
select mod(11, 4) from dual;

-- power(n2, n1) n2�� n1���� ��ȯ
select power(3, 2) from dual;

-- round(n, i) n�� �Ҽ��� ���� (i+1)��°���� �ݿø��� ���� ��ȯ, 
-- ������ ���� �� i�� 0
select round(10.5453, 2) from dual;

-- sign(n) n�� ��ȣ ��ȯ, n�� ����̸� 1 �����̸� -1 0�̸� 0 ��ȯ
select sign(-3) from dual;

select sqrt(3) from dual;
-- trunc(n1, n2) n1�� �Ҽ��� ���� n2 �ڸ����� ����, n2 ���� �� 0
select trunc(10.5454, 2) from dual;

select round(565.545, -1) first,
    round(565.545, -2) second,
    round(565.545, -3) third
    from dual;

-- ������ �Լ�
-- chr(n) n�� ���ڷ� n ���� �ش�Ǵ� ���ڸ� ��ȯ
select chr(65) || chr(66) || chr(67) from dual;

-- concat(char1, char2) char1�� char2 ���ڸ� ������ ����� ��ȯ, ||�����ڿ� ���� ���
select concat('A', 'B') from dual;

-- initcap(char) char�� ù ��° ���ڸ� �빮�ڷ� ��ȯ
select initcap('the') from dual;

-- lower(char) char�� �ҹ��ڷ� ��ȯ
select lower('THE') from dual;

-- upper(char) char�� �빮�ڷ� ��ȯ
select upper('the') from dual;

-- lpad(expr1, n, expr2) expr1�� ��ȯ�ϴµ�, 
-- expr2�� (n - expr1 ����)��ŭ ������ ä�� ��ȯ
select lpad('THE', 5, '*') from dual;

-- rpad(expr1, n, expr2) expr1�� ��ȯ�ϴµ�, 
-- expr2�� (n - expr1 ����)��ŭ �������� ä�� ��ȯ
select rpad('THE', 5, '*') from dual;

-- ltrim(expr1, expr2) expr1�� ���ʿ��� expr2�� ������ ����� ��ȯ
select ltrim('**THE**', '*') from dual;

-- rtrim(expr1, expr2) expr1�� �����ʿ��� expr2�� ������ ����� ��ȯ
select rtrim('**THE**', '*') from dual;

/*
substr(char, n1, n2)
- char���� n1 ��ġ���� ������ n2 ���̸�ŭ�� �߶� ����� ��ȯ
- n1�� 0���� ����ϸ� 1�� ����
- n1�� �����̸� char ������ ���������� �Ųٷ� ���� ������
- n2�� �����ϸ� n1���� ������ ��ȯ
- n2 ���� 1 �̸����� �����ϸ� NULL���� ��ȯ
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

-- trim(char) char�� ���� �� ������ ������ ����� ��ȯ
select trim('  ABCD EFG  ') from dual;

-- ascii(char) char ������ ASCII �ڵ� ���� ��ȯ, CHR �Լ��� �ݴ� ���
select ascii('A') from dual;

/*
instr(char1, char2, n1, n2)
- char1���� char2 ���ڸ� ã�� �� ���� ��ġ�� ��ȯ��
- n1�� char1���� �� ��° ���ں��� ã�� �������� ��Ÿ���� ��ġ�̸� ���� �� 1�� ����
- n2�� char1���� char2���ڸ� ã�� �� ��ġ�ϴ� ������ �� ��° ��ġ�� ��ȯ������ ��Ÿ��. 
- ���� �� 1�� ����
*/
select instr('ABABAB', 'A', 2) from dual;

select instr('ABABAB', 'A') first,
    instr('ABABAB', 'A', 2) second,
    instr('ABABAB', 'A', 2, 1) third,
    instr('ABABAB', 'A', 2, 2) fourth
    from dual;

-- length(char) char ������ ���� ���� ��ȯ
select length('the') from dual;

-- ��¥�� �Լ� DATE / TIMESTAMP
-- sysdate ���� ���ڿ� �ð��� ��ȯ
select sysdate from dual;
select to_char(sysdate, 'YYYY-MM-DD/HH24:MI:SS') from dual;

-- add_months(date, n) date ��¥�� n������ ���� ��¥�� ��ȯ.
-- n�� �����̸� ������ �ʰ� �� ��¥�� ��ȯ
select add_months(sysdate, 1) from dual;

-- months_between(date1, date2)
-- date1�� date2 �� ��¥ ������ ���� ���� ��ȯ.
-- date1�� date2���� ���� ��¥�� ���, �ݴ�� ���� ��ȯ
select months_between(sysdate + 31, sysdate) from dual;

-- last_day(date) date�� ���� ���� ������ ���ڸ� ��ȯ
select last_day(sysdate) from dual;

-- next_day(date, expr) date ��¥�� �������� expr�� ����� ��¥ ��ȯ.
-- expr�� ������ ��Ÿ���µ�, '������' ���·� �� ���� �ְ� 1~7���� ���ڸ� �� ���� ����.
-- 1�� �Ͽ���, 7�� �����
select next_day(sysdate, 2) from dual;

-- round(date, format) date�� format �������� �ݿø��� ��¥ ��ȯ.
-- format�� YEAR, MONTH, DD, HH, HH224, MI �� ��� ����
select round(sysdate, 'YEAR') from dual;

-- trunc(date, format) date�� format �������� �߶� ��¥ ��ȯ.
-- format�� round �Լ��� �����ϰ� ��� ����
select trunc(sysdate, 'YEAR') from dual;

-- ����ȯ �Լ�
-- to_number(char) char�� ���ڷ� ��ȯ
select to_number('12345') from dual;

-- to_char(n, number_format) ������ n�� number_format�� �°� ���ڷ� ��ȯ
-- number_format�� ���� ����
select to_char(12345, '99,999') from dual;

-- to_char(date, date_format) ��¥�� date�� date_format�� �°� ���ڷ� ��ȯ
-- date_format�� ���� ����
select to_char(sysdate, 'YYYY-MM-DD HH24:MI:SS') from dual;
-- ���ϱ��� ǥ��
select to_char(sysdate, 'DL') from dual;

-- to_date(char, date_format) ���� char�� date_format�� �°� ��¥�� ��ȯ
-- date_format�� ���� ����
select to_date('2018-04-02 23:52:01', 'YYYY-MM-DD HH24:MI:SS') from dual;

-- ����� ����ȯ
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

-- ��Ÿ �Լ�
-- NULL ���� �Լ�
/*
NVL(expr1, expr2) :
epxr1 ���� NULL�� ��� expr2�� ��ȯ�ϴ� �Լ��� �� ���� ���Ǵ� �Լ� �� �ϳ�.
���ӻ��� �ſ� �پ�, NULL ��� �÷� ���� ��ȸ�� �� �ش� �÷��� �����Ͱ� �ִ� ���(expr1)��
�״�� �����ְ�, �����Ͱ� ���� NULL�� ���� ��ü ��(expr2)�� ������ �� �ַ� ���
*/

-- NVL2(expr1, expr2, exp3) expr1 ���� NULL�� ��� expr3��
-- NULL�� �ƴ� ��쿡�� expr2�� ��ȯ�ϴ� �Լ�

-- COALESCE(expr1, expr2, ...) �Ű������� expr1, expr2, ... ���� ù ��°��
-- NULL�� �ƴ� ���� ��ȯ

-- NULLIF(expr1, expr2) �Ű������� expr1�� expr2 ���� ���� �� ���� ������ NULL��,
-- ���� ������ expr1�� ��ȯ.
select NVL(NULL, 'N/A'),
    NVL2(1, 2, 3),
    COALESCE(NULL, NULL, 5, 4, NULL),
    NULLIF('NL', 'nl')
    from dual;

-- ��Ÿ �Լ�
/*
GREATEST(expr1, expr2, ...)
�Ű����� expr1, expr2, ... �� ���� ū ���� ã�� ��ȯ. �Ű����� ���� ���� ����������
�� ������ ������ �� �� ū ���� ����� ��ȯ�ϹǷ� expr�� ����, ����, ��¥�� �� �� ����.
���ڳ��� Ȥ�� ���ڳ����� �񱳻Ӹ� �ƴ϶� ���ڿ� ���ڰ� ���ÿ� �� �� ����.
�̶� �� �Լ��� ��ȯ ���� ���������� ù ��° �Ű������� expr1�� ����
*/
select greatest('a', 2, 3, 4) from dual;
-- �ƽ�Ű �ڵ� ������ �� but ù ��° ���� �� �� ���ڴ� �� x

-- LEAST(expr1, expr2, ...) ���� ���� �� ��ȯ

/*
DECODE(expr, comp_val1, result1, comp_val2, result2, ..., default_value)
ù ��° �Ű������� expr ���� comp_val1�� ������ result1�� ��ȯ�ϰ�,
comp_val2�� ������ result2�� ��ȯ�ϴ� ��. ��� �Ͱ��� ���� ������ �� ���� �����
default_value�� ��ȯ�ϴµ�, �̸� �����ϸ� NULL�� ��ȯ.
�� �Լ��� �Ű������� expr, default_value�� ������ 255������ ��� ����.
*/

-- CASE ǥ���� DECODE �Լ� ��ü ����
/*
�ܼ��� CASE ǥ���� ����

CASE expr WHEN comparision_expr1 THEN return_expr1
          WHEN comparision_expr2 THEN return_expr2
          ...
          ELSE else_expr
END

�ܼ��� CASE ǥ������ expr ���� WHEN ������ comparision_expr1�� ������ return_expr1��,
comparision_expr2�� ������ return_expr2�� ��ȯ�ϴ� ������ ó����.
��� WHEN ���� ���� ���� ������ ELSE ���� ������� �Ѿ�� else_expr�� ��ȯ.
������ ���� return_expr1, return_expr2, ..., else_expr�� ��� ���� ���������̾�� ��.
*/

/*
�˻��� CASE ǥ���� ����

CASE WHEN condition1 THEN return_expr1
     WHEN condition2 THEN return_expr2
     ...
     ELSE else_expr
END

�˻��� CASE ǥ������ WHEN �� ��ü�� �� ������ ���� �������� �ܼ����� ���ӻ��� ����.
�ܼ����� expr ���� WHEN �� ������ ���� ���� ��츸 üũ�� �� �ִ� �ݸ�,
�˻��� CASE ǥ������ WHEN ������ ���ǽ��� ����� �� �־� �پ��� ���� �񱳰� ������
�� Ȱ�� ������ �� ����. �پ��� �����ڸ� ����� �� ������ ���� �� ����.
*/
select emp_name, age,
    case when age between 0 and 19 then '10��'
         when age between 20 and 29 then '20��'
         when age between 30 and 39 then '30��'
         when age between 40 and 49 then '40��'
         when age between 50 and 59 then '50��'
         else '60�� �̻�'
    end ages
from emp04;
commit;