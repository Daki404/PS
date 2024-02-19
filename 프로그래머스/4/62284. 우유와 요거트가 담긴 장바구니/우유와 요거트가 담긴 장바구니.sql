-- 코드를 입력하세요
SELECT
    CART_ID

FROM
    CART_PRODUCTS

WHERE
    (CART_ID, 'Milk') IN(
        SELECT CART_ID, NAME
        FROM CART_PRODUCTS
    ) AND
    (CART_ID, 'Yogurt') IN(
        SELECT CART_ID, NAME
        FROM CART_PRODUCTS
    )

GROUP BY
    CART_ID

ORDER BY
    CART_ID