#sudo setxkbmap be

import gambit
import numpy as np
import pandas as pd
import csv

results = pd.read_csv('payoffs.csv', header=None, skiprows = [0]) #Check later: possible to read from Github

print(results)
print(results.shape)

amt_players = int(results.shape[1]/2)
print(amt_players)
amt_strat = 2 #Can later be made dynamic

#Write m2 as below: look at strategic game and give rows for both players
#Alternative: give strategies per player --> player 2 has [2,0],[1,3] then, and transpose when calling
#gambit.Game.from_arrays(m1, transpose(m2))
# m1 = np.array([[3,1], [0,2]], dtype=gambit.Rational)
# m2 = np.array([[2,1], [0,3]], dtype=gambit.Rational)

g = gambit.Game.new_table([amt_players, amt_players])
# g = gambit.Game.from_arrays(m1, m2)
g.title = "Battle of the sexes example"
for i in range(amt_players):
    g.players[i].label = "Player "+ str(i+1)

strategies = ["Baseball", "Ballet"]

for i in range(amt_players):
    g.players[i].strategies[0].label = strategies[0]
    g.players[i].strategies[1].label = strategies[1]

# g.players[0].strategies[0].label = "Baseball"
# g.players[0].strategies[1].label = "Ballet"
# g.players[1].strategies[0].label = "Baseball"
# g.players[1].strategies[1].label = "Ballet"

# print(g.players[0].strategies)

#NEXT UP: payoffs in dictionary

print("Start init game")
counter = 0
print(amt_players)
for i in range(amt_players):
    for j in range(amt_players):
        # print(i, j)
        for p in range(amt_players):
            g[i,j][p] = int(results[amt_players+p][counter])
            # g[i,j][p] = int(results[amt_players+1][counter])
        counter += 1



solver = gambit.nash.ExternalEnumMixedSolver().solve(g)
for i in range(len(solver)):
    print(g.players)
for i in range(len(solver)):
    print(solver[i])