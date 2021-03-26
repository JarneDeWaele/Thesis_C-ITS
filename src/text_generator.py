import numpy as np
import os
from definitions import ASSETS_PATH
import pandas as pd
from src.payoff_builder import build_payoff_df


brands = ["VW", "Stellantis", "Renault", "BMW", "Hyundai", "Toyota",
           "Daimler", "Ford", "Volvo", "Nissan"]
shares = [0.257, 0.227, 0.102, 0.072, 0.071, 0.069, 0.042, 0.051, 0.026, 0.02]

def generate_text(amt_players, amt_strat=2, name='payoffs.csv'):

    results = pd.read_csv(os.path.join(ASSETS_PATH, name), header=None,
                          skiprows=[0])
    counter = 0
    file = open(os.path.join(ASSETS_PATH, 'text_generator.text'), "w")

    if amt_players == 2:
        for a in range(amt_strat):
            for b in range(amt_strat):
                for p in range(amt_players):
                    x = int((results[amt_players + amt_strat + p][counter]))
                    s = "g["+str(a)+", "+str(b)+"]["+str(p)+"] = "+str(x)
                    print(s)
                    file.write(s)
                    file.write("\n")
                counter += 1


    elif amt_players == 3:
        for a in range(amt_strat):
            for b in range(amt_strat):
                for c in range(amt_strat):
                    for p in range(amt_players):
                        x = int((results[amt_players + amt_strat + p][counter]))
                        s = "g[" + str(a) + ", " + str(b) +", " + str(c) + "][" + str(p) + "] = " + str(x)
                        print(s)
                        file.write(s)
                        file.write("\n")
                    counter += 1

    elif amt_players == 4:
        for a in range(amt_strat):
            for b in range(amt_strat):
                for c in range(amt_strat):
                    for d in range(amt_strat):
                        for p in range(amt_players):
                            x = int((results[amt_players + amt_strat + p][counter]))
                            s = "g[" + str(a) + ", " + str(b) +", " + str(c) + ", " + str(d) + "][" + str(p) + "] = " + str(x)
                            print(s)
                            file.write(s)
                            file.write("\n")
                        counter += 1

#Amount of players
n  = 2
build_payoff_df(n, name = 'test_payoffs.csv')
generate_text(n, name = 'test_payoffs.csv')