import numpy as np

np.random.seed(42)

n_sim = 10000

# Select box according to given probabilities
boxes = np.random.choice(['B1', 'B2', 'B3'], size=n_sim, p=[0.2, 0.5, 0.3])

# Draw a ball from the selected box
is_red = np.zeros(n_sim, dtype=bool)

for i, box in enumerate(boxes):
    if box == 'B1':
        is_red[i] = np.random.rand() < 0.8   # 8 red out of 10
    elif box == 'B2':
        is_red[i] = np.random.rand() < 0.5   # 5 red out of 10
    else:  # B3
        is_red[i] = np.random.rand() < 0.2   # 2 red out of 10

# Simulated probability
P_red_sim = np.mean(is_red)

# Theoretical probability (Law of Total Probability)
P_red_theory = (0.8 * 0.2) + (0.5 * 0.5) + (0.2 * 0.3)   # = 0.47

print("Experiment 3: Law of Total Probability")
print("-" * 45)
print(f"P(red)   Simulated  = {P_red_sim:.4f}")
print(f"P(red)   Theoretical = {P_red_theory:.4f}")