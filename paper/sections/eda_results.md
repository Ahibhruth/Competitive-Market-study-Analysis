# Exploratory Data Analysis Results: Competitive Market Dynamics

## 1. Overview of EDA Objectives
This analysis characterizes competitive interaction patterns across two distinct market contexts:
1.  **Japanese Electronics Retail**: A duopoly/oligopoly between BIC Camera and Yodobashi Camera (2018–2020).
2.  **Indian Telecom & FMCG**: A high-growth competitive landscape featuring Reliance Jio, Bharti Airtel, Coca-Cola, and PepsiCo (2016–2024).

The primary objectives were to:
*   Quantify the frequency and speed of competitive responses.
*   Classify action-response pairs to identify aggressive vs. defensive strategies.
*   Analyze the temporal distribution of response lags to understand market discipline.

---

## 2. Summary Statistics and Distributions

### Dataset 1: Japanese Electronics Retail (BIC Camera vs. Yodobashi)
*   **Total Events**: 40 observed competitive actions.
*   **Market Structure**: 100% Oligopoly.
*   **Response Rate**: 90% of initiating actions elicited a direct observable response.
*   **Response Lag**: 
    *   **Mean**: 9.8 days
    *   **Median**: 10.0 days
    *   **Range**: 7–14 days
    *   **Standard Deviation**: ~2.5 days

### Dataset 2: Indian Telecom & FMCG (Multi-Sector)
*   **Total Events**: 40 observed competitive actions.
*   **Market Structure**: Mixed (Oligopoly: 50%, Competitive: 47.5%, Duopoly: 2.5%).
*   **Response Rate**: ~92.5% (High engagement).
*   **Response Lag**:
    *   **Mean**: 12.2 days
    *   **Median**: 0 days (indicating same-day responses are common).
    *   **Max**: 90 days (indicating some long-tail strategic shifts).

---

## 3. Competitive Behavior Patterns

### 3.1 Response Frequency and Predictability
In the **Electronics Retail** sector, the high response rate (90%) and low standard deviation in lag times suggest a highly disciplined "tit-for-tat" equilibrium. Competitors monitor each other closely and respond within a predictable window (1-2 weeks).

In contrast, the **Telecom/FMCG** dataset shows a bifurcated response pattern. While the overall response rate is high, the lag distribution is extreme—ranging from immediate (0 days) to delayed strategic pivots (up to 3 months).

### 3.2 Aggressive vs. Passive Actions
**Heatmap Analysis:**
The interaction between *Action Types* and *Response Types* reveals distinct strategies.

*   **Electronics Retail**: The heatmap displays a strong correlation between "Price promotion" and "Promotional price matching," as well as "Loyalty incentive" and "Matched points campaign." This indicates a defensive, maintenance-focused strategy.
    
    ![Action vs Response Heatmap](../figures/eda/action_type_vs_response_type_heatmap.png)

*   **Telecom/FMCG**: The dynamics are more varied. "Price hikes" often trigger "Competitive responses" or "Matches," but "New product launches" may result in "Alternative strategies" rather than direct cloning.
    
    ![Action vs Response Heatmap (Telecom/FMCG)](../figures/eda/action_type_vs_response_type_heatmap_copy.png)

### 3.3 Temporal Response Lags
The distribution of response lags highlights the speed of information processing in each market.

*   **Electronics Retail**: The distribution is tightly clustered, reflecting standard business cycle adjustments (weekly/bi-weekly).
    
    ![Response Lag Distribution](../figures/eda/response_lag_distribution.png)

*   **Telecom/FMCG**: The distribution shows a significant spike at 0 days (likely algorithmic or pre-planned simultaneous releases) and a long tail, reflecting complex infrastructure or product development cycles.
    
    ![Response Lag Distribution (Telecom/FMCG)](../figures/eda/response_lag_distribution_copy.png)

---

## 4. Cross-Company Comparison Insights

| Feature | BIC Camera vs. Yodobashi (Japan) | Jio / Airtel / Coke / Pepsi (India) |
| :--- | :--- | :--- |
| **Primary Lever** | Price & Loyalty Points | Tariff Pricing, Data Bundles, Product Launch |
| **Response Speed** | Moderate, Consistent (10 days) | Instant (0 days) or Strategic (>30 days) |
| **Market Nature** | Stable Oligopoly | Disruptive / High-Growth |
| **Crisis Sensitivity** | Lower | Higher (COVID, Regulatory shifts) |

*   **Jio's Entry Effect**: The Telecom data highlights "Disruptive" actions (e.g., Free introductory offers) that forced incumbents (Airtel, Vodafone) into a "Price reduction / data boost" cycle, often with near-zero lag.
*   **Cola Wars**: The FMCG segment demonstrates "Product-level" competition (e.g., "Sting energy expansion" vs. "New energy drink focus"), which typically involves longer lags due to supply chain requirements.

---

## 5. Key Empirical Findings

*   **High Response Elasticity**: Across both datasets, >90% of competitive moves faced a retaliation, confirming that these markets are highly interdependent.
*   **Sector-Specific Lag Dynamics**: 
    *   **Retail**: Operates on a weekly/bi-weekly promotional cycle.
    *   **Telecom**: Operates on near-real-time pricing adjustments (0-day lag).
    *   **FMCG**: Operates on product development cycles (longer lags).
*   **Symmetry of Response**: 
    *   Price cuts are almost always met with price cuts (Symmetric).
    *   Format changes (e.g., "Channel expansion") often face asymmetric responses (e.g., "Logistics lead" retention).
*   **Market Structure Impact**: The pure Oligopoly (Japan) showed more predictable, lower-variance behavior compared to the mixed Competitive/Oligopoly structure in the Indian dataset.
