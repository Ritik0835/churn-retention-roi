CREATE TABLE IF NOT EXISTS customer_scores (
    customer_id TEXT PRIMARY KEY,
    churn_probability NUMERIC(8,7) NOT NULL
        CHECK (churn_probability BETWEEN 0 AND 1),
    actual_churn SMALLINT NOT NULL
        CHECK (actual_churn IN (0, 1)),
    monthly_charges NUMERIC(10,2) NOT NULL
        CHECK (monthly_charges >= 0)
);
