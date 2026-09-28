import numpy as np

np.random.seed(42)
n = 10000

p_disease = 0.02
p_healthy = 0.98
p_pos_disease = 0.95
p_pos_healthy = 1.0 - 0.90

has_disease = np.random.rand(n) < p_disease
rand_test = np.random.rand(n)
test_pos = np.where(has_disease, rand_test < p_pos_disease, rand_test < p_pos_healthy)

sim_p_pos = np.mean(test_pos)
sim_p_disease_given_pos = np.sum(has_disease & test_pos) / np.sum(test_pos)

theory_p_pos = (p_disease * p_pos_disease) + (p_healthy * p_pos_healthy)
theory_p_disease_given_pos = (p_disease * p_pos_disease) / theory_p_pos

print("Simulated Results:")
print(f"P(Positive Test)           = {sim_p_pos:.4f}")
print(f"P(Disease | Positive Test) = {sim_p_disease_given_pos:.4f} ({sim_p_disease_given_pos*100:.2f}%)")

print("\nTheoretical Results (Bayes' Theorem):")
print(f"P(Positive Test)           = {theory_p_pos:.4f}")
print(f"P(Disease | Positive Test) = {theory_p_disease_given_pos:.4f} ({theory_p_disease_given_pos*100:.2f}%)")

print("\nComparison:")
print(f"P(Positive Test): Simulated = {sim_p_pos:.4f} | Theory = {theory_p_pos:.4f}")
print(f"P(Disease | Positive Test): Simulated = {sim_p_disease_given_pos:.4f} | Theory = {theory_p_disease_given_pos:.4f}")
