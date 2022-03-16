-- https://programmers.co.kr/learn/courses/30/lessons/59044
-- ORACLE
/*
limit n : n개의 행을 출력한다.
limit n offset m : n개의 행을 출력하며, m번째 행으로 시작 위치를 정한다.
fetch (first n) row only : 첫번째 n개의 행을 출력한다.
offset m rows fetch (first n) row only : n개의 행을 출력하며, m번째 행으로 시작 위치를 정한다.
*/

SELECT
    i.NAME,
    i.DATETIME
FROM ANIMAL_INS i
    LEFT JOIN ANIMAL_OUTS o
    ON i.ANIMAL_ID = o.ANIMAL_ID
WHERE o.ANIMAL_ID IS NULL
ORDER BY 2
FETCH FIRST 3 ROW ONLY
;