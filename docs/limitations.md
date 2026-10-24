# Limitations and Next Steps

## 1. No Randomized Holdout Experiment

This project estimates the potential financial value of targeting customers at risk of churn. However, no randomized holdout or control group was used to measure the actual impact of retention offers.

Customers who receive an offer may still churn, while customers who receive no offer may stay anyway. Therefore, the estimated net value is a scenario-based projection, not proven incremental profit.

## 2. Uplift Modeling Is the Next Step

Churn prediction estimates which customers are likely to leave. It does not tell us which customers will change their behavior because of a retention offer.

The next step is to run a randomized retention experiment and collect treatment and control outcomes. With sufficient data, uplift modeling can estimate the incremental effect of an offer and help prioritize customers most likely to be retained because of the intervention.

## 3. All Business Inputs Are Assumptions

The offer cost, offer success rate, and retention period are illustrative assumptions rather than experimentally measured business results. Different values can materially change estimated net profit.

Monthly charges are used as a proxy for monthly revenue. They do not represent verified profit, contribution margin, or realized revenue retained. The analysis does not include all potential costs, discounts, or downstream customer behavior.

## 4. Model and Dataset Limitations

The analysis uses a held-out test set from the existing churn model. Its predictions and observed churn outcomes support ranking and evaluation, but they do not establish that a retention intervention will work.

Results may also change across customer populations, time periods, and business conditions. Model calibration and performance should be monitored before operational deployment.

## 5. Recommended Next Steps

1. Run a randomized retention-offer experiment with treatment and control groups.
2. Measure incremental retention, revenue, and profit.
3. Replace illustrative assumptions with observed offer costs and outcomes.
4. Explore uplift modeling when sufficient experimental data is available.
5. Validate the strategy on newer customer data before deployment.

**Conclusion:** This project is a decision-support and scenario-analysis prototype. Its financial estimates help compare targeting strategies under stated assumptions, but actual incremental profit remains unknown until measured experimentally.
