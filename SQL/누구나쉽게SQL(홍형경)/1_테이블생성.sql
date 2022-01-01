CREATE TABLE emp03
(
    emp_id NUMBER NOT NULL,
    emp_name VARCHAR2(100) NOT NULL,
    gender VARCHAR2(10) NULL,
    age NUMBER NULL,
    hire_date DATE NULL,
    etc VARCHAR2(300) NULL,
    PRIMARY KEY(emp_id)
);

insert into emp03(emp_id, emp_name, gender, age, hire_date)
values(1, 'James', 'Man', 33, '2018-01-01');
insert into emp03(emp_id, emp_name, gender, age, hire_date)
values(2, 'Webb', 'Man', 44, '2018-01-01');
insert into emp03(emp_id, emp_name, gender, age, hire_date)
values(3, 'Lin', 'Woman', 24, '2018-01-01');
insert into emp03(emp_id, emp_name, gender, age, hire_date)
values(4, 'Jamie', 'Woman', 54, '2018-01-01');
insert into emp03
values(5, 'July', 'Woman', 29, '2018-01-01', 'no');
-- COMMIT을 실행해 입력한 데이터 반영
commit;
delete from emp03 where emp_id = 5;
-- ROLLBACK 문을 실행해 DELETE 전 상태로 복귀
rollback;

select * from emp03;