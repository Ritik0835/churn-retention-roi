-- 1. Overall customer and churn summary
SELECT
    COUNT(*) AS total_customers,
    SUM(actual_churn) AS actual_churned,
    ROUND(100.0 * AVG(actual_churn), 2) AS actual_churn_rate_pct,
    ROUND(100.0 * AVG(churn_probability), 2) AS avg_predicted_risk_pct
FROM customer_scores;

-- 2. Customers grouped by predicted risk
WITH risk_summary AS (
    SELECT
        CASE
            WHEN churn_probability >= 0.70 THEN 'High risk'
            WHEN churn_probability >= 0.40 THEN 'Medium risk'
            ELSE 'Low risk'
        END AS risk_segment,
        COUNT(*) AS customers,
        SUM(actual_churn) AS actual_churned,
        ROUND(AVG(churn_probability) * 100, 2) AS avg_risk_pct,
        ROUND(SUM(monthly_charges), 2) AS monthly_charges_proxy
    FROM customer_scores
    GROUP BY 1
)
SELECT *
FROM risk_summary
ORDER BY CASE risk_segment
    WHEN 'High risk' THEN 1
    WHEN 'Medium risk' THEN 2
    ELSE 3
END;

-- 3. Top 20 customers by predicted churn risk
SELECT
    customer_id,
    ROUND(churn_probability * 100, 2) AS predicted_risk_pct,
    actual_churn,
    monthly_charges
FROM customer_scores
ORDER BY churn_probability DESC
LIMIT 20;
