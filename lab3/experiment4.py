import numpy as np

np.random.seed(42)

n_sim = 100000

# Select factory for each component
factories = np.random.choice(['A', 'B', 'C'], size=n_sim, p=[0.5, 0.3, 0.2])

# Determine if the component is defective
is_defective = np.zeros(n_sim, dtype=bool)

for i, factory in enumerate(factories):
    if factory == 'A':
        is_defective[i] = np.random.rand() < 0.02
    elif factory == 'B':
        is_defective[i] = np.random.rand() < 0.05
    else:  # C
        is_defective[i] = np.random.rand() < 0.08

# Simulated probability
P_def_sim = np.mean(is_defective)

# Theoretical probability (Law of Total Probability)
P_def_theory = (0.02 * 0.5) + (0.05 * 0.3) + (0.08 * 0.2)   # = 0.041

print("Experiment 4: Factory Quality-Control")
print("-" * 45)
print(f"P(defective)  Simulated  = {P_def_sim:.5f}")
print(f"P(defective)  Theoretical = {P_def_theory:.5f}")