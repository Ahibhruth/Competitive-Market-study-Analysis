# Equilibrium Analysis of Competitive Dynamics

## 1. Derivation of Equilibrium Conditions

### 1.1 The Stage Game Equilibrium (Static)
Consider the stage game $G$ defined in the *Game Formulation* report. The payoff matrix for the row player (Firm 1) is given by:

| | Maintain ($s_m$) | Price Cut ($s_p$) | Product Diff ($s_d$) |
| :--- | :--- | :--- | :--- |
| **Maintain ($s_m$)** | $0$ | $-L$ | $-L$ |
| **Price Cut ($s_p$)** | $G$ | $-C$ | $G/2$ |
| **Product Diff ($s_d$)** | $G$ | $-L/2$ | $V$ |

**Empirical Validation of Ordinal Ranking** ($G > V > 0 > -C > -L$):
*   **G > 0**: The 7.5% "No Response" cases show unilateral aggressors capturing market share ("Increase" in Market Share Change variable), confirming positive gains from unpunished defection.
*   **0 > -C**: While "Price war" events show "Neutral" market share outcomes, firms consistently accept this outcome rather than surrender, implying mutual war preserves more total value than unilateral defeat.
*   **-C > -L**: The >90% response rate is the strongest validation—firms immediately match aggressive moves despite incurring cost -C, revealing that tolerating rival aggression (-L) is perceived as strictly worse.
*   **V > 0**: FMCG differentiation cases ("New product launch" → "Alternative strategy") maintain "Positive" outcomes and pricing power, confirming mutual innovation preserves value.
*   **G > V**: Defection temptation inherent in prisoner's dilemma structure—unilateral price cut against cooperating rival yields higher immediate payoff than mutual cooperation.

**Proposition 1 (Prisoner's Dilemma Structure)**: If $G > V > 0 > -C > -L$, then $s_p$ (Price Cut) is a strictly dominant strategy in the stage game, and $(s_p, s_p)$ is the unique Nash Equilibrium (NE).

*Proof*:
1.  If Rival plays $s_m$: $u_1(s_p) = G > 0 = u_1(s_m)$. (Prefer Price Cut)
2.  If Rival plays $s_p$: $u_1(s_p) = -C > -L = u_1(s_m)$. (Prefer Price Cut, since mutual war better than unilateral surrender)
3.  If Rival plays $s_d$: $u_1(s_p) = G/2 > -L/2 = u_1(s_m)$ and $u_1(s_p) = G/2$ requires comparison with $u_1(s_d) = -L/2$. Since $G/2 > 0 > -L/2$, price cutting against differentiation yields positive payoff.
4.  Therefore, $s_p$ dominates $s_m$. While $s_d$ offers defense ($-L/2 > -L$), it does not dominate $s_p$ since $G > V$ implies defection temptation.
5.  The unique pure strategy Nash Equilibrium is $(s_p, s_p)$ with payoff $(-C, -C)$.

### 1.2 Repeated Game Equilibrium (Dynamic)
In the infinitely repeated game $G^\infty(\delta)$, firms can sustain the cooperative outcome $(s_m, s_m)$ or $(s_d, s_d)$ if the discount factor $\delta$ is sufficiently high.

Using a **Grim Trigger Strategy**:
*   Play $s_{coop}$ (e.g., Maintain or Diff) as long as everyone has done so.
*   If anyone deviates to $s_p$, play $s_p$ forever.

**Condition for Stability**:
$$ \frac{\pi_{coop}}{1-\delta} \geq \pi_{defect} + \frac{\delta \cdot \pi_{punish}}{1-\delta} $$

Substituting payoffs $\pi_{coop}=0$ (normalized), $\pi_{defect}=G$, $\pi_{punish}=-C$:
$$ 0 \geq G - \frac{\delta C}{1-\delta} $$
$$ \frac{\delta C}{1-\delta} \geq G $$
$$ \delta \geq \frac{G}{G+C} \equiv \delta^* $$

Thus, cooperation is sustainable if firms value future margin preservation enough relative to the immediate gain from undercutting.

---

## 1.3 Formal Proposition on Monitoring and Response Patterns

**Proposition 2 (Monitoring Lag and Response Symmetry)**: Firms operating in markets with response lags $\Delta_t < 1$ day exhibit significantly higher rates of symmetric (matching) responses compared to firms with $\Delta_t > 10$ days, which show greater strategic flexibility in choosing asymmetric (differentiation) responses.

*Formal Statement*:
Let $\rho_{sym}$ denote the proportion of symmetric responses (Price → Price Match, Product → Product Match). Then:
$$ E[\rho_{sym} | \Delta_t < 1] > E[\rho_{sym} | \Delta_t > 10] $$

*Empirical Evidence*:
*   **Telecom (Low Lag)**: Median response lag = 0 days. The action-response heatmap shows dominant diagonal density with >80% symmetric matching. Price cuts trigger immediate price matches ("Parallel price adjustment").
*   **Retail (Moderate Lag)**: Mean response lag = 9.8 days (SD = 2.5). While still high diagonal density (~70%), off-diagonal entries emerge—"Price promotion" occasionally met with "Loyalty program enhancement" rather than pure price matching.
*   **FMCG (Variable Lag)**: Lag distribution ranges 0-90 days. Strategic "Alternative strategies" (asymmetric responses) more common, with ~40% off-diagonal responses when lag >30 days.

*Theoretical Justification*:
With instantaneous monitoring ($\Delta_t \to 0$), the cost of mismatched response is immediately realized (rapid market share loss), forcing convergence to symmetric Bertrand-style competition. With delayed monitoring ($\Delta_t > 10$), firms have time to:
1.  Assess whether rival's move is temporary or strategic
2.  Develop differentiated counter-strategies (product, channel)
3.  Implement responses that soften direct price competition

This prediction is **testable** using the EDA dataset by stratifying response types (symmetric vs. asymmetric) conditional on lag quantiles.

*Corollary 2.1*: Markets with perfect monitoring ($\Delta_t = 0$) are more likely to converge to the inefficient $(s_p, s_p)$ equilibrium, while markets with moderate information frictions ($\Delta_t \in [7, 14]$ days) exhibit greater equilibrium multiplicity, including coordination on $(s_d, s_d)$.

*Empirical Validation*: Telecom sector (0-day lag) shows persistent price wars and low margins (validation of Corollary 2.1's inefficiency prediction). Japanese Retail (10-day lag) shows stable cycling between promotional periods and differentiation phases, consistent with equilibrium multiplicity.

---

## 2. Stability Analysis

### 2.1 Robustness to Trembles (Trembling Hand Perfection)
In the empirical context, "trembles" correspond to accidental price changes or misinterpretation of rival moves (e.g., a system error posting a wrong price).

*   **Retail Sector**: With imperfect monitoring ($\Delta_t > 0$), a Grim Trigger is fragile. A single noisy signal $y_t$ could trigger an infinite price war.
    *   *Modified Stability Condition*: Firms utilize **Green-Porter** style trigger phases where punishment lasts for $T$ periods rather than infinity.
    *   Stability requires: $V(\text{Coop}) \geq E[V(\text{Defect}) | \text{Noise}]$.

### 2.2 Renegotiation Proofness
Once a punishment phase $(-C, -C)$ begins, both firms have an incentive to renegotiate back to $(0,0)$.
*   **Analysis**: The existence of "Differentiation" ($s_d$) offers a *Pareto-improving* exit path from the price war.
*   **Result**: The equilibrium is *weakly renegotiation-proof* if firms can coordinate on switching to $s_d$ (Product Innovation) rather than simply reverting to $s_m$. This matches the EDA finding where firms pivot to "Product Focus" after price skirmishes.

---

## 3. Comparative Statics

We analyze how equilibrium conditions change with respect to key parameters.

### 3.1 Impact of Response Lag ($\Delta_t$)
Let $\Delta_t$ be the time delay before retaliation. The effective discount factor is $\delta^{\Delta_t}$.
The incentive constraint becomes:
$$ \sum_{t=0}^{\Delta_t-1} \delta^t G + \sum_{t=\Delta_t}^{\infty} \delta^t (-C) \leq \sum_{t=0}^{\infty} \delta^t (0) $$

**Result**: As $\Delta_t$ decreases (faster detection):
*   The gain from defection (first term) shrinks.
*   Punishment arrives sooner.
*   **Conclusion**: $\frac{\partial \text{Stability}}{\partial \Delta_t} < 0$. Faster monitoring (Telecom) makes cooperation *easier* to sustain in theory, or punishment *swifter* if broken.

### 3.2 Impact of Differentiation ($\theta$)
Recall payoff $u_i = \alpha R + (1-\alpha) M \cdot \mathbb{I}(diff)$.
Let $\theta$ represent the degree of differentiation (increasing $V$).

**Result**: $\frac{\partial \delta^*}{\partial \theta} < 0$.
*   Higher differentiation increases the cooperative payoff $V$.
*   This lowers the critical discount factor $\delta^*$, expanding the set of parameters where peace is stable.
*   **Empirical Fit**: Explains why FMCG (high differentiation potential) sees fewer "pure" price wars than Telecom (commodity service).

---

## 4. Industry-Specific Equilibrium Cases

### Case A: Japanese Electronics Retail (The "Stag Hunt" of Promotion)
*   **Parameters**: $\Delta_t \approx 10$ days (Medium), Product Homogeneity = High.
*   **Equilibrium**: **Risk-Dominant Coordinate**.
    *   Firms are in a coordination game where "Matching" is safer than "Leading".
    *   The 10-day lag allows for short-term gains $G$, but the high reputational repetition ($T \to \infty$) enforces a "Tit-for-Tat" discipline.
    *   *Outcome*: Stable cycles of promotion and matching. Deviations are corrected within one cycle ($t+1$).

### Case B: Indian Telecom (The "War of Attrition")
*   **Parameters**: $\Delta_t \approx 0$ (Instant), $\alpha \approx 1$ (Market Share Focus).
*   **Equilibrium**: **Aggressive Nash Equilibrium**.
    *   With $\Delta_t \to 0$, the "Gain" period vanishes. However, if the goal is *market exit* of a rival (predatory pricing), the game changes to a War of Attrition.
    *   Player $i$ fights until cost $C_i > \text{Benefit of Monopoly}$.
    *   *Outcome*: Intense, low-margin equilibrium until market consolidation occurs or segmentation (Post-paid vs Pre-paid) is established.

---

## 5. Economic Interpretation

### 5.1 Efficiency and Welfare
*   **Consumer Surplus**: The "Price Cut" equilibrium maximizes consumer surplus in the short run (lower prices). However, the "Differentiation" equilibrium ($s_d$) may increase total welfare by introducing variety, even if prices are higher.
*   **Deadweight Loss**: The "Status Quo" ($s_m$) under oligopoly typically implies prices $P > MC$. The breakdown of collusion (Price Wars) moves $P \to MC$, correcting the deadweight loss but harming producer surplus.

### 5.2 The "Red Queen" Effect
The stability analysis reveals a "Red Queen" dynamic: firms must constantly run (respond) just to stay in the same place (maintain share).
*   In Retail, this manifests as **Promotional Churn**: constant activity with neutral net share change.
*   In Telecom, this manifests as **Feature Escalation**: data caps increase exponentially while ARPU (Average Revenue Per User) remains flat or declines.

### 5.3 Strategic Recommendation
To escape the low-profit $(s_p, s_p)$ trap, firms must increase $\theta$ (Differentiation).
*   **Mechanism**: By reducing the substitutability of products, firms decouple their reaction functions.
*   **Prediction**: Future competition will shift from Price (observable, easy to match) to Ecosystem Lock-in (complex, hard to match), increasing the effective $\Delta_t$ for rivals and restoring stability.
