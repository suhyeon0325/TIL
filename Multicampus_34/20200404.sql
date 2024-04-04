-- p192 
-- UK Commerce 데이터를 이용한 리포트 작성

-- p.194
-- 국가별, 상품별 구매자 수 및 매출액 
USE mydata;
SELECT * FROM dataset3;

SELECT 
	country
    , stockcode
    , COUNT(DISTINCT customerid) BU 
    , SUM(quantity * unitprice) SALES 
FROM dataset3
GROUP BY 1, 2
ORDER BY 3 DESC, 4 DESC
;

-- 특정 상품 구매자가 가장 많이 구매한 상품은?
-- 장바구니 분석 
-- 예: 맥주를 구매할 경우, 기저귀를 구매하는 경향이 있는지 없는지 연관성 파악

-- 1) 특정 상품을 구매한 구매자가 어떤 상품을 많이 구매하는지 살펴보자 
-- 가장 많이 판매된 Top2 상품을 모두 구매한 고객을 찾아보자. 
-- 이 고객군이 구매한 상품 코드를 조회한다! 

-- 2개 상품 조회 (MAX)
SELECT 
	* 
    , ROW_NUMBER() OVER(ORDER BY QTY DESC) RNK
FROM (
	SELECT 
		stockcode
		, SUM(quantity) QTY 
	FROM dataset3
	GROUP BY 1
) A
;

-- 1, 2인 데이터만 조회하자. 
SELECT 
	stockcode
FROM (
	SELECT 
		* 
		, ROW_NUMBER() OVER(ORDER BY QTY DESC) RNK
	FROM (
		SELECT 
			stockcode
			, SUM(quantity) QTY 
		FROM dataset3
		GROUP BY 1
	) A
) A
WHERE RNK BETWEEN 1 AND 2
;

-- 84077, 85123A
-- 2개 상품을 모두 구매한 고객번호가 뭘까? 
DESC dataset3;

SELECT DISTINCT customerID 
FROM dataset3
WHERE stockcode = '84077'
	AND stockcode = '85123A'
;

SELECT DISTINCT customerID 
FROM dataset3
WHERE stockcode IN ('84077', '85123A')
;

SELECT customerID 
FROM dataset3
GROUP BY 1
HAVING MAX(CASE WHEN stockcode = '84077' THEN 1 ELSE 0 END) = 1
	AND MAX(CASE WHEN stockcode = '85123A' THEN 1 ELSE 0 END) = 1
; -- 13488, 14669, 14911, 17211

SELECT * FROM dataset3;

SELECT DISTINCT a.customerID
FROM 
  (SELECT customerID FROM dataset3 WHERE stockcode = '84077') a
JOIN 
  (SELECT customerID FROM dataset3 WHERE stockcode = '85123A') b
ON a.customerID = b.customerID
ORDER BY 1
; -- 13488, 14669, 14911, 17211

-- 테이블생성 
CREATE TABLE mydata.BU_LIST AS 
SELECT customerID 
FROM dataset3
GROUP BY 1
HAVING MAX(CASE WHEN stockcode = '84077' THEN 1 ELSE 0 END) = 1
	AND MAX(CASE WHEN stockcode = '85123A' THEN 1 ELSE 0 END) = 1
;

SELECT DISTINCT stockcode 
FROM dataset3
WHERE customerID IN (SELECT customerID FROM BU_LIST)
	AND stockcode NOT IN ('84077', '85123A')
;

-- 국가별 재구매율 계산 
SELECT 
	A.COUNTRY,
	SUBSTR(A.INVOICEDATE,1,4) YY,
	COUNT(DISTINCT B.CUSTOMERID) / COUNT(DISTINCT A.CUSTOMERID) RETENTION_RATE
FROM (
	SELECT DISTINCT COUNTRY,
	INVOICEDATE,
	CUSTOMERID
	FROM MYDATA.DATASET3) A
LEFT JOIN (SELECT DISTINCT COUNTRY,
	INVOICEDATE,
	CUSTOMERID
	FROM MYDATA.DATASET3
) B
ON SUBSTR(A.INVOICEDATE,1,4) = SUBSTR(B.INVOICEDATE,1,4) -1
AND A.COUNTRY = B.COUNTRY
AND A.CUSTOMERID = B.CUSTOMERID
GROUP BY 1,2
ORDER BY 1,2;

SELECT 
	*
FROM (
	SELECT DISTINCT COUNTRY,
	INVOICEDATE,
	CUSTOMERID
	FROM MYDATA.DATASET3) A
LEFT JOIN (SELECT DISTINCT COUNTRY,
	INVOICEDATE,
	CUSTOMERID
	FROM MYDATA.DATASET3
) B
ON SUBSTR(A.INVOICEDATE,1,4) = SUBSTR(B.INVOICEDATE,1,4) -1
AND A.COUNTRY = B.COUNTRY
AND A.CUSTOMERID = B.CUSTOMERID
;
-- GROUP BY 1,2
-- ORDER BY 1,2;

-- 202p
-- 코호트 분석
-- 실무적 : SQL에서 코호트 분석 쿼리를 작성하는 것 보다는
--        차라리, Python, R, Tableau 활용해서 시각화로 결과 도출하기 
--        엑셀 코호트 분석 


-- 첫 구매월을 기준으로 각 그룹 간의 패턴을 파악해본다. 
-- 먼저 고객별로 첫 구매일을 구한다. 
SELECT 
	customerid
    , MIN(invoicedate) MNDT 
FROM dataset3
GROUP BY 1
;

-- 각 고객의 주문일자, 구매액을 조회
SELECT 
	customerid
    , invoicedate
    , unitprice * quantity sales
FROM dataset3
;

SELECT * FROM (
	SELECT 
		customerid
		, MIN(invoicedate) MNDT 
	FROM dataset3
	GROUP BY 1) A 
LEFT JOIN (SELECT 
	customerid
    , invoicedate
    , unitprice * quantity sales
FROM dataset3) B
ON A.customerid = B.customerid
;

-- 구매월을 기준으로 코호트분석
-- MNDT는 각 고객의 최초 구매월 의미
-- DATEDIFF 첫 구매 이후, 몇 개월 뒤에 구매가 이루어졌는지 기간
-- SALES : 

SELECT 
	SUBSTR(MNDT, 1, 7) MM
    , TIMESTAMPDIFF(MONTH, MNDT, INVOICEDATE) DATEDIFF
    , COUNT(DISTINCT A.customerid) BU
    , SUM(SALES) SALES
FROM (
	SELECT 
		customerid
		, MIN(invoicedate) MNDT 
	FROM dataset3
	GROUP BY 1) A 
LEFT JOIN (SELECT 
	customerid
    , invoicedate
    , unitprice * quantity sales
FROM dataset3) B
ON A.customerid = B.customerid
GROUP BY 1, 2
;

-- 고객 세그먼트 (RFM)
-- 타겟 마케팅 : 세대별 / 연령별

-- Recency : 거래의 최근성을 나타내는 지표
-- p.207
SELECT 
	customerid
    , MAX(invoiceDate) MXDT 
FROM dataset3
GROUP BY 1
;

SELECT MAX(invoiceDate) FROM dataset3; -- 마지막 구매일 2011-12-01

-- 이후 2011-12-02로부터의 Timer Interval을 계산한다. 
SELECT 
	customerid
    , DATEDIFF('2011-12-02', MXDT) RECENCY
FROM (
	SELECT 
		customerid
		, MAX(invoiceDate) MXDT 
	FROM dataset3
	GROUP BY 1
) A
;

-- Frequency는 구매 건수
-- Monetary는 구매 금액
SELECT 
	customerid
    , COUNT(DISTINCT invoiceNo) FREQUENCY
    , SUM(quantity * unitprice) Monetary
FROM dataset3
GROUP BY 1
;

select customerid,
datediff('2011-12-02',mxdt) Recency,
Frequency,
Monetary
from
(select customerid,
max(invoiceDate) mxdt,
count(distinct InvoiceNo) Frequency,
sum(Quantity*UnitPrice) Monetary
from mydata.dataset3
group
by 1) a
;

-- 재구매 Segment
-- 동일한 상품을 2개 연도에 걸쳐서 구매한 고객과 그렇지 않은 고객 나누자. 
-- 예) A라는 상품을 2010년도, 2011년도에 걸쳐 구매한 고객 
--    vs. A라는 상품을 특정 연도에만 구매한 고객으로 나눌 수 있느냐? 


-- 고객별, 상품별 구매 연도를 Unique 하게 카운트 
SELECT 
	customerid
    , stockcode
    , COUNT(DISTINCT SUBSTR(invoiceDate, 1, 4)) UNIQUE_YY 
FROM dataset3
GROUP BY 1, 2
;


-- UNIQUE_YY가 2 이상인 고객, 그렇지 않은 고객으로 구분하자. 
SELECT 
	customerid
    , MAX(UNIQUE_YY) mx_unique_yy
FROM (
	SELECT 
		customerid
		, stockcode
		, COUNT(DISTINCT SUBSTR(invoiceDate, 1, 4)) UNIQUE_YY 
	FROM dataset3
	GROUP BY 1, 2
) A 
GROUP BY 1
;


-- mx_unique_yy가 2 이상인 경우는 1, 그렇지 않은 경우는 0으로 설정
-- CASE WHEN 
SELECT 
	customerid
    , CASE WHEN mx_unique_yy >= 2 THEN 1 else 0 END repurchase_seqment
FROM (
	SELECT 
		customerid
		, MAX(UNIQUE_YY) mx_unique_yy
	FROM (
		SELECT 
			customerid
			, stockcode
			, COUNT(DISTINCT SUBSTR(invoiceDate, 1, 4)) UNIQUE_YY 
		FROM dataset3
		GROUP BY 1, 2
	) A 
	GROUP BY 1
) A 
GROUP BY 1
;


-- repurchase_segment가 1인 고객만 조회하기
SELECT 
	customerid
    , CASE WHEN mx_unique_yy >= 2 THEN 1 else 0 END repurchase_seqment
FROM (
	SELECT 
		customerid
		, MAX(UNIQUE_YY) mx_unique_yy
	FROM (
		SELECT 
			customerid
			, stockcode
			, COUNT(DISTINCT SUBSTR(invoiceDate, 1, 4)) UNIQUE_YY 
		FROM dataset3
		GROUP BY 1, 2
	) A 
	GROUP BY 1
) A 
GROUP BY 1
;

-- 분석하는 사람들 : 쿼리 성능을 고려할 필요가 없음
-- DBA or 백엔드 개발자 (실제 서비스 DB 만드는 사람들) : 쿼리 성능 체크하자!!
-- 경험치 + 경력
SELECT customerid
FROM (
	SELECT 
		customerid
		, CASE WHEN mx_unique_yy >= 2 THEN 1 else 0 END repurchase_segment
	FROM (
		SELECT 
			customerid
			, MAX(UNIQUE_YY) mx_unique_yy
		FROM (
			SELECT 
				customerid
				, stockcode
				, COUNT(DISTINCT SUBSTR(invoiceDate, 1, 4)) UNIQUE_YY 
			FROM dataset3
			GROUP BY 1, 2
		) A 
		GROUP BY 1
	) A 
	GROUP BY 1
) A
WHERE repurchase_segment = 1
;










