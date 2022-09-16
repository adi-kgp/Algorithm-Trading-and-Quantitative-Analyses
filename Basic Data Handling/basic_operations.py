#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Basic Data Operations

@author: arch_camen
"""

import datetime as dt
import yfinance as yf
import pandas as pd

stocks = ['AMZN', 'MSFT', 'META', 'GOOG']
start = dt.datetime.today() - dt.timedelta(4350)
end = dt.datetime.today() - dt.timedelta(365)

cl_price = pd.DataFrame() # empty dataframe to be filled with closing prices of tickers

ohlcv_data = {} # empty dictionary to be filled with ohlcv dataframe for each ticker

# looping over tickers and creating a dataframe with close prices
for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end)['Adj Close']
    
#drop nan values

cl_price.dropna(axis=0, how='any', inplace=True)

## Basic Stats
# mean
cl_price.mean()

# std
cl_price.std()

# median
cl_price.median()

cl_price.describe()

daily_return = cl_price.pct_change()

# daily_return = cl_price/cl_price.shift(1) - 1 i e. (present - old)/old

# mean of daily returns makes much more sense in financial domain
daily_return.mean()

daily_return.std()




