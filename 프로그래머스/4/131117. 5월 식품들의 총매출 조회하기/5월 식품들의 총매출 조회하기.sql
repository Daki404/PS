SELECT
    a.PRODUCT_ID,
    PRODUCT_NAME,
    (AMOUNT * PRICE) AS TOTAL_SALES

FROM
    FOOD_PRODUCT AS a
JOIN
    (
        SELECT
            PRODUCT_ID,
            SUM(AMOUNT) AS AMOUNT,
            PRODUCE_DATE
        FROM
            FOOD_ORDER
        WHERE
            YEAR(PRODUCE_DATE) = '2022'
            AND MONTH(PRODUCE_DATE) = '5'
        GROUP BY
            PRODUCT_ID
    ) AS b
ON a.PRODUCT_ID = b.PRODUCT_ID


ORDER BY
    TOTAL_SALES DESC,
    a.PRODUCT_ID
