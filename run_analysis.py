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
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Mapping binary columns
df['crisis_event'] = df['crisis_event'].map({'yes': 1, 'no': 0})

# Mapping quantity
quantity_mapping = {'low': 1, 'medium': 2, 'high': 3}
df['quantity'] = df['quantity'].map(quantity_mapping)

# Standardizing text columns
text_cols = ['industry', 'action_type', 'price_before_type', 'price_after_type', 'response_type']
for col in text_cols:
    if col in df.columns:
        df[col] = df[col].str.lower().str.strip()

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
if 'response_lag' in df.columns:
    print("\nResponse Lag Statistics:")
    print(df['response_lag'].describe())

# Visualizations (Saved to output/)
plt.figure(figsize=(10, 6))
sns.countplot(y='response_type', data=df)
plt.title('Distribution of Response Types')
plt.tight_layout()
plt.savefig('output/response_type_distribution.png')
print("Saved output/response_type_distribution.png")

# Heatmap: Industry vs Response Type
plt.figure(figsize=(12, 8))
ct = pd.crosstab(df['industry'], df['response_type'])
sns.heatmap(ct, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Industry vs Response Type')
plt.tight_layout()
plt.savefig('output/industry_response_heatmap.png')
print("Saved output/industry_response_heatmap.png")

# ==========================================
# 4. Machine Learning
# ==========================================
print("\n--- Machine Learning ---")

# Filtering
df_ml = df[df['response_type'] != 'invalid'].copy()

# Features and Target
X = df_ml[['industry', 'action_type', 'price_before_type', 'price_after_type']]
y = df_ml['response_type']

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training set shape: {X_train.shape}")
print(f"Test set shape: {X_test.shape}")

# Preprocessing
categorical_features = ['industry', 'action_type', 'price_before_type', 'price_after_type']
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ],
    remainder='passthrough'
)

# Pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('clf', RandomForestClassifier(n_estimators=300, random_state=42, class_weight='balanced'))
])

# Training
print("Training model...")
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
print(f"Model Accuracy: {score:.4f}")

# Feature Importance
feature_names = model.named_steps['preprocessor'].get_feature_names_out()
importances = model.named_steps['clf'].feature_importances_

importance_df = pd.DataFrame({
    'feature': feature_names,
    'importance': importances
}).sort_values(by='importance', ascending=False)

print("\nTop 10 Feature Importances:")
print(importance_df.head(10))

# Save feature importance plot
plt.figure(figsize=(10, 8))
sns.barplot(x='importance', y='feature', data=importance_df.head(10))
plt.title('Top 10 Feature Importances')
plt.tight_layout()
plt.savefig('output/feature_importance.png')
print("Saved output/feature_importance.png")

print("\nAnalysis complete.")
