
import pandas as pd
import numpy as np

def analyze_dataset(file_path, name):
    print(f"--- Analysis for {name} ({file_path}) ---")
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    print(f"Total Events: {len(df)}")
    print(f"Time Range: {df['event_date'].min()} to {df['event_date'].max()}")
    
    # Companies
    if 'initiating_company' in df.columns:
        print("\nInitiating Companies:")
        print(df['initiating_company'].value_counts())
    if 'responding_company' in df.columns:
        print("\nResponding Companies:")
        print(df['responding_company'].value_counts())

    # Response Analysis
    if 'response_observed' in df.columns:
        resp_counts = df['response_observed'].value_counts(normalize=True)
        print("\nResponse Observed Distribution:")
        print(resp_counts)
    
    # Lag Analysis
    if 'response_lag_days' in df.columns:
        # Clean lag
        lag = pd.to_numeric(df['response_lag_days'], errors='coerce')
        print("\nResponse Lag (Days) Stats:")
        print(lag.describe())

    # Action Types
    if 'action_type' in df.columns:
        print("\nAction Types:")
        print(df['action_type'].value_counts())

    # Response Types
    if 'response_type' in df.columns:
        print("\nResponse Types:")
        print(df['response_type'].value_counts())
        
    # Market Structure
    if 'market_structure' in df.columns:
        print("\nMarket Structure:")
        print(df['market_structure'].value_counts())

analyze_dataset("data/dataset.csv", "Original Dataset")
analyze_dataset("data/Data2.csv", "Dataset 2")
