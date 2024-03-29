-- 자동차 대여 기록에서 대여중 / 대여 가능 여부 구분하기
WITH INFO AS (
    SELECT 
        DISTINCT(CAR_ID) AS CAR_ID,
        IF (START_DATE <= '2022-10-16' AND END_DATE >= '2022-10-16', '대여중', '대여 가능') AS AVAILABILITY
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE <= '2022-10-16' AND END_DATE >= '2022-10-16'
)

SELECT 
    H.CAR_ID,
    COALESCE(AVAILABILITY, '대여 가능') AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
LEFT JOIN INFO AS I
ON H.CAR_ID = I.CAR_ID
GROUP BY H.CAR_ID
ORDER BY H.CAR_ID DESC