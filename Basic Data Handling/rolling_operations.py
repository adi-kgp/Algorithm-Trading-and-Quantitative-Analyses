#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Import OHLCV data and perform basic data operations
@author: arch_camen
"""

import datetime as dt
import pandas as pd
import yfinance as yf

stocks = ['AMZN', 'MSFT', 'META', 'GOOG']

start = dt.datetime.today() - dt.timedelta(4350)

end = dt.datetime.today() - dt.timedelta(700)

cl_price = pd.DataFrame()

for ticker in tickers:
    cl_price[ticker] = yf.download(ticker, start, end)['Adj Close']
    
cl_price.dropna(inplace=True)

daily_return = cl_price.pct_change()

simple_ma = daily_return.rolling(window=10).mean()
daily_return.rolling(window=10).std()
df = daily_return.rolling(window=10).max()
daily_return.rolling(window=10).min()

exponential_ma = daily_return.ewm(com=10, min_periods = 10).mean()

