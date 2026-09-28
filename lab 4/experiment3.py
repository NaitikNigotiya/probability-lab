import numpy as np

coins = {'Coin A': 0.50, 'Coin B': 0.70, 'Coin C': 0.90}
prior = 1 / 3

def bayesian_inference(sequence):
    h = sequence.count('H')
    t = sequence.count('T')
    
    likelihoods = {}
    for coin, p_h in coins.items():
        likelihoods[coin] = (p_h ** h) * ((1 - p_h) ** t)
    
    total_prob = sum(prior * l for l in likelihoods.values())
    posteriors = {coin: (prior * l) / total_prob for coin, l in likelihoods.items()}
    best_coin = max(posteriors, key=posteriors.get)
    return posteriors, best_coin

sequences = [
    ['H', 'H', 'H', 'T'],
    ['H', 'H', 'H', 'H', 'H'],
    ['T', 'T', 'H', 'T']
]

for seq in sequences:
    posteriors, best = bayesian_inference(seq)
    print(f"Sequence: {', '.join(seq)}")
    for coin, prob in posteriors.items():
        print(f"  P({coin} | Evidence) = {prob:.4f}")
    print(f"  Most Likely Coin: {best}\n")
