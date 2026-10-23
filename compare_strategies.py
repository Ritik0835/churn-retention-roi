
import math
import pandas as pd

# Load the validated test-set scores
df = pd.read_csv("data/scores.csv")

# Base-case assumptions from docs/assumptions.md
OFFER_COST = 10.0
SAVE_RATE = 0.20
MONTHS_KEPT = 6

# MonthlyCharges is a revenue proxy, not verified profit
df["value_kept"] = df["MonthlyCharges"] * MONTHS_KEPT

# Expected net value per targeted customer
df["expected_value"] = (
    df["churn_probability"] * SAVE_RATE * df["value_kept"]
    - OFFER_COST
)

# Select the top 20%, rounding up to a whole customer
top_n = math.ceil(len(df) * 0.20)

strategies = {
    "Target everyone": df.copy(),
    "Top 20% by churn probability": (
        df.nlargest(top_n, "churn_probability").copy()
    ),
    "Top 20% by expected value": (
        df.nlargest(top_n, "expected_value").copy()
    ),
}

results = []

for strategy, targeted in strategies.items():
    expected_saved = (
        targeted["churn_probability"] * SAVE_RATE
    ).sum()

    expected_revenue_kept = (
        targeted["churn_probability"]
        * SAVE_RATE
        * targeted["value_kept"]
    ).sum()

    offer_cost_total = len(targeted) * OFFER_COST
    net_expected_value = expected_revenue_kept - offer_cost_total

    results.append({
        "strategy": strategy,
        "customers_targeted": len(targeted),
        "targeted_share_pct": round(
            len(targeted) / len(df) * 100, 2
        ),
        "expected_customers_saved": round(expected_saved, 2),
        "expected_revenue_kept_proxy": round(
            expected_revenue_kept, 2
        ),
        "offer_cost_total": round(offer_cost_total, 2),
        "net_expected_value": round(net_expected_value, 2),
    })

comparison = pd.DataFrame(results)
comparison.to_csv("data/strategy_comparison.csv", index=False)

print(f"Test-set customers: {len(df)}")
print(f"Customers in top 20%: {top_n}")
print(f"Assumptions: save rate={SAVE_RATE:.0%}, "
      f"months kept={MONTHS_KEPT}, offer cost=${OFFER_COST:.2f}")
print("\nStrategy comparison:")
print(comparison.to_string(index=False))
print("\nSaved: data/strategy_comparison.csv")
