
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import itertools

# Configuration
OUTPUT_DIR = "figures/game_theory/"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. Encode Players and Strategies
players = ["Firm 1", "Firm 2"]
strategies = ["Maintain", "Price Cut", "Product Diff"]

# 2. Construct Payoff Matrices (Ordinal Proxy Values)
# Values derived from game_formulation.md:
# Maintain (0,0)
# Unilateral Aggression: Winner gets G (Gain), Loser gets -L (Loss)
# Price War: Both get -C (Cost/Margin Erosion)
# Differentiation: Both get V (Value Preservation)

# Proxy numerical values for ordinal ranking:
G = 3   # Significant market share gain
L = 2   # Significant market share loss
C = 1   # Margin erosion (less bad than losing share, but worse than neutral)
V = 2   # Value preservation (positive outcome, similar to G but shared)
# Unknowns (?, ?) in formulation are estimated based on logic:
# Price Cut vs Product Diff -> Price cutter gains share (G), Diff player loses share (-L) short term? 
# Or Diff player ignores price cut? 
# Let's assume Price Cut beats Product Diff in short term share (G, -L) for consistency with "Price Sensitivity"
# But Product Diff vs Price Cut -> (V, -C)? No, let's stick to the formulation's logic.
# If (Price Cut, Product Diff) -> The Formulation said (?, ?). 
# Let's assume: Price Cut gains share (G), Product Diff player loses (-L).
# If (Product Diff, Price Cut) -> (-L, G).

# Payoff Matrix Construction
# Rows: Firm 1, Cols: Firm 2
# Format: (Firm 1 Payoff, Firm 2 Payoff)

payoff_matrix = {
    ("Maintain", "Maintain"): (0, 0),
    ("Maintain", "Price Cut"): (-L, G),
    ("Maintain", "Product Diff"): (-L, G),  # Assuming Product Diff captures share from Maintainer
    
    ("Price Cut", "Maintain"): (G, -L),
    ("Price Cut", "Price Cut"): (-C, -C),
    ("Price Cut", "Product Diff"): (G, -L), # Price cutter steals share from differentiator (short term)
    
    ("Product Diff", "Maintain"): (G, -L),
    ("Product Diff", "Price Cut"): (-L, G), # Differentiator loses share to Price Cutter (short term)
    ("Product Diff", "Product Diff"): (V, V)
}

# 3. Identify Best Responses and Nash Equilibrium
def find_nash_equilibrium(payoff_map, strats):
    nash_eqs = []
    
    # Create payoff grids for easier analysis
    p1_grid = np.zeros((len(strats), len(strats)))
    p2_grid = np.zeros((len(strats), len(strats)))
    
    for r, strat1 in enumerate(strats):
        for c, strat2 in enumerate(strats):
            payoffs = payoff_map[(strat1, strat2)]
            p1_grid[r, c] = payoffs[0]
            p2_grid[r, c] = payoffs[1]
            
    # Find Best Responses
    best_responses_p1 = [] # List of (r, c)
    best_responses_p2 = [] # List of (r, c)
    
    # For each column (Firm 2 strategy), find Firm 1's best row
    for c in range(len(strats)):
        col_payoffs = p1_grid[:, c]
        max_val = np.max(col_payoffs)
        for r in range(len(strats)):
            if p1_grid[r, c] == max_val:
                best_responses_p1.append((r, c))
                
    # For each row (Firm 1 strategy), find Firm 2's best column
    for r in range(len(strats)):
        row_payoffs = p2_grid[r, :]
        max_val = np.max(row_payoffs)
        for c in range(len(strats)):
            if p2_grid[r, c] == max_val:
                best_responses_p2.append((r, c))
                
    # Intersection = Nash
    nash_indices = set(best_responses_p1).intersection(set(best_responses_p2))
    for r, c in nash_indices:
        nash_eqs.append((strats[r], strats[c]))
        
    return nash_eqs, p1_grid, p2_grid, best_responses_p1, best_responses_p2

nash_equilibria, p1_grid, p2_grid, br_p1, br_p2 = find_nash_equilibrium(payoff_matrix, strategies)

print(f"Nash Equilibria identified: {nash_equilibria}")

# 4. Generate Visual Outputs

def plot_payoff_matrix(p1_g, p2_g, strats, nash_eqs, filename):
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Create a text grid
    n = len(strats)
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_xticks(np.arange(n) + 0.5)
    ax.set_yticks(np.arange(n) + 0.5)
    ax.set_xticklabels(strats)
    ax.set_yticklabels(strats[::-1]) # Reverse to match matrix orientation
    ax.xaxis.set_ticks_position('top')
    
    # Grid lines
    for x in range(n + 1):
        ax.axhline(x, color='black', linewidth=1)
        ax.axvline(x, color='black', linewidth=1)
        
    # Plot payoffs
    for r in range(n):
        for c in range(n):
            # Matrix coordinates: r=0 is top, r=n-1 is bottom
            # Plot coordinates: y=n-1 is top, y=0 is bottom
            y_pos = n - 1 - r
            
            p1_val = int(p1_g[r, c])
            p2_val = int(p2_g[r, c])
            text = f"({p1_val}, {p2_val})"
            
            # Highlight Nash
            if (strats[r], strats[c]) in nash_eqs:
                rect = plt.Rectangle((c, y_pos), 1, 1, facecolor='#FFD700', alpha=0.3)
                ax.add_patch(rect)
                text += "\n(NE)"
                
            ax.text(c + 0.5, y_pos + 0.5, text, 
                    ha='center', va='center', fontsize=12, fontweight='bold')
            
    ax.set_title("Ordinal Payoff Matrix\n(Firm 1, Firm 2)", pad=20)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, filename), dpi=300)
    plt.savefig(os.path.join(OUTPUT_DIR, filename.replace(".png", ".svg")))
    plt.close()

plot_payoff_matrix(p1_grid, p2_grid, strategies, nash_equilibria, "payoff_matrix.png")

# 5. Strategy Interaction Diagram (Heatmap style for "Aggression")
def plot_interaction_landscape(p1_g, p2_g, strats, filename):
    # Sum of payoffs (Joint Payoff)
    joint_payoff = p1_g + p2_g
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(joint_payoff, annot=True, fmt='g', cmap="RdYlGn", 
                xticklabels=strats, yticklabels=strats)
    plt.title("Joint Payoff Landscape\n(Higher = More Cooperative/Stable)")
    plt.xlabel("Firm 2 Strategy")
    plt.ylabel("Firm 1 Strategy")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, filename), dpi=300)
    plt.savefig(os.path.join(OUTPUT_DIR, filename.replace(".png", ".svg")))
    plt.close()

plot_interaction_landscape(p1_grid, p2_grid, strategies, "joint_payoff_landscape.png")

# 6. Repeated Game Stability Simulation (Qualitative Visualization)
# Simulate a sequence where Firm 1 deviates to Price Cut, and Firm 2 retaliates.
# Scenario:
# T=0: Maintain, Maintain (0, 0)
# T=1: Price Cut, Maintain (G, -L)  <- Firm 1 defects
# T=2: Price Cut, Price Cut (-C, -C) <- Firm 2 punishes (Tit-for-Tat)
# T=3: Price Cut, Price Cut (-C, -C) ...
# T=4: Product Diff, Product Diff (V, V) <- Shift to differentiation

scenarios = [
    ("Maintain", "Maintain"),
    ("Price Cut", "Maintain"),
    ("Price Cut", "Price Cut"),
    ("Price Cut", "Price Cut"),
    ("Product Diff", "Product Diff")
]

p1_scores = [payoff_matrix[s][0] for s in scenarios]
p2_scores = [payoff_matrix[s][1] for s in scenarios]
time_steps = ["T=0\nStatus Quo", "T=1\nDefection", "T=2\nPunishment", "T=3\nWar", "T=4\nRecovery"]

def plot_repeated_game_sim(p1_s, p2_s, labels, filename):
    plt.figure(figsize=(10, 6))
    plt.plot(labels, p1_s, marker='o', label='Firm 1 Payoff', linewidth=2, color='blue')
    plt.plot(labels, p2_s, marker='s', label='Firm 2 Payoff', linewidth=2, color='red', linestyle='--')
    
    plt.axhline(0, color='gray', linestyle=':', alpha=0.5)
    plt.title("Repeated Game Simulation: Defection & Retaliation Cycle")
    plt.ylabel("Ordinal Payoff")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, filename), dpi=300)
    plt.savefig(os.path.join(OUTPUT_DIR, filename.replace(".png", ".svg")))
    plt.close()

plot_repeated_game_sim(p1_scores, p2_scores, time_steps, "repeated_game_simulation.png")

print("Analysis Complete. Figures saved to:", OUTPUT_DIR)
