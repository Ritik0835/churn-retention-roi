# Retention Strategy Comparison

## Objective

Compare three retention strategies using the same 1,409-customer
test set and the same base-case assumptions.

## Assumptions

- Offer cost: $10 per targeted customer
- Offer success rate: 20%
- Months of revenue kept: 6
- Value kept: MonthlyCharges × 6
- MonthlyCharges is a revenue proxy, not verified profit.

## Results

| Strategy | Customers Targeted | Expected Revenue Kept | Offer Cost | Net Expected Value |
|---|---:|---:|---:|---:|
| Target everyone | 1,409 | 33,129.24 | 14,090.00 | 19,039.24 |
| Top 20% by churn probability | 282 | 17,626.65 | 2,820.00 | 14,806.65 |
| Top 20% by expected value | 282 | 18,744.23 | 2,820.00 | 15,924.23 |

All monetary values use the dataset's currency convention.

## Interpretation

- Targeting everyone produces the highest total estimated net value,
  but requires substantially more spending.
- Under the same targeted-customer budget, selecting customers by
  expected value produces $1,117.58 more estimated net value than
  selecting them by churn probability alone.
- Expected-value targeting considers both churn probability and
  monthly charges, so it prioritizes customers with higher estimated
  value to retain.

## Limitations

- These are model-based estimates, not observed campaign results.
- The assumed offer success rate is not experimentally validated.
- Monthly charges are not contribution margin or verified profit.
- The model does not prove that an offer causes retention.
- Actual campaign performance should be tested before deployment.

