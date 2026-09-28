import random

random.seed(42)

ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suits = ['Hearts','Diamonds','Clubs','Spades']
deck = [(r, s) for r in ranks for s in suits]

N = 10000
count_A = 0    # Card is an Ace
count_B = 0    # Card is a Heart
count_AB = 0   # Card is Ace of Hearts

for _ in range(N):
    rank, suit = random.choice(deck)

    is_A = (rank == 'A')
    is_B = (suit == 'Hearts')

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