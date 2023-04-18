-- 특정 기간동안 대여 가능한 자동차들의 대여비용 구하기
SELECT 
    H.CAR_ID,
    CAR_TYPE,
    ROUND(DAILY_FEE * ((100 - DISCOUNT_RATE) / 100) * 30) AS FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
INNER JOIN (
    SELECT CAR_ID, C.CAR_TYPE, DAILY_FEE, DISCOUNT_RATE
    FROM CAR_RENTAL_COMPANY_CAR AS C
    LEFT JOIN (
        SELECT CAR_TYPE, DISCOUNT_RATE
        FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
        WHERE DURATION_TYPE = '30일 이상'
    ) AS P
    ON C.CAR_TYPE = P.CAR_TYPE
    WHERE C.CAR_TYPE IN ('세단', 'SUV')
) AS C
ON H.CAR_ID = C.CAR_ID
WHERE H.CAR_ID NOT IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE END_DATE >= '2022-11-01' AND START_DATE <= '2022-11-30'
)
GROUP BY H.CAR_ID
HAVING FEE >= 500000 AND FEE < 2000000
ORDER BY FEE DESC, CAR_TYPE ASC, H.CAR_ID DESC