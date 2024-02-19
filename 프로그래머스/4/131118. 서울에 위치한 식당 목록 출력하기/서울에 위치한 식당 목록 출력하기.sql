/*
인포에 리뷰 조인 때리고 아이디로 그룹 때리고 에버리지 스코어
웨어로 정규표현식 서울 필터링
*/
SELECT
    a.REST_ID,
    REST_NAME,
    FOOD_TYPE,
    FAVORITES,
    ADDRESS,
    ROUND(AVG(REVIEW_SCORE), 2) AS SCORE

FROM
    REST_INFO AS a
JOIN
    REST_REVIEW AS b
ON
    a.REST_ID = b.REST_ID

WHERE
    ADDRESS REGEXP('^서울')

GROUP BY
    a.REST_ID,
    REST_NAME,
    FOOD_TYPE,
    FAVORITES,
    ADDRESS

ORDER BY
    SCORE DESC