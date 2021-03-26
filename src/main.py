# sudo setxkbmap be

import gambit
import pandas as pd
from src.payoff_builder import build_payoff_df
import os
from definitions import ASSETS_PATH
import numpy as np


brands = ["VW", "Stellantis", "Renault", "BMW", "Hyundai", "Toyota",
           "Daimler", "Ford", "Volvo", "Nissan"]
shares = [0.257, 0.227, 0.102, 0.072, 0.071, 0.069, 0.042, 0.051, 0.026, 0.02]

#Insert amount of players
amt_players = 2

build_payoff_df(n=amt_players)
results = pd.read_csv(os.path.join(ASSETS_PATH, 'payoffs.csv'), header=None,
                      skiprows=[0])


print(results)

amt_strat = 2  # Can later be made dynamic

g = gambit.Game.new_table([amt_players for i in range(amt_players)])

g.title = "Thesis Use Case 1"
for i in range(amt_players):
    g.players[i].label = brands[i]

print(g.players)

strategies = ["ITS-G5", "C-V2X"]

for i in range(amt_players):
    for j in range(amt_strat):
        g.players[i].strategies[j].label = strategies[j]

print(g.strategies)

#2 Players
g[0, 0][0] = 993
g[0, 0][1] = 993
g[0, 1][0] = 577
g[0, 1][1] = 423
g[1, 0][0] = 577
g[1, 0][1] = 423
g[1, 1][0] = 993
g[1, 1][1] = 993

#3 Players
# g[0, 0, 0][0] = 993
# g[0, 0, 0][1] = 993
# g[0, 0, 0][2] = 993
# g[0, 0, 1][0] = 963
# g[0, 0, 1][1] = 963
# g[0, 0, 1][2] = 37
# g[0, 1, 0][0] = 756
# g[0, 1, 0][1] = 244
# g[0, 1, 0][2] = 756
# g[0, 1, 1][0] = 352
# g[0, 1, 1][1] = 648
# g[0, 1, 1][2] = 648
# g[1, 0, 0][0] = 352
# g[1, 0, 0][1] = 648
# g[1, 0, 0][2] = 648
# g[1, 0, 1][0] = 756
# g[1, 0, 1][1] = 244
# g[1, 0, 1][2] = 756
# g[1, 1, 0][0] = 963
# g[1, 1, 0][1] = 963
# g[1, 1, 0][2] = 37
# g[1, 1, 1][0] = 993
# g[1, 1, 1][1] = 993
# g[1, 1, 1][2] = 993

#4 players
# g[0, 0, 0, 0][0] = 993
# g[0, 0, 0, 0][1] = 993
# g[0, 0, 0, 0][2] = 993
# g[0, 0, 0, 0][3] = 993
# g[0, 0, 0, 1][0] = 980
# g[0, 0, 0, 1][1] = 980
# g[0, 0, 0, 1][2] = 980
# g[0, 0, 0, 1][3] = 20
# g[0, 0, 1, 0][0] = 969
# g[0, 0, 1, 0][1] = 969
# g[0, 0, 1, 0][2] = 31
# g[0, 0, 1, 0][3] = 969
# g[0, 0, 1, 1][0] = 914
# g[0, 0, 1, 1][1] = 914
# g[0, 0, 1, 1][2] = 86
# g[0, 0, 1, 1][3] = 86
# g[0, 1, 0, 0][0] = 825
# g[0, 1, 0, 0][1] = 175
# g[0, 1, 0, 0][2] = 825
# g[0, 1, 0, 0][3] = 825
# g[0, 1, 0, 1][0] = 613
# g[0, 1, 0, 1][1] = 387
# g[0, 1, 0, 1][2] = 613
# g[0, 1, 0, 1][3] = 387
# g[0, 1, 1, 0][0] = 500
# g[0, 1, 1, 0][1] = 500
# g[0, 1, 1, 0][2] = 500
# g[0, 1, 1, 0][3] = 500
# g[0, 1, 1, 1][0] = 252
# g[0, 1, 1, 1][1] = 748
# g[0, 1, 1, 1][2] = 748
# g[0, 1, 1, 1][3] = 748
# g[1, 0, 0, 0][0] = 252
# g[1, 0, 0, 0][1] = 748
# g[1, 0, 0, 0][2] = 748
# g[1, 0, 0, 0][3] = 748
# g[1, 0, 0, 1][0] = 500
# g[1, 0, 0, 1][1] = 500
# g[1, 0, 0, 1][2] = 500
# g[1, 0, 0, 1][3] = 500
# g[1, 0, 1, 0][0] = 613
# g[1, 0, 1, 0][1] = 387
# g[1, 0, 1, 0][2] = 613
# g[1, 0, 1, 0][3] = 387
# g[1, 0, 1, 1][0] = 825
# g[1, 0, 1, 1][1] = 175
# g[1, 0, 1, 1][2] = 825
# g[1, 0, 1, 1][3] = 825
# g[1, 1, 0, 0][0] = 914
# g[1, 1, 0, 0][1] = 914
# g[1, 1, 0, 0][2] = 86
# g[1, 1, 0, 0][3] = 86
# g[1, 1, 0, 1][0] = 969
# g[1, 1, 0, 1][1] = 969
# g[1, 1, 0, 1][2] = 31
# g[1, 1, 0, 1][3] = 969
# g[1, 1, 1, 0][0] = 980
# g[1, 1, 1, 0][1] = 980
# g[1, 1, 1, 0][2] = 980
# g[1, 1, 1, 0][3] = 20
# g[1, 1, 1, 1][0] = 993
# g[1, 1, 1, 1][1] = 993
# g[1, 1, 1, 1][2] = 993
# g[1, 1, 1, 1][3] = 993

# counter = 0
#
# for a in range(amt_strat):
#     for b in range(amt_strat):
#         for c in range(amt_strat):
#             for d in range(amt_strat):
#             #     for e in range(amt_strat):
#             #         for f in range(amt_strat):
#                         # for g in range(amt_strat):
#                         #     for h in range(amt_strat):
#                         #         for i in range(amt_strat):
#                         #             for j in range(amt_strat):
#
#                 for p in range(amt_players):
#                     print(float(results[amt_players + amt_strat + p][counter]))
#                     g[a, b][p] = int((results[amt_players + amt_strat + p][counter]))
#                     # print(g[a, b][p])
#                     print((results[amt_players + amt_strat + p][counter]))
#                 counter += 1

solver = gambit.nash.ExternalEnumPureSolver().solve(g)
# solver = gambit.nash.enummixed_solve(g)
print(solver)
# solver = gambit.nash.ExternalEnumPureSolver()
# solver.solve(g)
# solver = gambit.nash.simpdiv_solve(g, external=False)
# solver = gambit.nash.enumpure_solve(g, use_strategic=True)
# print(solver)
for i in range(len(solver)):
    print(solver[i])
# print(len(solver))

