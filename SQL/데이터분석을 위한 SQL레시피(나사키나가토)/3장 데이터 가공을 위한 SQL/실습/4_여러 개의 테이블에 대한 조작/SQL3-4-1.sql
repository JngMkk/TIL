DROP TABLE IF EXISTS app1_mst_users;
CREATE TABLE app1_mst_users (
    user_id varchar(255)
  , name    varchar(255)
  , email   varchar(255)
);

INSERT INTO app1_mst_users
VALUES
    ('U001', 'Joongmo'  , 'joongmo@example.com'  )
  , ('U002', 'Doeun', 'doeun@example.com')
;

DROP TABLE IF EXISTS app2_mst_users;
CREATE TABLE app2_mst_users (
    user_id varchar(255)
  , name    varchar(255)
  , phone   varchar(255)
);

INSERT INTO app2_mst_users
VALUES
    ('U001', 'Hyewon', '010-xxxx-xxxx')
  , ('U002', 'Heejung', '011-xxxx-xxxx')
;

-- UNION ALL 구문을 사용해 테이블을 세로로 결합하는 쿼리
SELECT 'app1' AS app_name, user_id, name, email FROM app1_mst_users
UNION ALL
SELECT 'app2' AS app_name, user_id, name, NULL AS email FROM app2_mst_users;