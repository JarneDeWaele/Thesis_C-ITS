import numpy as np
import random
import nashpy as nash

amount_of_strategies = 5
strategies=[0, 0.25, 0.50, 0.75, 1]


def generate_random_payoffmatrix(amount_of_strategies, share=1 / 7):
    return np.array([[np.round(np.random.randint(0, 100) * share, 0) for i in range(amount_of_strategies)]
                     for j in range(amount_of_strategies)])


player1_payoff_matrix = generate_random_payoffmatrix(amount_of_strategies)
player2_payoff_matrix = generate_random_payoffmatrix(amount_of_strategies)
# print(player1_payoff_matrix)

game1 = nash.Game(player1_payoff_matrix, player2_payoff_matrix)
pure_strategies = {}
amt_pure_strat = 0
for eq in game1.support_enumeration():
    pure_strat = True
    for i in range(2):
        if np.count_nonzero(eq[i] == 1) != 1:
            pure_strat = False

    if pure_strat:
        amt_pure_strat += 1
        pure_strategies[str(amt_pure_strat)] = [list(np.round(eq[0], 2)), list(np.round(eq[1], 2))]
        print(np.round(eq[0], 2), np.round(eq[1], 2))
print(pure_strategies)

# store equilibria
# update penetration
