import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
N = 10_000
outcomes = np.random.randint(1, 7, size=N)

faces = np.arange(1, 7)

frequencies = np.array([(outcomes == f).sum() for f in faces])
simulated_prob = frequencies / N
theoretical_prob = 1 / 6

print("=" * 55)
print(f"{'Outcome':<10} {'Frequency':<12} {'Sim. Prob':<14} {'Theo. Prob'}")
print("-" * 55)
for f, freq, sp in zip(faces, frequencies, simulated_prob):
    print(f"{f:<10} {freq:<12} {sp:<14.4f} {theoretical_prob:.4f}")
print("=" * 55)
print(f"\nTotal rolls : {N}")
print(f"Theoretical : {theoretical_prob:.4f}  ({theoretical_prob*100:.2f}%)")
print(f"Sim. range  : [{simulated_prob.min():.4f}, {simulated_prob.max():.4f}]")

fig, ax = plt.subplots(figsize=(8, 5))

bar_width = 0.35
x = np.arange(len(faces))

bars_sim  = ax.bar(x - bar_width/2, simulated_prob, bar_width,
                   label='Simulated Probability', color='steelblue', alpha=0.85)
bars_theo = ax.bar(x + bar_width/2, [theoretical_prob]*6, bar_width,
                   label='Theoretical Probability', color='tomato', alpha=0.85)

for bar in bars_sim:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.002,
            f'{bar.get_height():.4f}', ha='center', va='bottom', fontsize=8)

ax.set_xlabel('Die Face', fontsize=12)
ax.set_ylabel('Probability', fontsize=12)
ax.set_title('Experiment 1 - Probability Distribution of a Fair Die\n(10,000 Simulated Rolls)', fontsize=13)
ax.set_xticks(x)
ax.set_xticklabels(faces)
ax.set_ylim(0, 0.25)
ax.axhline(theoretical_prob, color='red', linestyle='--', linewidth=1.2,
           label=f'Theoretical = {theoretical_prob:.4f}')
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('experiment1_plot.png', dpi=150)
plt.show()
