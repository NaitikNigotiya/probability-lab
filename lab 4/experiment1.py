import numpy as np
import pandas as pd

np.random.seed(42)

n_trials = 10000

# Define the boxes
box_A = ['Red'] * 8 + ['Blue'] * 2
box_B = ['Red'] * 5 + ['Blue'] * 5
box_C = ['Red'] * 2 + ['Blue'] * 8

# Randomly select a box
selected_boxes = np.random.choice(
    ['A', 'B', 'C'],
    size=n_trials
)

# Draw one ball from the selected box
draws = []

for box in selected_boxes:
    if box == 'A':
        ball = np.random.choice(box_A)
    elif box == 'B':
        ball = np.random.choice(box_B)
    else:
        ball = np.random.choice(box_C)

    draws.append(ball)

draws = np.array(draws)

# Filter Red-ball trials
red_trials = (draws == 'Red')
total_red = np.sum(red_trials)

# Count Red draws from each box
red_from_A = np.sum((selected_boxes == 'A') & red_trials)
red_from_B = np.sum((selected_boxes == 'B') & red_trials)
red_from_C = np.sum((selected_boxes == 'C') & red_trials)

# Simulated conditional probabilities
P_A_given_Red = red_from_A / total_red
P_B_given_Red = red_from_B / total_red
P_C_given_Red = red_from_C / total_red

# Theoretical probabilities
theoretical_P_A_given_Red = 8 / 15
theoretical_P_B_given_Red = 1 / 3
theoretical_P_C_given_Red = 2 / 15

# Comparison table
table = pd.DataFrame({
    "Probability": ["P(A|Red)", "P(B|Red)", "P(C|Red)"],
    "Theoretical": [
        theoretical_P_A_given_Red,
        theoretical_P_B_given_Red,
        theoretical_P_C_given_Red
    ],
    "Simulated": [
        P_A_given_Red,
        P_B_given_Red,
        P_C_given_Red
    ],
    "Difference": [
        abs(P_A_given_Red - theoretical_P_A_given_Red),
        abs(P_B_given_Red - theoretical_P_B_given_Red),
        abs(P_C_given_Red - theoretical_P_C_given_Red)
    ]
})

print(table)