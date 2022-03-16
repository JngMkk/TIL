-- https://programmers.co.kr/learn/courses/30/lessons/62284
-- ORACLE

SELECT a.CART_ID
FROM CART_PRODUCTS a, CART_PRODUCTS b
WHERE
    a.CART_ID = b.CART_ID
    AND a.NAME = 'Milk'
    AND b.NAME = 'Yogurt'
ORDER BY 1
;