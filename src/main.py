# sudo setxkbmap be

import gambit
import pandas as pd
from src.payoff_builder import build_payoff_df
import os
from definitions import ASSETS_PATH


# brands = ["VW", "Stellantis", "Renault", "BMW", "Hyundai", "Toyota",
#            "Daimler", "Ford", "Volvo", "Nissan"]
# shares = [0.257, 0.227, 0.102, 0.072, 0.071, 0.069, 0.042, 0.051, 0.026, 0.02]

brands = ["VW", "Stellantis", "Renault", "BMW", "Hyundai", "Toyota"]
shares = [0.257, 0.227, 0.102, 0.072, 0.071, 0.069]

build_payoff_df(brands, shares)
results = pd.read_csv(os.path.join(ASSETS_PATH, 'payoffs.csv'), header=None,
                      skiprows=[0])  # Check later: possible to read from Github

print(results)

amt_players = len(brands)
amt_strat = 2  # Can later be made dynamic

g = gambit.Game.new_table([amt_players for i in range(amt_players)])

g.title = "Thesis Use Case 1"
for i in range(amt_players):
    g.players[i].label = brands[i]

print(g.players)

strategies = ["Wifi", "Cellular"]

# Only works for games with 2 strategies
for i in range(amt_players):
    for j in range(amt_strat):
        g.players[i].strategies[j].label = strategies[j]

print(g.strategies)

counter = 0

for a in range(amt_strat):
    for b in range(amt_strat):
        for c in range(amt_strat):
            for d in range(amt_strat):
                for e in range(amt_strat):
                    for f in range(amt_strat):
                        # for g in range(amt_strat):
                        #     for h in range(amt_strat):
                        #         for i in range(amt_strat):
                        #             for j in range(amt_strat):

                        for p in range(amt_players):
                            g[a, b, c, d, e, f][p] = int(results[amt_players + amt_strat + p][counter])
                            # g[i,j][p] = int(results[amt_players+1][counter])
                        counter += 1

#
#
# solver = gambit.nash.ExternalEnumMixedSolver().solve(g)
#
# for i in range(len(solver)):
#     print(solver[i])
