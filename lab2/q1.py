import random

results = []

for i in range(10000):
    t1 = random.choice(['H', 'T'])
    t2 = random.choice(['H', 'T'])
    results.append((t1, t2))

print("First 10 results:")
print(results[:10])


# Q2
import itertools

# Two coin tosses
sample_space_2 = list(itertools.product(["H", "T"], repeat=2))
print("Two tosses:", sample_space_2)

sample_space_3 = list(itertools.product(["H", "T"], repeat=3))
print("Three tosses:", sample_space_3)


# Q3
A = {"HH", "HT"}
B = {"HH", "TH"}

print("A =", A)
print("B =", B)


# Q4
import random

N = 10000

A_count = 0
B_count = 0
AB_count = 0

for i in range(N):
    toss1 = random.choice(["H", "T"])
    toss2 = random.choice(["H", "T"])

    if toss1 == "H":
        A_count += 1

    if toss2 == "H":
        B_count += 1

    if toss1 == "H" and toss2 == "H":
        AB_count += 1

P_A = A_count / N
P_B = B_count / N
P_AB = AB_count / N

print("P(A) =", P_A)
print("P(B) =", P_B)
print("P(A ∩ B) =", P_AB)


# Q5
import random

N = 10000

A_count = 0
B_count = 0
AB_count = 0

for i in range(N):
    toss1 = random.choice(["H", "T"])
    toss2 = random.choice(["H", "T"])

    if toss1 == "H":
        A_count += 1

    if toss2 == "H":
        B_count += 1

    if toss1 == "H" and toss2 == "H":
        AB_count += 1

P_A = A_count / N
P_B = B_count / N
P_AB = AB_count / N

print("P(A) =", P_A)
print("P(B) =", P_B)
print("P(A ∩ B) =", P_AB)
print("P(A) × P(B) =", P_A * P_B)

if abs(P_AB - (P_A * P_B)) < 0.01:
    print("A and B are independent")
else:
    print("A and B are not independent")
