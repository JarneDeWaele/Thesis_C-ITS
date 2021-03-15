import numpy as np
import pandas as pd
import itertools

amt_strategies = 2
brands = ["VW", "Stellantis", "Renault", "BMW", "Hyundai", "Toyota",
          "Daimler", "Ford", "Volvo", "Nissan"]
amt_brands = len(brands)
shares = [0.257, 0.227, 0.102, 0.072, 0.071, 0.069, 0.042, 0.051, 0.026, 0.02]
shares_total = np.sum(shares)
shares_norm = [i/shares_total for i in shares]

brands_and_shares = dict(zip(brands, shares_norm))

def benefit(x, k=10):
    if x < 0 or x > 1:
        raise ValueError("x is not a valid number")
    else:
        return 1/(1+np.exp(-k*(x-0.5)))

list_of_strategies = [list(i) for i in itertools.product([0, 1], repeat = amt_brands)]

for strategy in list_of_strategies:
    wifi_share = 0
    cellular_share = 0
    for i in range(len(strategy)):
        if strategy[i] == 0:
            wifi_share += shares_norm[i]
        else:
            cellular_share += shares_norm[i]
    list_of_strategies.append([wifi_share, cellular_share])

print(list_of_strategies)





