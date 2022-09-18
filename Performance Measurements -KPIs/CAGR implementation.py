#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementation of Compounded Annual Growth Returns (CAGR)
@author: zerone
"""

# import necessary libraries
import yfinance as yf

# Download historical data for required stocks
tickers = ['AMZN','GOOG','MSFT']
ohlcv_data = {}

# looping over tickers and storing OHLCV dataframe in dictionary
for ticker in tickers:
    temp = yf.download(ticker, period='7mo', interval='1d')
    temp.dropna(how='any', inplace=True)
    ohlcv_data[ticker] = temp
    
def CAGR(DF):
    df = DF.copy()
    df['return'] = df['Adj Close'].pct_change()
    df['cum_return'] = (1 + df['return']).cumprod()
    n = len(df)/252  # typical number of trading days in a year without factoring holidays
    CAGR = (df['cum_return'][-1])**(1/n) - 1
    return CAGR

for ticker in tickers:
    print("CAGR for {} = {}".format(ticker, CAGR(ohlcv_data[ticker])))
    
