# def : get kospi 200 volatility data


import datetime
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

start = datetime.datetime(2019, 9, 1)
end = datetime.datetime(2023, 6, 2)
yf.pdr_override()

ticker = "^KS200"
df = pdr.get_data_yahoo(ticker, start, end)

# calculate rate of returns
df_chg = df.pct_change()


df_chg = df_chg['Adj Close'].dropna()
print(df_chg)

mu = np.mean(df_chg)

# calculate historical volatility (every monthly)
df_vol_monthly = df_chg.resample('M').apply(lambda x: np.std(x))
print(df_vol_monthly)

# visualize historical volatility
plt.plot(df_vol_monthly)
plt.show()

