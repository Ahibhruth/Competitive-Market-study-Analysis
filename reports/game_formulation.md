# Game Theoretic Formulation of Competitive Dynamics

## 1. Model Objective
The objective of this game theoretic model is to analyze the strategic interactions between dominant firms in oligopolistic markets (specifically Electronics Retail and Telecom/FMCG). The model seeks to explain the high frequency of retaliatory responses and the divergence between "symmetric matching" (tit-for-tat) and "asymmetric differentiation" strategies observed in the empirical data.

## 2. Players
Let $N = \{1, 2, ..., n\}$ be the set of players.
Based on the EDA findings, we define two distinct player sets corresponding to the observed markets:

*   **Set A (Stable Duopoly)**: $N_A = \{\text{Firm}_1, \text{Firm}_2\}$
    *   *Empirical Proxy*: BIC Camera vs. Yodobashi Camera.
    *   *Characteristics*: High mutual monitoring, entrenched market positions.
*   **Set B (Disruptive Oligopoly)**: $N_B = \{\text{Incumbent}_1, \text{Incumbent}_2, \text{Disruptor}\}$
    *   *Empirical Proxy*: Airtel/Vodafone (Incumbents) vs. Reliance Jio (Disruptor); Coca-Cola vs. PepsiCo.
    *   *Characteristics*: Asymmetric capabilities, high-stakes market share battles.

## 3. Strategy Sets ($S_i$)
Derived explicitly from the "Action Types" and "Response Types" identified in the EDA (Section 3.2), the strategy space $S_i$ for player $i$ includes:

$$S_i = \{s_{\text{maintain}}, s_{\text{price}}, s_{\text{product}}, s_{\text{channel}}\}$$

Where:
*   $s_{\text{maintain}}$ (**Status Quo**): No new action initiated.
*   $s_{\text{price}}$ (**Price/Promotional Aggression**):
    *   *Observed Actions*: "Price promotion", "Loyalty incentive", "Tariff hike", "Free data promotion".
    *   *Observed Responses*: "Promotional price matching", "Parallel price adjustment".
*   $s_{\text{product}}$ (**Product Differentiation**):
    *   *Observed Actions*: "New product launch", "Sting energy expansion".
    *   *Observed Responses*: "Alternative strategy", "New energy drink focus".
*   $s_{\text{channel}}$ (**Structural/Channel Shift**):
    *   *Observed Actions*: "Channel expansion", "Fiber broadband launch".
    *   *Observed Responses*: "Logistics lead retention" (Asymmetric response).

## 4. Game Type

### 4.1 Temporal Structure: Repeated Game
The empirical evidence strongly supports a **Repeated Game** formulation ($G^\infty$) rather than a static one-shot game.
*   **Evidence**: The "Response Lag" distribution (Section 3.3) shows continuous interaction cycles.
    *   *Retail*: Consistent 7-14 day cycles imply a discrete time period $t$ (weekly).
    *   *Telecom*: Near-zero lag implies continuous time or very rapid $t$.
*   **Horizon**: Indefinite ($T \to \infty$), as firms compete perpetually without a known end date.

### 4.2 Nature of Play: Non-Cooperative
*   **Evidence**: The high response rate (>90%) and the prevalence of "Price reduction" and "Competitive reaction" (Section 3.2) indicate a lack of collusion. Firms are actively defending market share rather than coordinating to maximize joint profits (which would imply fewer price wars).

## 5. Assumptions
Each assumption is grounded in the EDA findings:

1.  **Imperfect Monitoring with Low Noise (Retail) vs. High Visibility (Telecom)**
    *   *Justification*: In Retail, the 7-14 day lag suggests a delay in observing and reacting to rival moves. In Telecom, the 0-day median lag confirms perfect information where price changes are instantly visible.
2.  **Reaction Functions are Deterministic**
    *   *Justification*: The Heatmap analysis (Section 3.2) shows strong diagonal density (e.g., Price $\to$ Price Match). Firms rarely randomize; they follow predictable "Tit-for-Tat" or "Matched" strategies.
3.  **Asymmetric Costs of Delay**
    *   *Justification*: The "Disruptive" market (Telecom) exhibits 0-day lags, implying the cost of delay is extremely high (rapid subscriber churn). The "Stable" market (Retail) tolerates ~10-day lags, implying lower immediate churn risks.
4.  **Differentiated Payoff Sensitivity**
    *   *Justification*: The "Crisis Sensitivity" finding (Section 4) indicates that external shocks (COVID, Regulatory) alter the payoff matrix, forcing shifts from $s_{\text{price}}$ to $s_{\text{channel}}$ (e.g., Online/Delivery).

## 6. Payoff Structure
We define the payoff function $\pi_i(s_i, s_{-i})$ based on ordinal preferences derived from "Response Observed" and "Market Share Change" proxies.

Let $\pi_i$ be composed of Market Share ($M$) and Margin ($P$).

$$ \pi_i(s_i, s_{-i}) = M_i(s_i, s_{-i}) + \lambda P_i(s_i) $$

**Ordinal Payoff Matrix (Proxy):**

| Player 1 \ Player 2 | Maintain ($s_m$) | Price Cut ($s_p$) | Product Innovation ($s_d$) |
| :--- | :--- | :--- | :--- |
| **Maintain ($s_m$)** | $(0, 0)$ | $(-L, G)$ | $(-L, G)$ |
| **Price Cut ($s_p$)** | $(G, -L)$ | $(-C, -C)$ | $(?, ?)$ |
| **Product ($s_d$)** | $(G, -L)$ | $(?, ?)$ | $(V, V)$ |

*   **Status Quo $(0,0)$**: "Neutral" market share estimate (observed in 60% of cases).
*   **Unilateral Aggression $(G, -L)$**: If Firm 1 plays $s_p$ (Price Cut) and Firm 2 plays $s_m$, Firm 1 gains share ($G$) and Firm 2 loses ($-L$). *Evidence*: "Response Observed = No" is rare (7.5%), implying firms avoid this outcome.
*   **Price War $(-C, -C)$**: Both play $s_p$. Share remains "Neutral" (Section 2, Table 1 in EDA), but margins erode. *Evidence*: High frequency of "Price adjustment" pairs with "Neutral" market share outcome.
*   **Differentiation $(V, V)$**: Both play $s_d$ (Product/Channel). Margins are preserved. *Evidence*: "Channel expansion" met with "Logistics lead" retention results in "Positive" sentiment.

## 7. Model Limitations
1.  **Binary Response Simplification**: The model categorizes responses broadly (Match/Differentiation), losing nuance in the *magnitude* of response (e.g., 5% vs 10% price cut).
2.  **Lag Time Abstraction**: While we treat the game as repeated, the specific impact of the *length* of delay (e.g., 7 days vs 14 days) on the payoff function is not explicitly modeled, though EDA shows it varies by sector.
3.  **Missing Cost Data**: We assume cost structures based on "Margin" implications, but we lack direct financial data to quantify $C$ or $V$ precisely.
