import os

# set pandas display options
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # project root
ASSETS_PATH = os.path.join(ROOT_DIR, 'assets')
