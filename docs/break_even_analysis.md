# Break-Even Success Rate Analysis

## Objective

Calculate the minimum retention-offer success rate required for the expected value of a retention campaign to break even.

## Assumptions

- Offer cost per targeted customer: $10
- Retention period: 6 months
- MonthlyCharges: used as a proxy for monthly revenue
- Churn probability: estimated by the churn prediction model

These are illustrative assumptions, not measured campaign results.

## Formula

The expected value per targeted customer is:

Expected Value = P(Churn) × Success Rate × MonthlyCharges × Months Retained − Offer Cost

At break-even, Expected Value = 0.

Therefore:

Break-Even Success Rate = Offer Cost / (P(Churn) × MonthlyCharges × Months Retained)

Multiply the result by 100 to express it as a percentage.

## Worked Example

Assume a customer has:

- Predicted churn probability: 0.80
- MonthlyCharges: $80
- Months retained: 6
- Offer cost: $10

Break-Even Success Rate = 10 / (0.80 × 80 × 6)

Break-Even Success Rate = 10 / 384

Break-Even Success Rate = 0.02604, or approximately **2.60%**.

Under these assumptions, the retention offer must successfully prevent churn for approximately 2.60% of comparable targeted customers to break even in expected value.

## Interpretation

- If the actual offer success rate is above the break-even rate, expected value is positive under this simplified model.
- If it is below the break-even rate, expected value is negative.
- Higher offer costs increase the break-even rate.
- Higher monthly charges, longer retention periods, or higher predicted churn probabilities reduce the break-even rate, all else being equal.

## Limitations

- Predicted churn probability is a model estimate, not a guarantee that a customer will churn.
- MonthlyCharges is a revenue proxy, not verified realized revenue or profit.
- The calculation assumes the retained revenue proxy can be attributed to the offer and does not subtract service costs.
- The true offer success rate must be measured using campaign outcomes.
- Results depend on the assumptions and should not be presented as proven campaign performance.
