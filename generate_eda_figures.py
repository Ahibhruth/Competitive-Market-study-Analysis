
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure output directory exists
output_dir = "figures/eda/"
os.makedirs(output_dir, exist_ok=True)

def save_plot(name):
    plt.savefig(f"{output_dir}/{name}.png", dpi=300, bbox_inches="tight")
    plt.savefig(f"{output_dir}/{name}.svg", bbox_inches="tight")
    print(f"Saved {name}")
    plt.close()

print("--- Processing eda.ipynb ---")

# Load data
df_raw = pd.read_csv("data/dataset.csv", encoding="utf-8")
df = df_raw.copy()

# Cleaning
missing_values = ["NA", "N/A", "", "None", "null"]
df.replace(missing_values, np.nan, inplace=True)

df["event_date"] = pd.to_datetime(df["event_date"], dayfirst=True, errors="coerce")

def yes_no_clean(x):
    if pd.isna(x): return np.nan
    x = str(x).strip().lower()
    return 1 if x == "yes" else 0 if x == "no" else np.nan

df["response_observed_bin"] = df["response_observed"].apply(yes_no_clean)
df["regulatory_sensitivity_bin"] = df["regulatory_sensitivity"].apply(yes_no_clean)

df["response_lag_days_num"] = pd.to_numeric(df["response_lag_days"], errors="coerce")

def price_type(x):
    if pd.isna(x): return "missing"
    x = str(x).lower().replace("â¥", "¥")
    return "numeric" if "¥" in x else x

df["price_before_type"] = df["price_before"].apply(price_type)
df["price_after_type"] = df["price_after"].apply(price_type)

df["quantity_after"] = df["quantity_after"].astype(str).str.lower().str.strip()
quantity_map = {"standard": 1, "bundle": 2, "seasonal": 3, "expanded": 4, "high speed": 4, "premium": 4}
df["quantity_after_code"] = df["quantity_after"].map(quantity_map)

df["crisis_event"] = df["notes"].astype(str).str.lower().str.contains("covid|inflation|lockdown|tax")

text_cols = ["industry", "action_type", "response_type", "market_structure", "public_sentiment_shift"]
for col in text_cols:
    df[col] = df[col].astype(str).str.lower().str.strip()

# PLOT 1: Heatmap
print("Generating Heatmap...")
plt.figure(figsize=(12,6))
sns.heatmap(
    pd.crosstab(df["action_type"], df["response_type"], normalize="index"),
    cmap="Blues",
    annot=False
)
plt.title("Action Type vs Response Type (Normalized)")
save_plot("action_type_vs_response_type_heatmap")

# PLOT 2: Histplot
print("Generating Histplot...")
sns.histplot(df["response_lag_days_num"], bins=10)
plt.title("Distribution of Response Lag Days")
save_plot("response_lag_distribution")


print("--- Processing eda copy.ipynb ---")
# Load data 2
df_raw = pd.read_csv("data/Data2.csv", encoding="utf-8")
df = df_raw.copy()

# Cleaning (same logic)
df.replace(missing_values, np.nan, inplace=True)
df["event_date"] = pd.to_datetime(df["event_date"], dayfirst=True, errors="coerce")
df["response_observed_bin"] = df["response_observed"].apply(yes_no_clean)
df["regulatory_sensitivity_bin"] = df["regulatory_sensitivity"].apply(yes_no_clean)
df["response_lag_days_num"] = pd.to_numeric(df["response_lag_days"], errors="coerce")
df["price_before_type"] = df["price_before"].apply(price_type)
df["price_after_type"] = df["price_after"].apply(price_type)
df["quantity_after"] = df["quantity_after"].astype(str).str.lower().str.strip()
df["quantity_after_code"] = df["quantity_after"].map(quantity_map)
df["crisis_event"] = df["notes"].astype(str).str.lower().str.contains("covid|inflation|lockdown|tax")
for col in text_cols:
    df[col] = df[col].astype(str).str.lower().str.strip()

# PLOT 1 Copy
print("Generating Heatmap (Copy)...")
plt.figure(figsize=(12,6))
sns.heatmap(
    pd.crosstab(df["action_type"], df["response_type"], normalize="index"),
    cmap="Blues",
    annot=False
)
plt.title("Action Type vs Response Type (Normalized) (Copy)")
save_plot("action_type_vs_response_type_heatmap_copy")

# PLOT 2 Copy
print("Generating Histplot (Copy)...")
sns.histplot(df["response_lag_days_num"], bins=10)
plt.title("Distribution of Response Lag Days (Copy)")
save_plot("response_lag_distribution_copy")

print("Done.")
