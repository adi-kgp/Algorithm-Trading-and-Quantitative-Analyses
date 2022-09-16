#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Handling nan values
@author: arch_camen
"""

import datetime as dt
import yfinance as yf
import pandas as pd

stocks = ['AMZN', 'MSFT', 'META', 'GOOG']

start = dt.datetime.today() - dt.timedelta(4350)

end = dt.datetime.today() - dt.timedelta(700)

cl_price = pd.DataFrame() # empty dataframe to be filled with closing prices of tickers

ohlcv_data = {} # empty dictionary to be filled with ohlcv dataframe for each ticker

# looping over tickers and creating a dataframe with close prices
for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end)['Adj Close']
    
    
# fill nan values
cl_price.fillna(method='bfill', axis=0, inplace=True)

# drop nan values
cl_price.dropna(axis=0, how='any')