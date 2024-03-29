-- 자동차 대여 기록 별 금액 구하기
WITH duration AS (
    SELECT 
        HISTORY_ID,
        H.CAR_ID,
        CAR_TYPE,
        DAILY_FEE,
        DATEDIFF(END_DATE, START_DATE) + 1 AS DATES,
        CASE
            WHEN DATEDIFF(END_DATE, START_DATE) + 1 < 7 THEN 0
            WHEN DATEDIFF(END_DATE, START_DATE) + 1 < 30 THEN '7일 이상'
            WHEN DATEDIFF(END_DATE, START_DATE) + 1 < 90 THEN '30일 이상'
            ELSE '90일 이상'
        END AS DURATION_TYPE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
    INNER JOIN CAR_RENTAL_COMPANY_CAR AS C
    ON H.CAR_ID = C.CAR_ID
    WHERE CAR_TYPE = '트럭'
)

SELECT 
    HISTORY_ID,
    ROUND(DATES*DAILY_FEE*(100-(COALESCE(DISCOUNT_RATE, 0)))/100) AS FEE
FROM duration AS D
LEFT JOIN (
    SELECT DURATION_TYPE, DISCOUNT_RATE
    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    WHERE CAR_TYPE = '트럭'
) AS P ON D.DURATION_TYPE = P.DURATION_TYPE
ORDER BY FEE DESC, HISTORY_ID DESC

-- 추가) 다른 접근 방식
-- WITH duration AS (
--     SELECT 
--         HISTORY_ID,
--         H.CAR_ID,
--         CAR_TYPE,
--         DAILY_FEE,
--         DATEDIFF(END_DATE, START_DATE) + 1 AS DATES
--     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
--     INNER JOIN CAR_RENTAL_COMPANY_CAR AS C
--     ON H.CAR_ID = C.CAR_ID
-- )

-- SELECT 
--     HISTORY_ID,
--     ROUND(DATES*DAILY_FEE*(100-(COALESCE(DISCOUNT_RATE, 0)))/100) AS FEE
-- FROM duration AS A
-- LEFT JOIN (
--     SELECT CAR_TYPE, DURATION_TYPE, DISCOUNT_RATE
--     FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
-- ) AS P
-- ON A.CAR_TYPE = P.CAR_TYPE AND REPLACE(P.DURATION_TYPE, '일 이상', '') <= A.DATES
-- WHERE A.CAR_TYPE = '트럭'
-- GROUP BY HISTORY_ID
-- ORDER BY FEE DESC, HISTORY_ID DESC