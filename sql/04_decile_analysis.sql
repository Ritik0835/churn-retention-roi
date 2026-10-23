WITH scored_customers AS (
    SELECT
        customer_id,
        actual_churn,
        churn_probability,
        NTILE(10) OVER (
            ORDER BY churn_probability DESC, customer_id
        ) AS decile
    FROM customer_scores
)
SELECT
    decile,
    COUNT(*) AS customers,
    SUM(actual_churn) AS actual_churners,
    ROUND(
        100.0 * SUM(actual_churn) / COUNT(*),
        2
    ) AS churn_rate_pct
FROM scored_customers
GROUP BY decile
ORDER BY decile;
