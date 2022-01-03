-- SQL �ǽ�
-- �����ζ� �м�
-- lotto_master ���̺� ����
CREATE TABLE lotto_master(
    seq_no NUMBER NOT NULL, -- �ζ�ȸ��
    draw_date DATE,         -- ��÷��
    num1 NUMBER,            -- ��÷��ȣ1
    num2 NUMBER,            -- ��÷��ȣ2
    num3 NUMBER,            -- ��÷��ȣ3
    num4 NUMBER,            -- ��÷��ȣ4
    num5 NUMBER,            -- ��÷��ȣ5
    num6 NUMBER,            -- ��÷��ȣ6
    bonus NUMBER);          -- ���ʽ���ȣ
    
ALTER TABLE lotto_master
ADD CONSTRAINTS lotto_master_pk PRIMARY KEY (seq_no);

-- lotto_detail ���̺� ����
CREATE TABLE lotto_detail(
    seq_no NUMBER NOT NULL,     -- �ζ�ȸ��
    rank_no NUMBER NOT NULL,    -- ���
    win_person_no NUMBER,       -- ��÷�� ��
    win_money NUMBER);          -- 1�δ� ��÷�ݾ�
    
ALTER TABLE lotto_detail
ADD CONSTRAINTS lotto_detail_pk PRIMARY KEY (seq_no, rank_no);

select * from lotto_master order by 1;

-- �ߺ� ��ȣ ��ȸ
-- �ߺ��� �ζ� ��ȣ ���� ���� ��ȸ(GROUP BY)
select num1, num2, num3, num4, num5, num6, count(*)
from lotto_master
group by num1, num2, num3, num4, num5, num6;

-- �ߺ��� �ζ� ��ȣ ���� ���� ��ȸ(GROUP BY & HAVING)
select num1, num2, num3, num4, num5, num6, count(*)
from lotto_master
group by num1, num2, num3, num4, num5, num6
having count(*) > 1;
-- ��ȸ�� ������ ����. �̷ν� 827ȸ���� �ߺ��� ��÷��ȣ�� ������ �� �� ����.

-- ���� ���� ��÷�� ��÷��ȣ ��ȸ (���ʽ���ȣ ����)
-- num1 �÷� ���� ��÷ �Ǽ� ��ȸ
select num1 lotto_num, count(*) cnt
from lotto_master group by num1 order by 2 desc;

-- ���� ���� ��÷��ȣ ��ȸ
select lotto_num, sum(cnt) as cnt
from (select num1 lotto_num, count(*) cnt
        from lotto_master
        group by num1
        union all
        select num2 lotto_num, count(*) cnt
        from lotto_master
        group by num2
        union all
        select num3 lotto_num, count(*) cnt
        from lotto_master
        group by num3
        union all
        select num4 lotto_num, count(*) cnt
        from lotto_master
        group by num4
        union all
        select num5 lotto_num, count(*) cnt
        from lotto_master
        group by num5
        union all
        select num6 lotto_num, count(*) cnt
        from lotto_master
        group by num6)
        group by lotto_num
        order by 2 desc;

-- ���� ���� ��÷���� ���� ȸ���� ��ȣ, �ݾ� ��ȸ
-- �ִ� ��÷�ݰ� ��÷��ȣ ��ȸ
select a.seq_no
        ,a.draw_date
        ,b.win_person_no
        ,b.win_money
        ,a.num1, a.num2, a.num3, a.num4, a.num5, a.num6, a.bonus
        from lotto_master a, lotto_detail b
        where a.seq_no = b.seq_no
        and b.rank_no = 1
        order by b.win_money desc;


-- ������ �м�
-- �������� DB(www.ktdb.go.kr)
-- traffic_accident ���̺� ����
create table traffic_accident(
    year number not null,               -- ����
    trans_type varchar2(30) not null,   -- �������
    total_acct_num number,              -- ��� �Ǽ�
    death_person_num number);           -- ����� ��
    
alter table traffic_accident
add constraints traffic_accident_pk primary key (year, trans_type);

select * from traffic_accident;

-- ����, ������ܺ� �� ��� �Ǽ� ��ȸ
-- ����, ������ܺ� ���, ��� �Ǽ� ��ȸ
select case when year between 1980 and 1989 then '1980���'
            when year between 1990 and 1999 then '1990���'
            when year between 2000 and 2009 then '2000���'
            when year between 2010 and 2019 then '2010���'
            end as years
            ,trans_type
            ,sum(total_acct_num) as ���Ǽ�
            ,sum(death_person_num) as ����ڼ�
    from traffic_accident
    where 1 = 1
    group by case when year between 1980 and 1989 then '1980���'
                  when year between 1990 and 1999 then '1990���'
                  when year between 2000 and 2009 then '2000���'
                  when year between 2010 and 2019 then '2010���'
                 end, trans_type
    order by 1, 2;
    
-- ���뺰 ���� �м�
-- ������ܺ� ��� �Ǽ� ���뺰 ����
-- ��Ī�� ���ڷ� ������ �� ����. "" �� ���ξ� ��.
SELECT trans_type
      ,SUM(CASE WHEN year BETWEEN 1980 AND 1989 THEN total_acct_num ELSE 0 END) "1980���"
      ,SUM(CASE WHEN year BETWEEN 1990 AND 1999 THEN total_acct_num ELSE 0 END) "1990���"
      ,SUM(CASE WHEN year BETWEEN 2000 AND 2009 THEN total_acct_num ELSE 0 END) "2000���"
      ,SUM(CASE WHEN year BETWEEN 2010 AND 2019 THEN total_acct_num ELSE 0 END) "2010���"
FROM traffic_accident
WHERE 1=1
GROUP BY trans_type
ORDER BY trans_type;

-- ������ܺ� ����� �� ���뺰 ����
select trans_type,
    sum(case when year between 1980 and 1989 then death_person_num else 0 end) "1980���",
    sum(case when year between 1990 and 1999 then death_person_num else 0 end) "1990���",
    sum(case when year between 2000 and 2009 then death_person_num else 0 end) "2000���",
    sum(case when year between 2010 and 2019 then death_person_num else 0 end) "2010���"
    from traffic_accident
    where 1 = 1
    GROUP BY trans_type
    ORDER BY trans_type;
    
-- ������ܺ� ���� ���� ����� ���� �߻��� ���� ���ϱ�
-- ������ܺ� ����� �� ������ ����
-- �������� ���
select a.*
from traffic_accident a,
    (select trans_type,
    max(death_person_num) death_per
    from traffic_accident
    group by trans_type) b
    where a.trans_type = b.trans_type
    and a.death_person_num = b.death_per;
    
-- ����� �̼����� �м�
-- �����ڸ���(https://www.airkorea.or.kr)
-- fine_dust ���̺� ����
create table fine_dust(
    gu_name varchar2(50) not null,          -- �� ��
    mea_station varchar2(30) not null,      -- ������
    mea_date date not null,                 -- ��������
    pm10 number,                            -- �̼����� ��
    pm25 number);                           -- �ʹ̼����� ��

alter table fine_dust
add constraints fine_dust_pk primary key (gu_name, mea_station, mea_date);

-- fine_dust_standard ���̺� ���� (�̼��� ���� ���̺�)
-- �̼������� �ʹ̼����� �󵵿� ���� �̼����� ���� �����͸� ��� ����
create table fine_dust_standard(
    org_name varchar2(50) not null,     -- �����
    std_name varchar2(30) not null,     -- �̼����� ����(����, ����, ����, �ſ쳪��)
    pm10_start number,                  -- �̼����� ��(���� ��)
    pm10_end number,                    -- �̼����� ��(�� ��)
    pm25_start number,                  -- �ʹ̼����� ��(���� ��)
    pm25_end number);                   -- �ʹ̼����� ��(�� ��)
    
alter table fine_dust_standard
add constraints fine_dust_standard_pk primary key (org_name, std_name);

-- ���� �̼������� �ʹ̼������� �ּ�, �ִ�, ��հ� ���ϱ�
-- ���� �̼������� �ּ�, �ִ�, ��հ�
select to_char(a.mea_date, 'YYYY-MM') months
    ,round(min(a.pm10), 0) pm10_min
    ,round(max(a.pm10), 0) pm10_max
    ,round(avg(a.pm10), 0) pm10_avg
    ,round(min(a.pm25), 0) pm25_min
    ,round(max(a.pm25), 0) pm25_max
    ,round(avg(a.pm25), 0) pm25_avg
    from fine_dust a
    where pm10 > 0
    and pm25 > 0
    group by to_char(mea_date, 'YYYY-MM')
    order by 1;
    
-- ����� �̼����� ��Ȳ
-- ����� �̼����� ����
select a.months, a.pm10_avg,
        (select b.std_name
        from fine_dust_standard b
        where b.org_name = 'WHO'
        and a.pm10_avg between b.pm10_start and b.pm10_end) "�̼����� ����"
        ,a.pm25_avg,
        (select b.std_name
        from fine_dust_standard b
        where b.org_name = 'WHO'
        and a.pm25_avg between b.pm25_start and b.pm25_end) "�ʹ̼����� ����"
    from (select to_char(a.mea_date, 'YYYY-MM') months
    ,round(avg(a.pm10), 0) pm10_avg
    ,round(avg(a.pm25), 0) pm25_avg
    from fine_dust a
    where a.pm10 > 0
    and a.pm25 > 0
    group by to_char(mea_date, 'YYYY-MM')) a
    order by 1;