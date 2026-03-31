
import pandas as pd
import yfinance as yf
import numpy as np
from dtaidistance import dtw
import matplotlib.pyplot as plt
ticker_1 = yf.Ticker("TSLA")
ticker_2 = yf.Ticker("AMZN")

data_1 = ticker_1.history(period="1y")
data_2 = ticker_2.history(period="1y")

series_1 = data_1['Close'].values
series_2 = data_2['Close'].values
print("Missing values in TSLA series:", np.isnan(series_1).sum())
print("Missing values in AMZN series:", np.isnan(series_2).sum())

series_1 = pd.Series(series_1).ffill().values
series_2 = pd.Series(series_2).ffill().values

min_length = min(len(series_1), len(series_2))
series_1 = series_1[:min_length]
series_2 = series_2[:min_length]
distance = dtw.distance(series_1, series_2)
print(f"DTW distance between TSLA and AMZN: {distance}")
