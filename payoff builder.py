import numpy as np
import pandas as pd

amt_strategies = 2
brands = ["VW", "Stellantis", "Renault", "BMW", "Hyundai", "Toyota",
          "Daimler", "Ford", "Volvo", "Nissan"]
shares = [0.257, 0.227, 0.102, 0.072, 0.071, 0.069, 0.042, 0.051, 0.026, 0.02]
shares_total = np.sum(shares)
shares_norm = [i/shares_total for i in brands]

brands_and_shares = dict(zip(brands, shares_norm))


