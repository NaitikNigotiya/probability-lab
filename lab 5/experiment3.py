import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
N = 10_000
rolls = np.random.randint(1, 7, size=N)

running_avg = np.cumsum(rolls) / np.arange(1, N + 1)

E_X = 3.5

print("Running Average at Various n:")
print("=" * 38)
print(f"{'n':<10} {'X_n':<12} {'|X_n - E[X]|'}")
print("-" * 38)
for n in [10, 50, 100, 500, 1000, 5000, 10000]:
    avg = running_avg[n - 1]
    print(f"{n:<10} {avg:<12.4f} {abs(avg - E_X):.4f}")
print("=" * 38)
print(f"\nExpected value E[X] = {E_X}")
print(f"Final running average (n={N}): {running_avg[-1]:.4f}")

fig, ax = plt.subplots(figsize=(10, 5))

n_values = np.arange(1, N + 1)
ax.plot(n_values, running_avg, color='steelblue', linewidth=1.2,
        alpha=0.9, label=r'Running average $\bar{X}_n$')

ax.axhline(E_X, color='tomato', linewidth=2, linestyle='--',
           label=f'E[X] = {E_X}  (theoretical mean)')

ax.fill_between(n_values, E_X - 0.1, E_X + 0.1,
                color='tomato', alpha=0.1, label='±0.1 band around E[X]')

ax.set_xlabel('Number of Rolls  (n)', fontsize=12)
ax.set_ylabel(r'Running Average  $\bar{X}_n$', fontsize=12)
ax.set_title('Experiment 3 - Law of Large Numbers\n'
             r'Running Average of Die Rolls Converges to $E[X]=3.5$', fontsize=13)
ax.set_xscale('log')
ax.set_ylim(1, 6)
ax.legend(fontsize=11)
ax.grid(linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('experiment3_plot.png', dpi=150)
plt.show()
