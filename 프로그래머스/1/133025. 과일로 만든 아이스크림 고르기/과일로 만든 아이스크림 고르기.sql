-- 코드를 입력하세요
SELECT
    a.FLAVOR

FROM
    FIRST_HALF AS a
JOIN
    ICECREAM_INFO AS b
ON a.FLAVOR = b.FLAVOR

WHERE
    b.INGREDIENT_TYPE = 'fruit_based'
    AND a.TOTAL_ORDER > 3000

ORDER BY
    a.TOTAL_ORDER DESC