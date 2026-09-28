import numpy as np

np.random.seed(42)
n = 10000

die1 = np.random.randint(1, 7, n)
die2 = np.random.randint(1, 7, n)

A = (die1 + die2 == 8)
B = (die1 % 2 == 0)

P_A = np.mean(A)
P_B = np.mean(B)
P_A_and_B = np.mean(A & B)
P_A_given_B = P_A_and_B / P_B

print("Simulated Results:")
print(f"P(A)     = {P_A:.4f}")
print(f"P(B)     = {P_B:.4f}")
print(f"P(A∩B)   = {P_A_and_B:.4f}")
print(f"P(A|B)   = {P_A_given_B:.4f}")

print("\nTheoretical Results:")
print("P(A)     = 5/36 ≈ 0.1389")
print("P(B)     = 18/36 = 0.5000")
print("P(A∩B)   = 3/36 ≈ 0.0833")
print("P(A|B)   = 3/18 = 0.1667")