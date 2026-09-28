import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
N = 10_000
outcomes = np.random.randint(1, 7, size=N)

faces = np.arange(1, 7)

empirical_cdf = np.array([(outcomes <= x).sum() / N for x in faces])
theoretical_cdf = faces / 6

print("=" * 50)
print(f"{'x':<8} {'Empirical F(x)':<20} {'Theoretical F(x)'}")
print("-" * 50)
for x, emp, theo in zip(faces, empirical_cdf, theoretical_cdf):
    print(f"{x:<8} {emp:<20.4f} {theo:.4f}")
print("=" * 50)

fig, ax = plt.subplots(figsize=(8, 5))

x_step = np.concatenate([[0], faces, [7]])
emp_step = np.concatenate([[0], empirical_cdf, [1]])
ax.step(x_step, emp_step, where='post', color='steelblue',
        linewidth=2.5, label='Empirical CDF', zorder=3)

ax.plot(faces, empirical_cdf, 'o', color='steelblue', markersize=8, zorder=4)

theo_step = np.concatenate([[0], theoretical_cdf, [1]])
ax.step(x_step, theo_step, where='post', color='tomato',
        linewidth=2, linestyle='--', label='Theoretical CDF', zorder=2)

ax.plot(faces, theoretical_cdf, 's', color='tomato', markersize=8, zorder=4)

ax.set_xlabel('x  (Die face)', fontsize=12)
ax.set_ylabel('F(x) = P(X ≤ x)', fontsize=12)
ax.set_title('Experiment 2 - Empirical vs Theoretical CDF\n(10,000 Simulated Rolls)', fontsize=13)
ax.set_xticks(faces)
ax.set_yticks(np.round(theoretical_cdf, 4))
ax.set_xlim(0, 7)
ax.set_ylim(-0.05, 1.1)
ax.legend(fontsize=11)
ax.grid(linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('experiment2_plot.png', dpi=150)
plt.show()
