import random

random.seed(42)  # for reproducibility

N = 10000
count_A = 0   # Sum equals 7
count_B = 0   # First die is even
count_AB = 0  # Both A and B occur

for _ in range(N):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    s = d1 + d2

    is_A = (s == 7)
    is_B = (d1 % 2 == 0)

    if is_A:
        count_A += 1
    if is_B:
        count_B += 1
    if is_A and is_B:
        count_AB += 1

P_A = count_A / N
P_B = count_B / N
P_AB = count_AB / N
P_A_given_B = count_AB / count_B

print(f"P(A) = {P_A:.4f}")
print(f"P(B) = {P_B:.4f}")
print(f"P(A ∩ B) = {P_AB:.4f}")
print(f"P(A|B) = {P_A_given_B:.4f}")