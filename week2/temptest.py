import datetime
import numpy as np
import pandas as pd
import requests

df = pd.read_excel('schools.xlsx')
df = df.drop(df.columns[[0]], axis=1)

print(df)
