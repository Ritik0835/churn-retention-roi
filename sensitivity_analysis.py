import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/scores.csv")
OUTPUT_PATH = Path("data/sensitivity_table.csv")

MONTHS_RETAINED = 6
TARGET_SHARE = 0.20

SUCCESS_RATES = [0.10, 0.20, 0.30, 0.40, 0.50]
OFFER_COSTS = [5, 10, 15, 20, 25]

df = pd.read_csv(DATA_PATH)

required = {"customerID", "churn_probability", "MonthlyCharges"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {sorted(missing)}")

df = df.sort_values("churn_probability", ascending=False).copy()

top_n = int(len(df) * TARGET_SHARE + 0.999999)
df = df.head(top_n)

df["retained_revenue_proxy"] = (
    df["churn_probability"] * df["MonthlyCharges"] * MONTHS_RETAINED
)

rows = []

for success_rate in SUCCESS_RATES:
    row = {"success_rate_pct": int(success_rate * 100)}

    for offer_cost in OFFER_COSTS:
        expected_revenue_kept = (
            df["retained_revenue_proxy"].sum() * success_rate
        )
        total_offer_cost = len(df) * offer_cost
        net_profit = expected_revenue_kept - total_offer_cost

        row[f"cost_${offer_cost}"] = round(net_profit, 2)

    rows.append(row)

result = pd.DataFrame(rows)
result.to_csv(OUTPUT_PATH, index=False)

print(f"Customers targeted: {len(df)}")
print(f"Retention period: {MONTHS_RETAINED} months")
print("\nEstimated net profit sensitivity table:")
print(result.to_string(index=False))
print(f"\nSaved to: {OUTPUT_PATH}")
