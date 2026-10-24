# Business Memo: Customer Retention Offer Strategy

**To:** Business and Retention Team  
**Subject:** Prioritizing Retention Offers Using Churn Risk and Estimated Value

## Recommendation

Use churn risk and estimated offer value to prioritize customers for a controlled retention experiment. Do not deploy the model as a proven profit-maximization strategy until the offer's incremental effect has been measured.

## Who Gets the Offer?

The test dataset contains 1,409 customers, including 374 observed churners. Under the base scenario, prioritizing the top 20% by predicted churn risk selects 282 customers.

A separate expected-value analysis finds 766 customers with positive estimated value under the assumptions. The cumulative net-value curve reaches an estimated maximum of **$23,225.23** when those 766 customers are targeted. This is a scenario-based threshold, not a validated operational optimum.

## What Does It Cost?

For the top-20% risk strategy:

- Customers targeted: 282
- Assumed offer cost per customer: $10
- **Total offer cost: $2,820**

The base scenario assumes a 20% offer success rate and six months of retained monthly charges as the value horizon.

## What Does It Return?

Using monthly charges as a revenue proxy, the model estimates:

- Expected value before offer costs: $17,626.65
- Offer cost: $2,820
- **Estimated net value: $14,806.65**

These figures are derived from churn probabilities and assumed offer effectiveness. They are not realized revenue, verified profit, or a causal estimate of the offer's impact.

## How Sure Are We?

Confidence in actual incremental profit is **low because no randomized retention experiment has been conducted**. The analysis compares scenarios but cannot establish how many customers would stay because they received an offer.

The success rate, offer cost, and retention period are assumptions. Monthly charges do not account for contribution margin or all costs. Results also depend on model quality and whether the test population represents future customers.

## Next Steps

1. Run a randomized experiment with treatment and control groups.
2. Measure incremental retention and profit after offer costs.
3. Replace assumed success rates with observed outcomes.
4. Evaluate uplift modeling to identify customers whose behavior is most likely to change because of the offer.

**Decision:** Use this analysis to design and prioritize a pilot, not to claim proven retention ROI.
