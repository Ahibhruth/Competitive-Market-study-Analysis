import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

# Ensure directories exist
os.makedirs("data", exist_ok=True)
os.makedirs("output", exist_ok=True)

print("Starting analysis...")

# ==========================================
# 1. Data Loading
# ==========================================
print("\n--- Data Loading ---")
try:
    df_raw = pd.read_csv("data/dataset.csv", encoding="utf-8")
    print(f"Raw data loaded. Shape: {df_raw.shape}")
except FileNotFoundError:
    print("Error: data/dataset.csv not found.")
    exit(1)

# ==========================================
# 2. Data Cleaning
# ==========================================
print("\n--- Data Cleaning ---")
df = df_raw.copy()

# Handling missing values
missing_values = ["NA", "N/A", "", "None", "null"]
df.replace(missing_values, np.nan, inplace=True)
print(f"Missing values before cleaning:\n{df.isna().sum()}")

# Date conversion
df["event_date"] = pd.to_datetime(
    df["event_date"],
    dayfirst=True,
    errors="coerce"
)

# Helper function for yes/no cleaning
def yes_no_clean(x):
    if pd.isna(x):
        return np.nan
    x = str(x).strip().lower()
    if x == "yes":
        return 1
    if x == "no":
        return 0
    return np.nan

# Apply yes/no cleaning
if "response_observed" in df.columns:
    df["response_observed_bin"] = df["response_observed"].apply(yes_no_clean)
if "regulatory_sensitivity" in df.columns:
    df["regulatory_sensitivity_bin"] = df["regulatory_sensitivity"].apply(yes_no_clean)

# Numeric conversion for response_lag_days
if "response_lag_days" in df.columns:
    df["response_lag_days_num"] = pd.to_numeric(df["response_lag_days"], errors="coerce")

# Price type cleaning
def price_type(x):
    if pd.isna(x):
        return "missing"
    x = str(x).lower()
    x = x.replace("â¥", "¥")  # encoding fix
    if "¥" in x:
        return "numeric"
    return x

if "price_before" in df.columns:
    df["price_before_type"] = df["price_before"].apply(price_type)
if "price_after" in df.columns:
    df["price_after_type"] = df["price_after"].apply(price_type)

# Quantity cleaning
if "quantity_after" in df.columns:
    df["quantity_after"] = df["quantity_after"].astype(str).str.lower().str.strip()
    quantity_map = {
        "standard": 1,
        "bundle": 2,
        "seasonal": 3,
        "expanded": 4,
        "high speed": 4,
        "premium": 4
    }
    df["quantity_after_code"] = df["quantity_after"].map(quantity_map)

# Crisis event creation from notes
if "notes" in df.columns:
    df["crisis_event"] = (
        df["notes"]
        .astype(str)
        .str.lower()
        .str.contains("covid|inflation|lockdown|tax")
    ).astype(int)

# Save cleaned data
cleaned_path = "data/cleaned_dataset.csv"
df.to_csv(cleaned_path, index=False)
print(f"Cleaned data saved to {cleaned_path}")

# ==========================================
# 3. Exploratory Data Analysis (EDA)
# ==========================================
print("\n--- Exploratory Data Analysis ---")
print(df.info())

# Response Lag Analysis
if "response_lag_days_num" in df.columns:
    print("\nResponse Lag Statistics:")
    print(df["response_lag_days_num"].describe())

# Visualizations (Saved to output/)
plt.figure(figsize=(10, 6))
sns.countplot(y="response_type", data=df)
plt.title("Distribution of Response Types")
plt.tight_layout()
plt.savefig("output/response_type_distribution.png")
print("Saved output/response_type_distribution.png")

# Heatmap: Industry vs Response Type
plt.figure(figsize=(12, 8))
ct = pd.crosstab(df["industry"], df["response_type"])
sns.heatmap(ct, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Industry vs Response Type")
plt.tight_layout()
plt.savefig("output/industry_response_heatmap.png")
print("Saved output/industry_response_heatmap.png")

# ==========================================
# 4. Machine Learning
# ==========================================
print("\n--- Machine Learning ---")

# Filtering response types with counts >= 2
counts = df["response_type"].value_counts()
valid_types = counts[counts >= 2].index
df_ml = df[df["response_type"].isin(valid_types)].copy()

print(f"Filtered ML dataset shape: {df_ml.shape}")

# Features and Target
features = [
    "industry",
    "action_type",
    "price_before_type",
    "price_after_type",
    "quantity_after_code",
    "market_structure",
    "regulatory_sensitivity_bin",
    "crisis_event"
]

# Ensure all features exist
missing_features = [f for f in features if f not in df_ml.columns]
if missing_features:
    print(f"Error: Missing features for ML: {missing_features}")
else:
    X = df_ml[features]
    y = df_ml["response_type"]

    # Train Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.25,
        random_state=42
    )
    print(f"Training set shape: {X_train.shape}")
    print(f"Test set shape: {X_test.shape}")

    # Preprocessing
    categorical = [
        "industry",
        "action_type",
        "price_before_type",
        "price_after_type",
        "market_structure"
    ]

    numeric = [
        "quantity_after_code",
        "regulatory_sensitivity_bin",
        "crisis_event"
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
            ("num", "passthrough", numeric)
        ]
    )

    # Pipeline
    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("clf", RandomForestClassifier(
                n_estimators=300,
                random_state=42,
                class_weight="balanced"
            ))
        ]
    )

    # Training
    print("Training model...")
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(f"Model Accuracy: {score:.4f}")

    # Feature Importance (Extracting from Pipeline)
    try:
        # Get feature names from OneHotEncoder
        ohe = model.named_steps["preprocessor"].named_transformers_["cat"]
        cat_features = ohe.get_feature_names_out(categorical)
        all_features = np.concatenate([cat_features, numeric])
        
        importances = model.named_steps["clf"].feature_importances_
        
        importance_df = pd.DataFrame({
            "feature": all_features,
            "importance": importances
        }).sort_values(by="importance", ascending=False)
        
        print("\nTop 10 Feature Importances:")
        print(importance_df.head(10))
        
        # Save feature importance plot
        plt.figure(figsize=(10, 8))
        sns.barplot(x="importance", y="feature", data=importance_df.head(10))
        plt.title("Top 10 Feature Importances")
        plt.tight_layout()
        plt.savefig("output/feature_importance.png")
        print("Saved output/feature_importance.png")
        
    except Exception as e:
        print(f"Could not extract feature importances: {e}")

print("\nAnalysis complete.")
