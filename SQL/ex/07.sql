-- https://programmers.co.kr/learn/courses/30/lessons/59045
-- ORACLE

SELECT
    i.ANIMAL_ID,
    i.ANIMAL_TYPE,
    i.NAME
FROM ANIMAL_INS i
    JOIN ANIMAL_OUTS o
    ON i.ANIMAL_ID = o.ANIMAL_ID
WHERE SEX_UPON_INTAKE LIKE 'Intact%'
    AND (SEX_UPON_OUTCOME LIKE 'Spayed%' OR SEX_UPON_OUTCOME LIKE 'Neutered%')
ORDER BY 1
;