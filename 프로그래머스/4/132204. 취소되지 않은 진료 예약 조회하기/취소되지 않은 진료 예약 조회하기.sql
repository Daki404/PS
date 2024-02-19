/*
삼중 조인 때려 박고
조건으로
CS 랑 날짜랑 취소 아닌거 오름차순 정렬 진료에약 일시
*/
SELECT
    APNT_NO,
    PT_NAME,
    a.PT_NO,
    a.MCDP_CD,
    DR_NAME,
    APNT_YMD

FROM
    APPOINTMENT AS a
JOIN
    PATIENT AS b
ON a.PT_NO = b.PT_NO
JOIN
    DOCTOR AS c
ON a.MDDR_ID = c.DR_ID

WHERE
    a.MCDP_CD = 'CS'
    AND APNT_CNCL_YN != 'Y'
    AND DATE_FORMAT(APNT_YMD, '%Y-%m-%d') = '2022-04-13'

ORDER BY
    APNT_YMD

