#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Getting data for multiple stocks using yfinance library
@author: arch_camen
"""

import datetime as dt
import yfinance as yf
import pandas as pd

stocks = ["AMZN", "MSFT", "INTC", "GOOG", "INFY.NS", "3988.HK"]

start = dt.datetime.today() - dt.timedelta(360)
end = dt.datetime.today()

cl_price = pd.DataFrame() # empty dataframe which will be filled with closing prices

ohlcv_data = {}

# looping over tickers and creating a dataframe with closing prices
for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end)['Adj Close']
    
for ticker in stocks:
    ohlcv_data[ticker] = yf.download(ticker, start, end)
    
ohlcv_data['MSFT']['Open']








