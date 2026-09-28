import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
N = 10_000
a, b = 10, 20

samples = np.random.uniform(a, b, size=N)

def theoretical_pdf(x, a=10, b=20):
    return np.where((x >= a) & (x <= b), 1.0 / (b - a), 0.0)

print("=" * 45)
print("Uniform Distribution U(10, 20)")
print("=" * 45)
print(f"Samples generated : {N}")
print(f"Theoretical mean  : {(a + b) / 2:.4f}")
print(f"Simulated mean    : {samples.mean():.4f}")
print(f"Theoretical std   : {(b - a) / np.sqrt(12):.4f}")
print(f"Simulated std     : {samples.std():.4f}")
print(f"Theoretical PDF   : 1/(b-a) = 1/{b-a} = {1/(b-a):.4f}")
print(f"Sample min        : {samples.min():.4f}")
print(f"Sample max        : {samples.max():.4f}")
print("=" * 45)

fig, ax = plt.subplots(figsize=(8, 5))

n_bins = 30
ax.hist(samples, bins=n_bins, density=True,
        color='steelblue', alpha=0.7, edgecolor='white',
        label='Simulated PDF (histogram)')

x_vals = np.linspace(8, 22, 500)
ax.plot(x_vals, theoretical_pdf(x_vals),
        color='tomato', linewidth=2.5, linestyle='--',
        label=r'Theoretical PDF: $f(x)=\frac{1}{10}$  for $10 \leq x \leq 20$')

ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('Probability Density  f(x)', fontsize=12)
ax.set_title('Experiment 4 - Medical Diagnostic Test Simulation\n'
             'Simulated vs Theoretical PDF for X ~ U(10, 20)', fontsize=13)
ax.set_xlim(7, 23)
ax.set_ylim(0, 0.18)
ax.axhline(1 / (b - a), color='tomato', linewidth=1, linestyle=':', alpha=0.6)
ax.legend(fontsize=10)
ax.grid(linestyle='--', alpha=0.5)

ax.annotate(f'f(x) = 1/10 = 0.1', xy=(15, 0.1), xytext=(16.5, 0.13),
            arrowprops=dict(arrowstyle='->', color='tomato'),
            fontsize=10, color='tomato')

plt.tight_layout()
plt.savefig('experiment4_plot.png', dpi=150)
plt.show()
