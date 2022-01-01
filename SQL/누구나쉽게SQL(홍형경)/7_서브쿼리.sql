/*
���ݱ��� ���� ������ �� �ϳ��� SELECT �������� �̷���� �־��µ�, �̸� �� ���� Ȥ��
����������� �Ѵ�. ���������� �������� �ȿ� �ִ� �� �ٸ� SELECT ������ ���Ѵ�.
���� ���������� �����ϴ� SELECT ������ �׻� ��ȣ�� �ѷ��ο�����.
���������� SELECT ���� ���Ǿ� Ư�� ���� ��ȯ�� �� �ְ�, FROM ���� ���Ǿ� ��ġ
���̺�ó�� ����� ���� ����. ��, WHERE ������ ���� ���� ���ϴ� ���� ����.
*/

/*
��Į�� ��������
���� ������ SELECT ������ ��ġ �÷��̳� ǥ����ó�� ���.
��Į�� �������� ���� SELECT �������� �� �ϳ��� �÷��̳� ǥ���ĸ� ����� �� ����.
���� �÷��̳� ǥ���ĵ��� +�� ||�����ڷ� ������ ���� ��ȯ���� �� �����
���� ���� ����� ���� ����. ����, �������� �ϳ��� �ϳ��� �÷��̳� ǥ���� ������ �ϹǷ�
�� �� �̻��� ��, �� ��ȯ�ϴ� �÷� ���� 2 �̻��̸� �ȵ�. ���� ��ȯ�Ǵ� �ο� ����
�ݵ�� 1������ ��.
*/

SELeCT a.emp_id, a.emp_name, a.gender, a.age, a.dept_id,
        (SELECT b.dept_name from dept_master b where a.dept_id = b.dept_id)
        dept_name
from emp_master a;

select a.emp_id, a.emp_name, a.gender, a.age, a.dept_id, b.dept_name
from emp_master a, dept_master b
where a.dept_id = b.dept_id(+);

/*
�ζ��� ��
���� ������ from ������ ����ϴ� ���������� ����.
��, from ������ �������� ��ü�� �ϳ��� ���̺�ó�� ���Ǵ� ��.
���� �ζ��� ��� ��Į�� ���������ʹ� �ٸ��� ���� ���� �÷��̳� ǥ����, ���� ���� �ο츦
��ȯ�� �� ����.
*/
select a.dept_id, a.dept_name, k.emp_id, k.emp_name, k.address
from dept_master a,
(select b.emp_id, b.emp_name, c.city || c.gu || c.address_name AS address, b.dept_id
from emp_master b, address_master c
where b.address_id = c.address_id) k
where a.use_yn = 'Y' and a.dept_id = k.dept_id
order by 1, 3;

/*
��ø ��������
where ������ ����ϴ� ��������.
where ������ ����Ѵٴ� ���� �������� �Ϻη� ���ȴٴ� ��.
�������� ���̺��� Ư�� �÷� ���� ���� ���� ��ȯ�ϴ� �뵵�� ���.
��ø ���������� �ζ��� ��ó�� ���� ���� �÷�, ���� ���� �ο츦 ��ȯ�� �� ����.
*/
-- ���� �� ��ȯ
select * from dept_master a
where a.dept_id = (select b.dept_id from emp_master b where b.emp_name = '�������');

-- ���� �� ��ȯ
select * from dept_master a
where a.dept_id in
(select b.dept_id from emp_master b where b.age between 40 and 49);

-- ���� �÷�, ���� �� ��ȯ
select * from emp_master a
where (a.gender, a.age) in
(select b.gender, b.age from emp_master b, address_master c
where b.address_id = c.address_id and c.gu in ('�߱�', '���빮��'));

/*
���� ����
���� ������ �˾ƺ� ��ø ������������ ����� ���� ���.
������������ ���� ���̺�� �������� ����� �����ϴ� ��.
*/
-- exists �����ڸ� ����� ���� ����
select * from dept_master a
where exists(select 1 from emp_master b where b.age between 40 and 49 and a.dept_id = b.dept_id);

-- ��Ƽ ������ ���� ���ΰ� ������ ������ not �����ڰ� ���ٴ� ���� �ٸ�.
-- not �����ڸ� ����� ��Ƽ ����
select * from dept_master a
where a.dept_id not in (Select b.dept_id from emp_master b where b.age between 40 and 49);

-- not exists�� ����� ��Ƽ ����
select * from dept_master a
where not exists (select 1 from emp_master b where b.age between 40 and 49 and a.dept_id = b.dept_id);