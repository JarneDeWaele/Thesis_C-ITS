import nashpy as nash
import numpy as np
import os
from definitions import ASSETS_PATH
from src.payoff import *

payoff_c2c_cc, payoff_5gaa = build_payoff_matrix()

print(payoff_c2c_cc)
print(payoff_5gaa)

phase0_game = nash.Game(payoff_c2c_cc, payoff_5gaa)
print(phase0_game)
for eq in phase0_game.vertex_enumeration():
    print(np.round(eq[0], 2), np.round(eq[1], 2))
