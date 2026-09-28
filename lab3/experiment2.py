import numpy as np

np.random.seed(42)

# Box contains 5 red, 3 blue, 2 green balls
balls = ['R'] * 5 + ['B'] * 3 + ['G'] * 2
n_sim = 10000

# Simulate drawing a ball 10,000 times
draws = np.random.choice(balls, size=n_sim)

# Define events
A = (draws == 'R')          # A: ball is red
B = (draws != 'G')          # B: ball is not green
A_and_B = A & B

# Simulated probabilities
P_A = np.mean(A)
P_B = np.mean(B)
P_A_and_B = np.mean(A_and_B)
P_A_given_B = P_A_and_B / P_B

# Theoretical values
P_A_theory = 5 / 10
P_B_theory = 8 / 10
P_A_and_B_theory = 5 / 10
P_A_given_B_theory = (5 / 10) / (8 / 10)   # = 0.625

print("Experiment 2: Conditional Probability")
print("-" * 45)
print(f"P(A)        Simulated = {P_A:.4f}   | Theoretical = {P_A_theory:.4f}")
print(f"P(B)        Simulated = {P_B:.4f}   | Theoretical = {P_B_theory:.4f}")
print(f"P(A ∩ B)    Simulated = {P_A_and_B:.4f}   | Theoretical = {P_A_and_B_theory:.4f}")
print(f"P(A|B)      Simulated = {P_A_given_B:.4f}   | Theoretical = {P_A_given_B_theory:.4f}")