-- GROUP BY ���� ���� �Լ�
/*
SELECT expr1, expr2, ...
    FROM ...
    WEHRE ...
    AND ...
    GROUP BY expr1, expr2, ...
    ORDER BY ...

������ ��� �÷��̳� ǥ������ ����ϸ� ��.
GROUP BY ���� ����� ��� �÷��̳� ǥ������ SELECT ������ ����ؾ� ��.
���� �Լ��� ���� ����ؾ� �ǹ̰� �ִ�.

COUNT(expr) expr�� ��ü ������ ���� ��ȯ. ���� *. �ش� select������ ��ȸ�� ��ü ������
MAX(expr) expr�� �ִ��� ��ȯ
MIN(expr) wxpr�� �ּڰ��� ��ȯ
SUM(expr) expr�� �հ踦 ��ȯ
AVG(expr) expr�� ��հ��� ��ȯ
VARIANCE(expr) expr�� �л��� ��ȯ
STDDEV(expr) expr�� ǥ�������� ��ȯ
���� �Լ��� select �������� ����� �� ����.
*/
select station_name from subway_statistics
    where gubun = '����'
    group by station_name
    order by station_name;

select count(*) cnt,
    MIN(passenger_number) min_value,
    MAX(passenger_number) max_value,
    SUM(passenger_number) sum_value,
    AVG(passenger_number) avg_value
    from subway_statistics;
    
-- ����ö���� ���� �ο� ���
select station_name, count(*) cnt,
    min(passenger_number) min_value,
    max(passenger_number) max_value,
    sum(passenger_number) sum_value,
    avg(passenger_number) avg_value
FROM subway_statistics
where gubun = '����'
group by station_name
order by station_name;

-- ���ε����д����� �ð��� ������ �ο� ��ȸ
select station_name,
    boarding_time,
    gubun,
    min(passenger_number) min_value,
    max(passenger_number) max_value,
    sum(passenger_number) sum_value
    from subway_statistics
    where station_name in ('���ε����д���(232)')
    group by station_name, boarding_time, gubun
    order by station_name, boarding_time, gubun;

-- ���� �ο��� ���� ������ ��ȸ
select station_name,
    boarding_time,
    gubun,
    min(passenger_number) min_value,
    max(passenger_number) max_value,
    sum(passenger_number) sum_value
    from subway_statistics
    group by station_name, boarding_time, gubun
    order by 6 desc;
    
-- HAVING �� ���� ������ ������
SELECT station_name,
    boarding_time,
    gubun,
    min(passenger_number) min_value,
    max(passenger_number) max_value,
    sum(passenger_number) sum_value
    from subway_statistics
    group by station_name, boarding_time, gubun
    having sum(passenger_number) between 15000 and 16000
    order by 6 desc;

-- DISTINCT �ߺ� ���� ������ ������ ���鸸 ��ȸ�Ǿ� group by ���� ����� ȿ���� ��.
select distinct station_name
from subway_statistics
order by 1;

