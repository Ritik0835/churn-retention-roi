
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Base-case assumptions
OFFER_COST = 10.0
SAVE_RATE = 0.20
MONTHS_KEPT = 6

# Load test-set scores
df = pd.read_csv("data/scores.csv")

# Calculate expected net value per targeted customer
df["value_kept"] = df["MonthlyCharges"] * MONTHS_KEPT
df["expected_value"] = (
    df["churn_probability"] * SAVE_RATE * df["value_kept"]
    - OFFER_COST
)

# Rank customers by expected value, highest first
ranked = df.sort_values("expected_value", ascending=False).reset_index(drop=True)

# Calculate cumulative net value at each targeting level
ranked["customers_targeted"] = range(1, len(ranked) + 1)
ranked["cumulative_net_value"] = ranked["expected_value"].cumsum()
ranked["targeted_share_pct"] = (
    ranked["customers_targeted"] / len(ranked) * 100
)

# Include the zero-targeting starting point
curve = pd.concat([
    pd.DataFrame([{
        "customers_targeted": 0,
        "cumulative_net_value": 0.0,
        "targeted_share_pct": 0.0,
    }]),
    ranked[[
        "customers_targeted",
        "cumulative_net_value",
        "targeted_share_pct",
    ]],
], ignore_index=True)

# Identify the targeting level with the highest estimated net value
best = curve.loc[curve["cumulative_net_value"].idxmax()]

# Save curve data for further analysis
Path("data").mkdir(exist_ok=True)
curve.to_csv("data/net_value_by_target_share.csv", index=False)

# Create and save chart
Path("docs").mkdir(exist_ok=True)
plt.figure(figsize=(10, 6))
plt.plot(
    curve["targeted_share_pct"],
    curve["cumulative_net_value"],
    label="Estimated cumulative net value",
)
plt.scatter(
    [best["targeted_share_pct"]],
    [best["cumulative_net_value"]],
    zorder=3,
    label="Best targeting level",
)
plt.annotate(
    f"Best: {best['targeted_share_pct']:.1f}% targeted\n"
    f"Net value: ${best['cumulative_net_value']:,.2f}",
    (best["targeted_share_pct"], best["cumulative_net_value"]),
    xytext=(10, -35),
    textcoords="offset points",
)
plt.axhline(0, linewidth=0.8)
plt.xlabel("Share of customers targeted (%)")
plt.ylabel("Estimated net value (dataset currency units)")
plt.title("Estimated Retention Net Value by Targeting Level")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("docs/net_value_curve.png", dpi=160)
plt.close()

print(f"Test-set customers: {len(df)}")
print(f"Best customers targeted: {int(best['customers_targeted'])}")
print(f"Best targeting share: {best['targeted_share_pct']:.2f}%")
print(f"Maximum estimated net value: ${best['cumulative_net_value']:,.2f}")
print(f"Customers with positive expected value: {(df['expected_value'] > 0).sum()}")
print("Saved: data/net_value_by_target_share.csv")
print("Saved: docs/net_value_curve.png")
