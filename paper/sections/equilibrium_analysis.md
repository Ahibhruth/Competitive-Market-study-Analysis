# Equilibrium Analysis of Competitive Dynamics

## 1. Derivation of Equilibrium Conditions

### 1.1 The Stage Game Equilibrium (Static)
Consider the stage game $G$ defined in the *Game Formulation* report. The payoff matrix for the row player (Firm 1) is given by:

| | Maintain ($s_m$) | Price Cut ($s_p$) | Product Diff ($s_d$) |
| :--- | :--- | :--- | :--- |
| **Maintain ($s_m$)** | $0$ | $-L$ | $-L$ |
| **Price Cut ($s_p$)** | $G$ | $-C$ | $?$ |
| **Product Diff ($s_d$)** | $G$ | $?$ | $V$ |

**Proposition 1 (Prisoner's Dilemma)**: If $G > 0 > -C > -L$, then $s_p$ (Price Cut) is a strictly dominant strategy in the stage game, and $(s_p, s_p)$ is the unique Nash Equilibrium (NE).

*Proof*:
1.  If Rival plays $s_m$: $u_1(s_p) = G > 0 = u_1(s_m)$. (Prefer Price Cut)
2.  If Rival plays $s_p$: $u_1(s_p) = -C > -L = u_1(s_m)$. (Prefer Price Cut, assuming loss from inaction is greater than cost of war)
3.  Therefore, $s_p$ dominates $s_m$.

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
