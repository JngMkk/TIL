-- https://programmers.co.kr/learn/courses/30/lessons/59041
-- ORACLE

SELECT
    NAME,
    COUNT(NAME) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) > 1
ORDER BY 1
;

SELECT ANIMAL_OUTS.ANIMAL_ID,ANIMAL_OUTS.NAME FROM ANIMAL_OUTS
LEFT JOIN ANIMAL_INS ON
ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
WHERE ANIMAL_INS.ANIMAL_ID IS NULL
ORDER BY ANIMAL_ID
;