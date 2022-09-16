#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Import OHLCV data and perform basic visualization
@author: arch_camen
"""

import datetime as dt
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

stocks = ['AMZN', 'MSFT', 'META', 'GOOG']

start = dt.datetime.today() - dt.timedelta(4350)

end = dt.datetime.today() - dt.timedelta(700)

cl_price = pd.DataFrame()

for ticker in tickers:
    cl_price[ticker] = yf.download(ticker, start, end)['Adj Close']
    
cl_price.dropna(inplace=True)

daily_return = cl_price.pct_change() # Creates dataframe with daily returns for each stock

cl_price.plot(subplots=True, layout=(2,2), title="Stock Price Evolution", grid=True)

daily_return.plot(subplots=True, layout=(2,2), title="Daily Returns Evolution")

# In quantitative finance, we visualize compounded returns

(1 + daily_return).cumprod().plot()
