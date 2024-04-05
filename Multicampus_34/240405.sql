-- p.213
-- 일자별 첫 구매자수 
USE mydata;
SELECT * FROM dataset3;

-- 고객별 첫 구매일 
SELECT 
	customerid
    , MIN(invoicedate) MNDT 
FROM dataset3
GROUP BY customerid
;

-- 일자별 첫 구매 고객 수
SELECT 
	MNDT
    , COUNT(DISTINCT customerid) BU
FROM (
	SELECT 
		customerid
		, MIN(invoicedate) MNDT 
	FROM dataset3
	GROUP BY customerid
) A 
GROUP BY 1 
;


-- 상품별 첫 구매 고객 수
-- (1) 고객별, 상품별 첫 구매일자 
SELECT 
	customerid
    , stockcode
    , MIN(invoicedate) MNDT 
FROM dataset3
GROUP BY 1, 2
;

-- (2) 고객별 구매와 기준 순위 생성 (랭크) 
SELECT 
	* 
    , ROW_NUMBER() OVER(PARTITION BY customerid ORDER BY MNDT) RNK
FROM (
	SELECT 
		customerid
		, stockcode
		, MIN(invoicedate) MNDT 
	FROM dataset3
	GROUP BY 1, 2
) A
;
-- (a) 고객별 첫 구매 내역 조회
-- 순위 열의 값이 1이(고객별 최초 구매 내역) 조건을 생성! 
SELECT * 
FROM (
	SELECT 
		* 
		, ROW_NUMBER() OVER(PARTITION BY customerid ORDER BY MNDT) RNK
	FROM (
		SELECT 
			customerid
			, stockcode
			, MIN(invoicedate) MNDT 
		FROM dataset3
		GROUP BY 1, 2
	) A
) A 
WHERE RNK = 1
;

-- (b) 상품별 첫 구매 고객 수 집계
SELECT 
	stockcode
    , COUNT(DISTINCT customerid) first_bu
FROM (
	SELECT * 
	FROM (
		SELECT 
			* 
			, ROW_NUMBER() OVER(PARTITION BY customerid ORDER BY MNDT) RNK
		FROM (
			SELECT 
				customerid
				, stockcode
				, MIN(invoicedate) MNDT 
			FROM dataset3
			GROUP BY 1, 2
		) A
	) A 
	WHERE RNK = 1
) A
GROUP BY stockcode
ORDER BY 2 DESC
;

-- 첫 구매 후 이탈하는 고객의 비중 (전체 데이터 기준)
-- 첫 구매 후 이탈해 버린 고객의 데이터 확인
-- 동일한 날짜에 2번 이상 주문하고 이탈한 경우도 이탈 고객으로 체크 
SELECT 
	customerid
	, COUNT(DISTINCT invoicedate) F_DATE
FROM dataset3
GROUP BY 1;


SELECT 
	SUM(CASE WHEN F_DATE = 1 THEN 1 ELSE 0 END) / SUM(1) BOUNCE_RATE
FROM (
	SELECT 
		customerid
		, COUNT(DISTINCT invoicedate) F_DATE
	FROM dataset3
	GROUP BY 1
) A 
;

-- 국가별 이탈율 구하기
SELECT 
	country
	, SUM(CASE WHEN F_DATE = 1 THEN 1 ELSE 0 END) / SUM(1) BOUNCE_RATE
FROM (
	SELECT 
		customerid
        , country
		, COUNT(DISTINCT invoicedate) F_DATE
	FROM dataset3
	GROUP BY 1, 2
) A 
GROUP BY country
ORDER BY country
;

-- p.223 
-- 판매 수량이 20% 이상 증가한 상품 리스트
-- 데이터 세트의 판매기간 

SELECT DISTINCT SUBSTR(invoicedate, 1, 4) YY
FROM dataset3
;

-- 2010년 대비 2011년에 판매 수량이 20% 이상 증가한 상품을 찾자
-- 연도별, 상품별 판매 수량을 계산해보자 

SELECT * FROM dataset3;

-- 2011년도 상품별 판매 수량 
SELECT 
	stockcode
    , SUM(quantity) QTY
FROM dataset3
WHERE SUBSTR(invoicedate, 1, 4) = '2011'
GROUP BY 1
;

-- 2010년도 상품별 판매 수량 
SELECT 
	stockcode
    , SUM(quantity) QTY
FROM dataset3
WHERE SUBSTR(invoicedate, 1, 4) = '2010'
GROUP BY 1
;

SELECT 
	A.stockcode
    , A.QTY QTY_2011
    , B.QTY QTY_2010
    , A.QTY / B.QTY AS QTY_INCREASE_RATE
FROM (
	SELECT 
		stockcode
		, SUM(quantity) QTY
	FROM dataset3
	WHERE SUBSTR(invoicedate, 1, 4) = '2011'
	GROUP BY 1
) A 
LEFT JOIN (
	SELECT 
		stockcode
		, SUM(quantity) QTY
	FROM dataset3
	WHERE SUBSTR(invoicedate, 1, 4) = '2010'
	GROUP BY 1
) B
ON A.stockcode = B.stockcode
;

-- 판매량이 20% 이상 증가한 것 
SELECT * 
FROM (
	SELECT 
		A.stockcode
		, A.QTY QTY_2011
		, B.QTY QTY_2010
		, A.QTY / B.QTY - 1 AS QTY_INCREASE_RATE
	FROM (
		SELECT 
			stockcode
			, SUM(quantity) QTY
		FROM dataset3
		WHERE SUBSTR(invoicedate, 1, 4) = '2011'
		GROUP BY 1
	) A 
	LEFT JOIN (
		SELECT 
			stockcode
			, SUM(quantity) QTY
		FROM dataset3
		WHERE SUBSTR(invoicedate, 1, 4) = '2010'
		GROUP BY 1
	) B
	ON A.stockcode = B.stockcode
) BASE 
WHERE QTY_INCREASE_RATE >= 0.2
ORDER BY 4 ASC
;

-- 모니터링 주기 일, 주, 월, 분기 
-- 주차별 매출액 파악을 하자
-- WEEKOFYEAR 메서드

-- 해당 함수를 이용해 2011년 주차별 매출액을 계산해보자!! 
SELECT 
	WEEKOFYEAR(invoicedate) WK
	, SUM(quantity * unitprice) SALES
FROM
	dataset3
WHERE 
	SUBSTR(invoicedate, 1, 4) = '2011'
GROUP BY 1
ORDER BY 1
;

-- 신규/기존 고객의 2011년 월별 매출액
-- (1) 최초 구매 연도가 2011년이면 신규(NEW) / 2010년이면 기존 고객(EXI)
SELECT 
	CASE WHEN SUBSTR(MNDT, 1, 4) = '2011' THEN 'NEW' ELSE 'EXI' 
    END NEW_EXI
    , customerid
FROM 
	(SELECT 
		customerid
        , MIN(invoicedate) MNDT
	 FROM dataset3
     GROUP BY 1
    ) A 
;

-- (2) 해당 테이블을 매출 테이블(dataset3)에 join
SELECT 
	A.customerid
    , B.new_exi
    , A.invoicedate
    , A.unitprice
    , A.quantity
FROM 
	dataset3 A
LEFT JOIN (
	SELECT 
		CASE WHEN SUBSTR(MNDT, 1, 4) = '2011' THEN 'NEW' ELSE 'EXI' 
		END NEW_EXI
		, customerid
	FROM 
		(SELECT 
			customerid
			, MIN(invoicedate) MNDT
		 FROM dataset3
		 GROUP BY 1
		) A 
) B
ON A.customerid = B.customerid
WHERE SUBSTR(A.invoicedate, 1, 4) = '2011'
;

-- (3) 최종 집계
CREATE TABLE mydata.result AS 
SELECT 
    B.new_exi
    , SUBSTR(A.invoicedate, 1, 7) MM
    , SUM(A.unitprice * A.quantity) SALES
FROM 
	dataset3 A
LEFT JOIN (
	SELECT 
		CASE WHEN SUBSTR(MNDT, 1, 4) = '2011' THEN 'NEW' ELSE 'EXI' 
		END NEW_EXI
		, customerid
	FROM 
		(SELECT 
			customerid
			, MIN(invoicedate) MNDT
		 FROM dataset3
		 GROUP BY 1
		) A 
) B
ON A.customerid = B.customerid
WHERE SUBSTR(A.invoicedate, 1, 4) = '2011'
GROUP BY 1, 2
;





