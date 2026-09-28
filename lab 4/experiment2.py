import numpy as np

np.random.seed(42)
n = 100000

p_attack = 0.01
p_alert_attack = 0.95
p_alert_normal = 0.05

is_attack = np.random.rand(n) < p_attack
rand_alert = np.random.rand(n)
alert = np.where(is_attack, rand_alert < p_alert_attack, rand_alert < p_alert_normal)

total_alerts = np.sum(alert)
true_positives = np.sum(is_attack & alert)
false_positives = np.sum((~is_attack) & alert)

sim_p_alert = total_alerts / n
sim_p_attack_given_alert = true_positives / total_alerts

p_alert_theory = (0.01 * 0.95) + (0.99 * 0.05)
p_attack_given_alert_theory = (0.01 * 0.95) / p_alert_theory

print("Simulated Results:")
print(f"P(Alert)          = {sim_p_alert:.4f}")
print(f"P(Attack | Alert) = {sim_p_attack_given_alert:.4f} ({sim_p_attack_given_alert*100:.2f}%)")
print(f"False Positives   = {false_positives} / {total_alerts} ({false_positives/total_alerts*100:.2f}% of alerts)")

print("\nTheoretical Results (Bayes' Theorem):")
print(f"P(Alert)          = {p_alert_theory:.4f}")
print(f"P(Attack | Alert) = {p_attack_given_alert_theory:.4f} ({p_attack_given_alert_theory*100:.2f}%)")

print("\nEffect of False Positives:")
print("Since normal activities make up 99% of traffic, even a 5% false alarm rate")
print("generates ~4,950 false alerts vs ~950 true alerts. Thus, ~84% of alerts are false alarms.")
