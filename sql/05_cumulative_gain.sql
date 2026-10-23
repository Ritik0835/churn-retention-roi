WITH decile_summary AS (
    SELECT
        NTILE(10) OVER (
            ORDER BY churn_probability DESC, customer_id
        ) AS decile,
        actual_churn
    FROM customer_scores
),
decile_counts AS (
    SELECT
        decile,
        COUNT(*) AS customers,
        SUM(actual_churn) AS actual_churners
    FROM decile_summary
    GROUP BY decile
)
SELECT
    decile,
    customers,
    actual_churners,
    SUM(actual_churners) OVER (
        ORDER BY decile
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_churners,
    ROUND(
        100.0 * SUM(actual_churners) OVER (
            ORDER BY decile
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) / SUM(actual_churners) OVER (),
        2
    ) AS cumulative_gain_pct
FROM decile_counts
ORDER BY decile;
