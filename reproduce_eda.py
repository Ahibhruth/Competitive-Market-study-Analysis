# %% Cell Type: code
import pandas as pd
import numpy as np

df_raw = pd.read_csv("data/dataset.csv", encoding="utf-8")

print("Raw shape:", df_raw.shape)
df_raw.head()
#ahibhruth


# %% Cell Type: code
df = df_raw.copy()


# %% Cell Type: code
missing_values = ["NA", "N/A", "", "None", "null"]
df.replace(missing_values, np.nan, inplace=True)

df.isna().sum()


# %% Cell Type: code
df["event_date"] = pd.to_datetime(
    df["event_date"],
    dayfirst=True,
    errors="coerce"
)


# %% Cell Type: code
def yes_no_clean(x):
    if pd.isna(x):
        return np.nan
    x = str(x).strip().lower()
    if x == "yes":
        return 1
    if x == "no":
        return 0
    return np.nan

df["response_observed_bin"] = df["response_observed"].apply(yes_no_clean)
df["regulatory_sensitivity_bin"] = df["regulatory_sensitivity"].apply(yes_no_clean)

df[["response_observed", "response_observed_bin"]].head()


# %% Cell Type: code
df["response_lag_days_num"] = pd.to_numeric(
    df["response_lag_days"],
    errors="coerce"
)


# %% Cell Type: code
def price_type(x):
    if pd.isna(x):
        return "missing"
    x = str(x).lower()
    x = x.replace("â¥", "¥")  # encoding fix
    if "¥" in x:
        return "numeric"
    return x

df["price_before_type"] = df["price_before"].apply(price_type)
df["price_after_type"] = df["price_after"].apply(price_type)


# %% Cell Type: code
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


# %% Cell Type: code
df["crisis_event"] = (
    df["notes"]
    .astype(str)
    .str.lower()
    .str.contains("covid|inflation|lockdown|tax")
)


# %% Cell Type: code
text_cols = [
    "industry",
    "action_type",
    "response_type",
    "market_structure",
    "public_sentiment_shift"
]

for col in text_cols:
    df[col] = df[col].astype(str).str.lower().str.strip()


# %% Cell Type: code
df.info()

df["response_type"].value_counts()
df["response_observed_bin"].value_counts(dropna=False)
df["response_lag_days_num"].describe()


# %% Cell Type: code
df.to_csv("data/cleaned_dataset.csv", index=False)
print("✅ Cleaned dataset saved to data/cleaned_dataset.csv")


# %% Cell Type: code
df["response_type"].value_counts()
df["response_observed_bin"].value_counts(dropna=False)
df["price_before_type"].value_counts()


# %% Cell Type: code
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/cleaned_dataset.csv")


# %% Cell Type: code
df.shape


# %% Cell Type: code
df.info()

# %% Cell Type: code
df["response_type"].value_counts()


# %% Cell Type: code
pd.crosstab(
    df["action_type"],
    df["response_type"],
    normalize="index"
)


# %% Cell Type: code
plt.figure(figsize=(12,6))
sns.heatmap(
    pd.crosstab(df["action_type"], df["response_type"], normalize="index"),
    cmap="Blues",
    annot=False
)
plt.title("Action Type vs Response Type (Normalized)")
plt.show()


# %% Cell Type: code
pd.crosstab(df["crisis_event"], df["response_type"], normalize="index")


# %% Cell Type: code
df["response_lag_days_num"].describe()


# %% Cell Type: code
sns.histplot(df["response_lag_days_num"], bins=10)
plt.title("Distribution of Response Lag Days")
plt.show()


# %% Cell Type: code
df["industry"].value_counts()


# %% Cell Type: code
pd.crosstab(df["industry"], df["response_type"], normalize="index")


# %% Cell Type: code
counts = df["response_type"].value_counts()
valid_types = counts[counts >= 2].index

df_ml = df[df["response_type"].isin(valid_types)].copy()

df_ml["response_type"].value_counts()


# %% Cell Type: code
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

X = df_ml[features]
y = df_ml["response_type"]


# %% Cell Type: code
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42
)


# %% Cell Type: code
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier


# %% Cell Type: code
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


# %% Cell Type: code
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


# %% Cell Type: code
model.fit(X_train, y_train)


# %% Cell Type: code
from sklearn.metrics import classification_report, confusion_matrix

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))


# %% Cell Type: code
feature_names = model.named_steps["preprocessor"].get_feature_names_out()
importances = model.named_steps["clf"].feature_importances_

importance_df = pd.DataFrame({
    "feature": feature_names,
    "importance": importances
}).sort_values(by="importance", ascending=False)

importance_df.head(10)


# %% Cell Type: code


