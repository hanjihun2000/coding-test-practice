-- 오프라인/온라인 판매 데이터 통합하기
SELECT DATE_FORMAT(SALES_DATE, "%Y-%m-%d"), PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM (
    SELECT SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
    FROM ONLINE_SALE
    UNION ALL
    SELECT SALES_DATE, PRODUCT_ID, NULL, SALES_AMOUNT
    FROM OFFLINE_SALE
) AS D
WHERE MONTH(SALES_DATE) = 3
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID