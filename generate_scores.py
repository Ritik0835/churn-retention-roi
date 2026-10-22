from pathlib import Path

import joblib
import pandas as pd
from sklearn.model_selection import train_test_split

root = Path.home() / "Projects"
source = root / "customer-churn-mlops"
destination = root / "churn-retention-roi" / "data" / "scores.csv"

# Load source dataset and trained model
df = pd.read_csv(source / "data" / "Telco-Customer-Churn.csv")
model = joblib.load(source / "models" / "churn_pipeline.joblib")

# Preserve customer IDs and actual churn outcomes
customer_ids = df["customerID"]
actual_churn = df["Churn"].map({"No": 0, "Yes": 1})

# Prepare model inputs
X = df.drop(columns=["customerID", "Churn"]).copy()
X["TotalCharges"] = pd.to_numeric(X["TotalCharges"], errors="coerce")

# Recreate the original stratified test split
X_train, X_test, y_train, y_test, ids_train, ids_test = train_test_split(
    X,
    actual_churn,
    customer_ids,
    test_size=0.20,
    random_state=42,
    stratify=actual_churn,
)

# Predict churn probabilities on test customers only
probabilities = model.predict_proba(X_test)[:, 1]

# Create and save the scoring dataset
scores = pd.DataFrame({
    "customerID": ids_test.to_numpy(),
    "churn_probability": probabilities,
    "actual_churn": y_test.to_numpy(),
    "MonthlyCharges": df.set_index("customerID")
        .loc[ids_test, "MonthlyCharges"].to_numpy(),
})

destination.parent.mkdir(parents=True, exist_ok=True)
scores.to_csv(destination, index=False)

print(f"Saved: {destination}")
print(f"Rows: {len(scores)}")
print(f"Columns: {scores.columns.tolist()}")
print(f"Missing values: {scores.isna().sum().sum()}")
print(scores.head().to_string(index=False))
