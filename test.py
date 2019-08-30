import pandas as pd
import numpy as np


df = pd.read_csv('raw_data.txt', sep=',', encoding='utf-8', dtype='object')
print(len(df))
print(df.columns)