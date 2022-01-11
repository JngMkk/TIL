create table emp_master(
    emp_id number not null,             -- 사원번호
    emp_name varchar2(100) not null,    -- 사원 명
    gender varchar2(10),                -- 성별
    age number,                         -- 나이
    hire_date date,                     -- 입사일자
    dept_id number,                     -- 부서아이디
    address_id number,                  -- 주소아이디
    constraint emp_master_pk primary key (emp_id)
);

create table dept_master(
    dept_id number not null,            -- 부서아이디
    dept_name varchar2(50),             -- 부서 명
    use_yn varchar(2) default 'Y',      -- 사용여부
    -- default 'Y' : 값을 넣지 않아도 자동으로 'Y'값을 넣어줌
    dept_desc varchar2(100),            -- 부서설명
    constraint dept_master_pk primary key (dept_id)
);

create table address_master(
    address_id number not null,         -- 주소아이디
    city varchar2(100),                 -- 도시 명
    gu varchar2(50),                    -- 구 명
    address_name varchar2(100),         -- 나머지 주소
    constraint address_master_pk primary key (address_id)
);

INSERT INTO emp_master ( emp_id, emp_name, gender, age, hire_date, dept_id, address_id )
VALUES (1, '김유신', '남성', 56, TO_DATE('2018-01-01', 'YYYY-MM-DD'), 1, 1);

INSERT INTO emp_master ( emp_id, emp_name, gender, age, hire_date, dept_id, address_id )
VALUES (2, '신사임당', '여성', 34, TO_DATE('2018-01-01', 'YYYY-MM-DD'), 1, 2);

INSERT INTO emp_master ( emp_id, emp_name, gender, age, hire_date, dept_id, address_id )
VALUES (3, '홍길동', '남성', 45, TO_DATE('2018-01-01', 'YYYY-MM-DD'), 3, 2);

INSERT INTO emp_master ( emp_id, emp_name, gender, age, hire_date, dept_id, address_id )
VALUES (4, '강감찬', '남성', 23, TO_DATE('2018-01-01', 'YYYY-MM-DD'), 2, 3);

INSERT INTO emp_master ( emp_id, emp_name, gender, age, hire_date, dept_id, address_id )
VALUES (5, '세종대왕', '남성', 45, TO_DATE('2018-01-01', 'YYYY-MM-DD'), 4, 4);


INSERT INTO dept_master ( dept_id, dept_name )
VALUES (1, '회계팀');

INSERT INTO dept_master ( dept_id, dept_name )
VALUES (2, '경영팀');

INSERT INTO dept_master ( dept_id, dept_name )
VALUES (3, '전산팀');

INSERT INTO dept_master ( dept_id, dept_name )
VALUES (4, '마케팅팀');

INSERT INTO address_master ( address_id, city, gu, address_name )
VALUES (1, '서울특별시', '중구', '새문안로 12');

INSERT INTO address_master ( address_id, city, gu, address_name )
VALUES (2, '서울특별시', '서대문구', '연희로 15길');

INSERT INTO address_master ( address_id, city, gu, address_name )
VALUES (3, '서울특별시', '영등포구', '여의대로 99');

INSERT INTO address_master ( address_id, city, gu, address_name )
VALUES (4, '서울특별시', '강남구', '테헤란로 33');
commit;

select * from dept_master;

/*
내부 조인
WHERE 절에서 동등 연산자를 사용해 연결고리 컬럼, 즉 조인 컬럼을 비교하는 조인.
*/
select a.emp_id, a.emp_name, a.gender, a.age, a.dept_id,
        b.dept_id, b.dept_name, b.use_yn
        from emp_master a, dept_master b
        where a.dept_id = b.dept_id
        order by a.emp_id;

-- ANSI 구문 내부 조인
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
        and a.gender = '남성'
        order by a.emp_id;
        
select a.emp_id, a.emp_name, a.gender, a.age, a.dept_id,
        b.dept_id, b.dept_name, b.use_yn
        from emp_master a
        inner join dept_master b
        on a.dept_id = b.dept_id
        where a.gender = '남성'
        order by a.emp_id;
        
select a.emp_id, a.emp_name, a.gender, a.age,
        b.dept_id, b.dept_name, b.use_yn,
        c.address_id, c.city, c.address_name
        from emp_master a, dept_master b, address_master c
        where a.dept_id = b.dept_id
        and a.address_id = c.address_id
        and a.gender = '남성'
        order by a.emp_id;
        
select a.emp_id, a.emp_name, a.gender, a.age,
        b.dept_id, b.dept_name, b.use_yn,
        c.address_id, c.city, c.address_name
        from emp_master a
        inner join dept_master b
        on a.dept_id = b.dept_id
        inner join address_master c
        on a.address_id = c.address_id
        where a.gender = '남성'
        order by a.emp_id;
        
/*
외부 조인
내부 조인은 두 테이블에서 조인 컬럼 값이 같은 건을 조회하는데 반해,
외부 조인은 두 테이블 중 한 테이블의 조인 컬럼 값이 없더라도 없는 건까지 모두 포함해
조회하는 조인.
*/

insert into emp_master(emp_id, emp_name, gender, age, hire_date, dept_id, address_id)
values (6, '왕건', '남성', 35, to_date('2018-01-01', 'YYYY-MM-DD'), null, 4);

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
values (5, 'IT팀');
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
카티션 곱
WHERE 절에 조인 조건을 주지 않는 것을 말함.
두 테이블의 데이터를 기준으로 가능한 모든 조합의 데이터가 조회됨.
*/
SELECT a.emp_id, a.emp_name, a.gender, a.age, a.dept_id,
        b.dept_id, b.dept_name, b.use_yn
        from emp_master a, dept_master b
        order by a.emp_id;