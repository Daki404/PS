WITH tmp AS(
    SELECT CAR_ID,
    (CASE
        WHEN START_DATE <= '2022-10-16' AND END_DATE >= '2022-10-16' THEN '대여중'
        ELSE '대여 가능'
    END) AS AVAILABILITY

    FROM    
        CAR_RENTAL_COMPANY_RENTAL_HISTORY 
)

SELECT
    DISTINCT CAR_ID,
    CASE
        WHEN (CAR_ID, '대여중') IN (SELECT * FROM tmp) THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY

FROM
    tmp

ORDER BY
    CAR_ID DESC