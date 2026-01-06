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
The strategy space is constructed by abstracting the empirical action and response categories defined in Section 3.2 of the main paper. The formal definitions of **competitive action** (a publicly observable strategic initiative by a firm) and **competitive response** (a subsequent counter-move by a competitor) provide the empirical foundation for our game-theoretic constructs. Each observed action type (e.g., "price promotion," "menu expansion," "channel expansion") maps to one of four abstract strategies, allowing us to translate granular competitive events into a tractable game structure.

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
We define the payoff function $\pi_i(s_i, s_{-i})$ based on ordinal preferences derived from "Response Observed" and "Market Share Change" proxies observed in the EDA.

Let $\pi_i$ be composed of Market Share ($M$) and Margin ($P$).

$$ \pi_i(s_i, s_{-i}) = M_i(s_i, s_{-i}) + \lambda P_i(s_i) $$

### 6.1 Payoff Parameter Definitions and Empirical Justification

We define four key payoff parameters, each grounded in observable competitive outcomes:

**G (Unilateral Gain from Aggression)**: Market share gain when one firm initiates a competitive move (price cut, promotion) while the rival maintains status quo.
*   *Empirical Evidence*: The "No Response" cases (7.5% of observations) show the aggressive firm capturing share. In Telecom, Jio's initial free data offers (unmatched for months) yielded subscriber gains, validating G > 0.
*   *Magnitude Justification*: Market Share Change marked as "Increase" in EDA dataset for unilateral movers.
*   *Ordinal Value*: G = +3 (highest single-period payoff, representing temporary monopolistic advantage).

**L (Loss from Being Undercut)**: Market share loss when a firm maintains status quo while rival cuts price or launches aggressive promotion.
*   *Empirical Evidence*: Same "No Response" scenarios from rival's perspective. The 90%+ response rate indicates firms perceive L as severe enough to justify immediate retaliation costs.
*   *Magnitude Justification*: The extremely high response rate (>90%) reveals that -L must be worse than the cost of matching (-C), otherwise firms would tolerate being undercut.
*   *Ordinal Value*: L = -2 (worse than price war outcome, representing significant share erosion).

**C (Cost of Mutual Price War)**: Margin erosion when both firms simultaneously cut prices or engage in promotional battles.
*   *Empirical Evidence*: "Price promotion" → "Promotional price matching" pairs (dominant pattern in Electronics Retail heatmap) show "Neutral" market share outcomes, but implicit margin compression.
*   *Magnitude Justification*: The prevalence of price-matching cycles (diagonal density in action-response heatmap >70%) indicates firms accept -C as necessary defense, but it preserves more value than surrender (-L).
*   *Ordinal Ranking*: -C > -L (i.e., -1 > -2), meaning mutual war is less damaging than unilateral defeat.
*   *Ordinal Value*: C = -1 (both firms erode margins but maintain relative positions).

**V (Value from Mutual Differentiation)**: Preserved margins when both firms compete on product/channel innovation rather than price.
*   *Empirical Evidence*: FMCG cases where "New product launch" met with "Alternative strategy" (e.g., Coca-Cola's Sting energy drink vs. PepsiCo's alternative energy focus) show "Positive" sentiment and maintained pricing power.
*   *Magnitude Justification*: Firms pivot to product differentiation after price war episodes (observed in "Differentiation as Exit Strategy" pattern), revealing that V > -C and potentially V > 0.
*   *Ordinal Value*: V = +2 (cooperative outcome preserving margins for both firms, though lower than monopolistic gain G).

**Ordinal Ranking Validation**: G > V > 0 > -C > -L (i.e., +3 > +2 > 0 > -1 > -2)
*   *Empirical Support*: 
    *   High response rate (>90%) confirms -C > -L (firms prefer matching to surrender)
    *   Shift to differentiation after price wars confirms V > -C (escape from prisoner's dilemma)
    *   Rare "No Response" confirms G > 0 (unilateral aggression pays when unpunished)
    *   G > V follows from defection temptation in prisoner's dilemma structure

### 6.2 Complete Payoff Matrix with Empirically Resolved Asymmetric Entries

| Player 1 \ Player 2 | Maintain ($s_m$) | Price Cut ($s_p$) | Product Innovation ($s_d$) |
| :--- | :--- | :--- | :--- |
| **Maintain ($s_m$)** | $(0, 0)$ | $(-L, G)$ | $(-L, G)$ |
| **Price Cut ($s_p$)** | $(G, -L)$ | $(-C, -C)$ | $(G/2, -L/2)$ |
| **Product ($s_d$)** | $(G, -L)$ | $(-L/2, G/2)$ | $(V, V)$ |

*   **Status Quo $(0,0)$**: "Neutral" market share estimate (observed in 60% of cases with no competitive action).
*   **Unilateral Aggression $(G, -L)$**: If Firm 1 plays $s_p$ (Price Cut) and Firm 2 plays $s_m$, Firm 1 gains share ($G$) and Firm 2 loses ($-L$). *Evidence*: "Response Observed = No" is rare (7.5%), implying firms avoid this outcome.
*   **Price War $(-C, -C)$**: Both play $s_p$. Share remains "Neutral" (Section 2, Table 1 in EDA), but margins erode. *Evidence*: High frequency of "Price adjustment" pairs with "Neutral" market share outcome.
*   **Differentiation $(V, V)$**: Both play $s_d$ (Product/Channel). Margins are preserved. *Evidence*: "Channel expansion" met with "Logistics lead" retention results in "Positive" sentiment.

**Previously Unspecified Asymmetric Entries (Resolved)**:

*   **(Price Cut, Product Diff) → $(G/2, -L/2)$**: When Firm 1 cuts price while Firm 2 differentiates on product/channel.
    *   *Empirical Evidence*: EDA heatmap shows "Price hikes" (or cuts) often trigger "Alternative strategies" rather than matching in FMCG/Telecom (off-diagonal cells). The outcome is intermediate: price cutter gains some price-sensitive customers (partial G), while differentiator loses some share but retains loyal segment (partial L).
    *   *Justification*: Product differentiation provides *partial insulation* against price competition. Examples: When Jio cut prices, Airtel's "Premium postpaid" differentiation retained high-value customers despite subscriber count pressure. Similarly, Coca-Cola's "New product launches" during PepsiCo price promotions maintained brand premium in certain segments.
    *   *Ordinal Logic*: G/2 > 0 > -L/2 > -L, confirming differentiation strategy is defensive but not fully protective against price aggression.

*   **(Product Diff, Price Cut) → $(-L/2, G/2)$**: Symmetric case by role reversal.
    *   *Empirical Evidence*: When one firm launches "New product" while rival responds with "Competitive price action," the innovator faces customer defection from price-sensitive segments but retains differentiation premium.
    *   *Example*: Retail electronics cases where one firm expanded channel (e.g., online platform) while rival matched with aggressive point redemption promotions—both captured partial gains in different customer segments.

**Critical Implication**: The resolution of these asymmetric payoffs reveals that **pure product differentiation ($s_d$) is NOT a dominant defense** against price cuts in the stage game. Since $G/2 > -L/2$ for the price cutter, firms cannot unilaterally escape price competition through differentiation alone. This explains why mutual coordination on $(V, V)$ requires repeated game enforcement mechanisms (analyzed in Equilibrium section).

## 7. Model Limitations
1.  **Binary Response Simplification**: The model categorizes responses broadly (Match/Differentiation), losing nuance in the *magnitude* of response (e.g., 5% vs 10% price cut).
2.  **Lag Time Abstraction**: While we treat the game as repeated, the specific impact of the *length* of delay (e.g., 7 days vs 14 days) on the payoff function is not explicitly modeled, though EDA shows it varies by sector.
3.  **Missing Cost Data**: We assume cost structures based on "Margin" implications, but we lack direct financial data to quantify $C$ or $V$ precisely.

## 8. Formal Game Theoretic Extensions

### 8.1 Strategy Formalization
Let $h_t = (a^0, a^1, ..., a^{t-1})$ denote the public history of actions at time $t$, where $a^\tau = (a_1^\tau, ..., a_n^\tau)$ is the action profile at period $\tau$. A pure strategy $\sigma_i$ for player $i$ is a mapping from the set of all possible histories $\mathcal{H}$ to the action set $A_i$:

$$ \sigma_i: \mathcal{H} \to A_i $$

Given the EDA evidence of "Tit-for-Tat" (Retail) and "Immediate Retaliation" (Telecom), we posit that players utilize **Markov Strategies** conditioned on the most recent state $k$ (where $k$ represents the lag window):

$$ \sigma_i(h_t) \approx \sigma_i(a_{-i, t-1}, ..., a_{-i, t-k}) $$

*   **Retail Case ($k \approx 7-14$ days)**: Strategies depend on aggregate behavior over the last cycle.
*   **Telecom Case ($k \to 0$ days)**: Strategies respond to instantaneous moves: $\sigma_i(a_{-i, t})$.

### 8.2 Payoff Function Decomposition
We decompose the instantaneous payoff function $u_i(a)$ into **Market Share Retention ($R$)** and **Profit Margin ($M$)**, adjusted by a **differentiation parameter** $\theta$:

$$ u_i(a_i, a_{-i}) = \underbrace{\alpha \cdot R(a_i, a_{-i})}_\text{Volume Effect} + \underbrace{(1-\alpha) \cdot M(a_i) \cdot \mathbb{I}(a_i \neq a_{-i})}_\text{Differentiation Premium} - \underbrace{C(a_i)}_\text{Implementation Cost} $$

Where:
*   $\alpha \in [0,1]$: Weight on market share (higher for Telecom disruptors).
*   $\mathbb{I}(\cdot)$: Indicator function for product differentiation.
*   $C(a_i)$: Cost function (Low for Price cuts, High for Channel expansion).

**EDA Connection**:
*   *Price War*: Both choose $s_{price} \implies M(a_i)$ drops, $\mathbb{I}=0$. Payoff is low $(-C, -C)$.
*   *Differentiation*: One chooses $s_{price}$, other $s_{channel} \implies \mathbb{I}=1$. Margins are preserved for the differentiator.

### 8.3 Information Structure & Lag
The "Response Lag" ($\Delta_t$) identified in the EDA acts as an information friction parameter.

*   **Perfect Monitoring (Telecom)**: $\Delta_t \to 0$. Actions are observable $a_{-i, t}$ at time $t$.
    *   *Implication*: Supports subgame perfect equilibria with immediate punishment.
*   **Imperfect Monitoring (Retail)**: $\Delta_t \sim N(\mu=10, \sigma^2)$. Player $i$ observes a noisy signal $y_t$ of rival's action.
    *   *Implication*: Explains the "Maintain" periods; firms wait for signal confirmation before retaliating to avoid Type I errors (starting a price war falsely).

### 8.4 Mapping EDA Behaviors to Equilibrium Concepts

| Observed Behavior (EDA) | Game Theoretic Equivalent | Formal Condition |
| :--- | :--- | :--- |
| **0-Day Response (Telecom)** | **Grim Trigger / Immediate Punishment** | $\delta > \frac{g}{g+l}$ (Discount factor high enough to sustain collusion, or cost of delay is infinite) |
| **7-14 Day Lag (Retail)** | **Monitoring Delay / Inspection Game** | Observability $\omega < 1$; Response occurs only when $P(\text{Defection} | \text{Signal}) > \text{Threshold}$ |
| **Price Matching (Diagonal)** | **Nash Equilibrium in Prices (Bertrand)** | $BR_i(s_{price}) = s_{price}$ where $p_i = p_j$ |
| **Channel vs. Price (Off-Diagonal)** | **Product Differentiation (Hotelling)** | $\frac{\partial \pi_i}{\partial s_{channel}} > \frac{\partial \pi_i}{\partial s_{price}}$ given rival plays $s_{price}$ |
