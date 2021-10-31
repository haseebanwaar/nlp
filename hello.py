import pandas as pd
import numpy as np
import regex as re
import matplotlib.pyplot as plt

data = pd.read_csv("../input/large-random-tweets-from-pakistan/Random Tweets from Pakistan- Cleaned.csv")



data = data['full_text']

data = data.dropna()
data = data.drop_duplicates()

reg = re.compile(r'[\u0600-\u06ff]+',re.UNICODE)

datad = data.apply(lambda x:re.sub(reg,"",x))
data = data.apply(lambda x:re.sub(r'[  ]+'," ",x))
data = data.apply(lambda x:x.strip().lower())
