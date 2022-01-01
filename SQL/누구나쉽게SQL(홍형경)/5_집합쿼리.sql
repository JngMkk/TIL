/*
���� ����

�⺻������ �� �� �̻��� �������� SELECT ������ �����ϴ� ����.
�������� �� SELECT���� ��ȯ�ϴ� ����� �ϳ��� �������� ����,
���� �����ڸ� ����� �� ������ ������ ���·� ������ ������ ������ ���·� ������ ������
ó���� �� ����. ���� ������ ����Ǵ� �������� �� SELECT���� ��ȯ�ϴ� ����� �÷� ����
���������� ���� ��� �����ؾ� ��.
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
values(1, '��������', '����', 23, to_date('2018-02-01', 'YYYY-MM-DD'));
insert into emp08 (emp_id2, emp_name2, gender, age, hire_date)
values(2, '�㳭����', '����', 33, to_date('2018-02-01', 'YYYY-MM-DD'));
insert into emp08 (emp_id2, emp_name2, gender, age, hire_date)
values(3, '�踸��', '����', 43, to_date('2018-02-01', 'YYYY-MM-DD'));
insert into emp08 (emp_id2, emp_name2, gender, age, hire_date)
values(4, '�����', '����', 35, to_date('2018-02-01', 'YYYY-MM-DD'));
insert into emp08 (emp_id2, emp_name2, gender, age, hire_date)
values(5, '�Ż��Ӵ�', '����', 45, to_date('2018-02-01', 'YYYY-MM-DD'));
commit;
select * from emp08;

/*
UNION ALL
�� ������ ��� ���Ҹ� �������� ������ ����� ����.

SELECT col1, col2, ...
FROM ...
WHERE ...
UNION ALL
SELECT col1, col2, ...
FROM ...
WHERE ...

�Ϲ� SELECT ����� �ٸ� ���� �� ���� ���̿� UNION ALL�̶�� ���� �����ڰ� �߰��ƴٴ� ��.
���� �����ڷ� ����Ǵ� SELECT ������ ���� ����ϴ� �÷� ���� ���������� ��ġ�ؾ� ������,
SELECT ���� ����ϴ� �÷��� �̸��� �޶� ��� ����.
���� �����ڸ� ����� ������ ���� ��ȸ ����� ù ��° SELECT ���� �÷� ���� �������� ��ȸ.
���� �����ڸ� ����� �� ������ ������ �Ϲ� SELECT ���� �����ϰ� ORDER BY���� ���.
���� �� ������ �� �� ����
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
�� ������ �����ϸ� UNION ALL�� ����.
UNION�� ��� �ߺ� �����Ͱ� ������ ��� �� �����Ͱ� 1�Ǹ� ��ȸ��.
SELECT ������ ���� �ٸ� �÷�(EMP_ID�� GENDER �÷�)�� ����� ��� UNION�� ����ϴ���
�ߺ� �����ͷ� �������� �ʰ� ��� ��ȸ.
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
�� ������ ���� ���Ҹ� �����ϴ� ������ ������ ��.
�� ���� ���� ����� �˻��� ����� ��ҿ� �ش��ϴ� ����� �������� ��.
*/
SELECT age
from emp03
intersect
select age
from emp08
order by 1;

-- MINUS �� ������ �������� �ٸ� ���տ� ���� ��Ҹ� �����ϴ� ������ ����.
select age
from emp03
minus
select age
from emp08
order by 1;
