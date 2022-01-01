create table emp_master(
    emp_id number not null,             -- �����ȣ
    emp_name varchar2(100) not null,    -- ��� ��
    gender varchar2(10),                -- ����
    age number,                         -- ����
    hire_date date,                     -- �Ի�����
    dept_id number,                     -- �μ����̵�
    address_id number,                  -- �ּҾ��̵�
    constraint emp_master_pk primary key (emp_id)
);

create table dept_master(
    dept_id number not null,            -- �μ����̵�
    dept_name varchar2(50),             -- �μ� ��
    use_yn varchar(2) default 'Y',      -- ��뿩��
    -- default 'Y' : ���� ���� �ʾƵ� �ڵ����� 'Y'���� �־���
    dept_desc varchar2(100),            -- �μ�����
    constraint dept_master_pk primary key (dept_id)
);

create table address_master(
    address_id number not null,         -- �ּҾ��̵�
    city varchar2(100),                 -- ���� ��
    gu varchar2(50),                    -- �� ��
    address_name varchar2(100),         -- ������ �ּ�
    constraint address_master_pk primary key (address_id)
);

INSERT INTO emp_master ( emp_id, emp_name, gender, age, hire_date, dept_id, address_id )
VALUES (1, '������', '����', 56, TO_DATE('2018-01-01', 'YYYY-MM-DD'), 1, 1);

INSERT INTO emp_master ( emp_id, emp_name, gender, age, hire_date, dept_id, address_id )
VALUES (2, '�Ż��Ӵ�', '����', 34, TO_DATE('2018-01-01', 'YYYY-MM-DD'), 1, 2);

INSERT INTO emp_master ( emp_id, emp_name, gender, age, hire_date, dept_id, address_id )
VALUES (3, 'ȫ�浿', '����', 45, TO_DATE('2018-01-01', 'YYYY-MM-DD'), 3, 2);

INSERT INTO emp_master ( emp_id, emp_name, gender, age, hire_date, dept_id, address_id )
VALUES (4, '������', '����', 23, TO_DATE('2018-01-01', 'YYYY-MM-DD'), 2, 3);

INSERT INTO emp_master ( emp_id, emp_name, gender, age, hire_date, dept_id, address_id )
VALUES (5, '�������', '����', 45, TO_DATE('2018-01-01', 'YYYY-MM-DD'), 4, 4);


INSERT INTO dept_master ( dept_id, dept_name )
VALUES (1, 'ȸ����');

INSERT INTO dept_master ( dept_id, dept_name )
VALUES (2, '�濵��');

INSERT INTO dept_master ( dept_id, dept_name )
VALUES (3, '������');

INSERT INTO dept_master ( dept_id, dept_name )
VALUES (4, '��������');

INSERT INTO address_master ( address_id, city, gu, address_name )
VALUES (1, '����Ư����', '�߱�', '�����ȷ� 12');

INSERT INTO address_master ( address_id, city, gu, address_name )
VALUES (2, '����Ư����', '���빮��', '����� 15��');

INSERT INTO address_master ( address_id, city, gu, address_name )
VALUES (3, '����Ư����', '��������', '���Ǵ�� 99');

INSERT INTO address_master ( address_id, city, gu, address_name )
VALUES (4, '����Ư����', '������', '������� 33');
commit;

select * from dept_master;

/*
���� ����
WHERE ������ ���� �����ڸ� ����� ����� �÷�, �� ���� �÷��� ���ϴ� ����.
*/
select a.emp_id, a.emp_name, a.gender, a.age, a.dept_id,
        b.dept_id, b.dept_name, b.use_yn
        from emp_master a, dept_master b
        where a.dept_id = b.dept_id
        order by a.emp_id;

-- ANSI ���� ���� ����
select a.emp_id, a.emp_name, a.gender, a.age, a.dept_id,
        b.dept_id, b.dept_name, b.use_yn
        from emp_master a
        inner join dept_master b
        on a.dept_id = b.dept_id
        order by a.emp_id;
        
select a.emp_id, a.emp_name, a.gender, a.age, a.dept_id,
        b.dept_id, b.dept_name, b.use_yn
        from emp_master a, dept_master b
        where a.dept_id = b.dept_id
        and a.gender = '����'
        order by a.emp_id;
        
select a.emp_id, a.emp_name, a.gender, a.age, a.dept_id,
        b.dept_id, b.dept_name, b.use_yn
        from emp_master a
        inner join dept_master b
        on a.dept_id = b.dept_id
        where a.gender = '����'
        order by a.emp_id;
        
select a.emp_id, a.emp_name, a.gender, a.age,
        b.dept_id, b.dept_name, b.use_yn,
        c.address_id, c.city, c.address_name
        from emp_master a, dept_master b, address_master c
        where a.dept_id = b.dept_id
        and a.address_id = c.address_id
        and a.gender = '����'
        order by a.emp_id;
        
select a.emp_id, a.emp_name, a.gender, a.age,
        b.dept_id, b.dept_name, b.use_yn,
        c.address_id, c.city, c.address_name
        from emp_master a
        inner join dept_master b
        on a.dept_id = b.dept_id
        inner join address_master c
        on a.address_id = c.address_id
        where a.gender = '����'
        order by a.emp_id;
        
/*
�ܺ� ����
���� ������ �� ���̺��� ���� �÷� ���� ���� ���� ��ȸ�ϴµ� ����,
�ܺ� ������ �� ���̺� �� �� ���̺��� ���� �÷� ���� ������ ���� �Ǳ��� ��� ������
��ȸ�ϴ� ����.
*/

insert into emp_master(emp_id, emp_name, gender, age, hire_date, dept_id, address_id)
values (6, '�հ�', '����', 35, to_date('2018-01-01', 'YYYY-MM-DD'), null, 4);

commit;

select * from emp_master;

-- LEFT JOIN
select a.emp_id, a.emp_name, a.gender, a.age, a.dept_id,
        b.dept_id, b.dept_name, b.use_yn
        from emp_master a, dept_master b
        where a.dept_id = b.dept_id (+)
        order by a.emp_id;
        
-- LEFT JOIN(ANSI)
select a.emp_id, a.emp_name, a.gender, a.age, a.dept_id,
        b.dept_id, b.dept_name, b.use_yn
        from emp_master a
        left join dept_master b
        on a.dept_id = b.dept_id
        order by a.emp_id;
        
insert into dept_master(dept_id, dept_name)
values (5, 'IT��');
commit;

select * from dept_master;


-- RIGHT JOIN
select a.emp_id, a.emp_name, a.gender, a.age, a.dept_id,
        b.dept_id, b.dept_name, b.use_yn
        from emp_master a, dept_master b
        where a.dept_id(+) = b.dept_id
        order by a.emp_id;

-- RIGHT JOIN(ANSI)
select a.emp_id, a.emp_name, a.gender, a.age, a.dept_id,
        b.dept_id, b.dept_name, b.use_yn
        from emp_master a
        right join dept_master b
        on a.dept_id = b.dept_id
        order by a.emp_id;

-- FULL OUTER JOIN(ANSI)
select a.emp_id, a.emp_name, a.gender, a.age, a.dept_id,
        b.dept_id, b.dept_name, b.use_yn
        from emp_master a
        full outer join dept_master b
        on a.dept_id = b.dept_id
        order by a.emp_id;

/*
īƼ�� ��
WHERE ���� ���� ������ ���� �ʴ� ���� ����.
�� ���̺��� �����͸� �������� ������ ��� ������ �����Ͱ� ��ȸ��.
*/
SELECT a.emp_id, a.emp_name, a.gender, a.age, a.dept_id,
        b.dept_id, b.dept_name, b.use_yn
        from emp_master a, dept_master b
        order by a.emp_id;