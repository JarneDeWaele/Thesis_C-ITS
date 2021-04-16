import nashpy as nash
import numpy as np
import os
from definitions import ASSETS_PATH
from src.payoff import *


def get_pure_nash_equilibria():
    # Step 1: build payoff matrices for both players (the 2 consortia)
    payoff_c2c_cc, payoff_5gaa = build_payoff_matrix()
    print(payoff_c2c_cc)
    print(payoff_5gaa)

    # Step 2: build the game using the nashpy library
    phase0_game = nash.Game(payoff_c2c_cc, payoff_5gaa)

    # Step 3: solve the game

    pure_strategies_c2c_cc= {}  # Used for storing all pure strategies
    pure_strategies_5gaa = {}
    pure_strategies = {}
    amt_pure_strat = 0  # Used as keys in the dictionary

    # print(phase0_game)

    for eq in phase0_game.support_enumeration():  # iterate over all equilibria
        # print(np.round(eq[0], 2), np.round(eq[1], 2))  # separate print of each equilibrium

        # Filter out the mixed strategies
        pure_strat = True
        for i in range(2):
            if np.count_nonzero(eq[i] == 1) != 1:
                pure_strat = False

        # Only store pure strategies in the dictionary
        if pure_strat:
            amt_pure_strat += 1
            pure_strategies[str(amt_pure_strat)] = [list(np.round(eq[0], 2)), list(np.round(eq[1], 2))]
            pure_strategies_c2c_cc["C2C-CC strategy " + str(amt_pure_strat)] = list(np.round(eq[0], 2))
            pure_strategies_5gaa["5GAA strategy " + str(amt_pure_strat)] = list(np.round(eq[1], 2))

    print(pure_strategies)
    print(pure_strategies_c2c_cc)
    print(pure_strategies_5gaa)

    # Step 4: update penetration

get_pure_nash_equilibria()

