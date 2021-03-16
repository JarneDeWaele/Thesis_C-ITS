import numpy as np
import pandas as pd
import itertools

# amt_strategies = 2
# brands = ["VW", "Stellantis", "Renault", "BMW", "Hyundai", "Toyota",
#           "Daimler", "Ford", "Volvo", "Nissan"]
# brands = ["1", "2", "3", "4"]
# amt_brands = len(brands)
# shares = [0.257, 0.227, 0.102, 0.072, 0.071, 0.069, 0.042, 0.051, 0.026, 0.02]
# shares = [0.1, 0.2, 0.3, 0.4]
# shares_total = np.sum(shares)
# shares_norm = [i/shares_total for i in shares]

# brands_and_shares = dict(zip(brands, shares_norm))

def benefit(x, k=10):
    if x < 0 or x > 1:
        raise ValueError("x is not a valid number")
    else:
        return 1/(1+np.exp(-k*(x-0.5)))

def build_payoff_df(brands, shares, amt_strat = 2):

    b = len(brands)
    s = [i/sum(shares) for i in shares]
    list_of_strategies = [list(i) for i in itertools.product([0, 1], repeat = b)]

    for i in range(len(list_of_strategies)):

        wifi_share = 0
        cellular_share = 0
        for j in range(len(list_of_strategies[i])):
            if list_of_strategies[i][j] == 0:
                wifi_share += s[j]
            else:
                cellular_share += s[j]
        list_of_strategies[i].append(wifi_share)
        list_of_strategies[i].append(cellular_share)

        for p in range(b):
            b_strat_one = benefit(list_of_strategies[i][b])
            b_strat_two = benefit(list_of_strategies[i][b+1])
            if list_of_strategies[i][p] == 0:
                list_of_strategies[i].append(b_strat_one)
            else:
                list_of_strategies[i].append(b_strat_two)

    strats = ["Share strategy " + str(i) for i in range(amt_strat)]
    payoffs = ["Payoff P" +str(i+1) for i in range(b)]
    col = brands + strats + payoffs
    df = pd.DataFrame.from_records(list_of_strategies, columns=col)
    return df