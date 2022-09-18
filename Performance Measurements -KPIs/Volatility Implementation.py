#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Measuring the volatility of a buy and hold strategy
@author: zerone
"""

# import necessary libraries
import yfinance as yf
import numpy as np

# Download historical data for required stocks
tickers = ['AMZN','GOOG','MSFT']
ohlcv_data = {}

# looping over tickers and storing OHLCV dataframe in dictionary
for ticker in tickers:
    temp = yf.download(ticker, period='7mo', interval='1d')
    temp.dropna(how='any', inplace=True)
    ohlcv_data[ticker] = temp
    
def volatility(DF):
    df = DF.copy()
    df['return'] = df['Adj Close'].pct_change()
    vol = df['return'].std() * np.sqrt(252)
    return vol

for ticker in ohlcv_data:
    print("Volatility of {} = {}".format(ticker, volatility(ohlcv_data[ticker])))
    