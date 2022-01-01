-- ������ �Է°� ���� �׸��� ����
-- 1. INSERT
-- SELECT ���� �����ϸ� �� ���� ���� ���� �ο� �����͸� �Է��� �� ����.

-- CREATE TABLE ... AS ������ ����� ���̺� ����
create table subway_dml_test as
select * from subway_statistics where rownum < 1;

alter table subway_dml_test add primary key (seq_id);
/*
SELECT ������ ��ȸ�� ��� ���·� �ڵ����� ���̺��� ��������� ���ÿ� �����ͱ��� �����.
���⼭�� WHERE < 1�̶� ���� ������ �����ʹ� �ϳ��� ��������� ����.
ROWNUM�̶� ����Ŭ������ ����� �� �ִ� �ǻ��÷����� SELECT ������ ��ȯ�Ǵ� �ο� ���� ����
CREATE TABLE ... AS �������� ���̺��� �����ϸ� ������ �÷� ���Ǹ� ������� �ʾƵ� ��
������ �ε����� �⺻ Ű�� ���� �� ���ٴ� ��
���� ALTER TABLE ������ ����� �⺻ Ű�� �����ؾ���
�⺻ Ű Ȥ�� �÷��� �߰��ϰų� �÷� ���� ������ ����, �÷��� ������ ���� ALTER TABLE ���
*/

-- ���տ�忪 ������ �Է�
insert into subway_dml_test
select * from subway_statistics where station_name like '���տ��%';

commit;

select * from subway_dml_test;

-- subway_dml_test ���̺� subway_statistics ��ü ������ �Է�
insert into subway_dml_test
select * from subway_statistics;
-- ���� �߻� ORA-00001: ���Ἲ ���� ����(C##JNGMK.SYS_C008333)�� ����˴ϴ�
-- SYS_C008333 : subway_dml_test ���̺��� �⺻ Ű�� �ǹ�
-- ���տ�忪�� ���� �� �ִµ� �ٽ� �Է��Ϸ��� ���� seq_id ���� �ߺ��Ǿ� ����

-- �ߺ������� �����ϰ� ������ �Է�
insert into subway_dml_test
select * from subway_statistics where station_name not like '���տ��%';

commit;

-- �⺻ Ű�� �浹���� �ʰ� ������ �Է�
insert into subway_dml_test
select a.* from subway_statistics a
where not exists (select 1 from subway_dml_test b where a.seq_id = b.seq_id);

-- 2. DELETE
/*
DELETE ���� INSERT ���� �ٸ��� SELECT ����� �����ϴ� ���´� ����
���̺��� �����͸� �����ϹǷ� SELECT  ���� �ʿ� ����
������ � �����͸� ������ ������ WHERE ���� �߰��� ������ �� �� ����
*/

-- ���տ�忪 ������ ����
delete from subway_dml_test
where station_name like '���տ��%';

commit;

-- 3. UPDATE
-- ������ ����
/*
UPDATE ���̺� ��
SET COLUMN1 = ��1
    ,COLUMN2 = ��2
    , ...
WHERE ��;

UPDATE ���� ������ ���̺� ���� ����ϰ� SET ������ ������ �÷��� ������ ���� '�÷� = ��'
���·� ���. ���� ���� �÷� ���� �����Ϸ��� �޸�(,)�� ������ ��� �߰��ϸ� ��
���⼭ '='��ȣ�� WHERE ���������� ����ߴ� ���� �����ڰ� �ƴ϶� '='�� �������� ������ ����
���� �÷� ���� �Ҵ��϶�� �ǹ�. ����, ���̺��� Ư�� �����͸� �����ؾ� �� ��쿡��
WHERE ���� �߰��� ������ ������ �ָ� ��
*/

-- ���� �� �Ｚ�� ������
SELECT * FROM subway_dml_test
WHERE station_name LIKE '�Ｚ%'
ORDER BY seq_id;

-- UPDATE ��
UPDATE subway_dml_test
SET passenger_number = passenger_number + 10
    , boarding_date = ADD_MONTHS(boarding_date, 1)
WHERE station_name LIKE '�Ｚ%';

commit;

-- ���� �� �Ｚ�� ������
select * from subway_dml_test
where station_name like '�Ｚ%'
order by seq_id;
