-- https://programmers.co.kr/learn/courses/30/lessons/59413
-- ORACLE

WITH
TMP AS (
SELECT TO_NUMBER(TO_CHAR(DATETIME, 'HH24')) AS HOUR
FROM ANIMAL_OUTS
)
, TMP2 AS (
SELECT LEVEL-1 AS HOUR
FROM DUAL
CONNECT BY LEVEL <= 24
)
SELECT
    TT.HOUR,
    COALESCE(COUNT(T.HOUR), 0) AS COUNT
FROM TMP T
    RIGHT JOIN TMP2 TT
    ON T.HOUR = TT.HOUR
GROUP BY TT.HOUR
ORDER BY 1
;

SELECT
    HOUR,
    COUNT(*)-1 AS COUNT
FROM (SELECT LEVEL-1 AS HOUR
      FROM DUAL
      CONNECT BY LEVEL <= 24
      UNION ALL
      SELECT TO_NUMBER(TO_CHAR(DATETIME,'HH24')) AS HOUR
      FROM ANIMAL_OUTS) 
GROUP BY HOUR
ORDER BY 1
;