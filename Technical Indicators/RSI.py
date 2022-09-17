#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Import OHLCV data and calculate RSI (Relative Strength Index) Technical Indicators
@author: arch_camen
"""

import yfinance as yf
import pandas as pd
import numpy as np

tickers = ['AMZN', 'GOOG', 'MSFT']

ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period='1mo', interval='5m')
    temp.dropna(how='any', inplace=True)
    ohlcv_data[ticker] = temp

def RSI(DF, n=14):
    df = DF.copy()
    df['Change'] = df['Adj Close'] - df['Adj Close'].shift(1)
    df['gain'] = np.where(df['Change']>=0, df['Change'],0)
    df['loss'] = np.where(df['Change']<0, -1*df['Change'],0)
    df['avgGain'] = df['gain'].ewm(alpha=1/n, min_periods=n).mean()
    df['avgLoss'] = df['loss'].ewm(alpha=1/n, min_periods=n).mean()
    df['rs'] = df['avgGain']/df['avgLoss']
    df['rsi'] = 100 - (100/(1+df['rs']))
    return df['rsi']

for ticker in ohlcv_data:
    ohlcv_data[ticker]['RSI'] = RSI(ohlcv_data[ticker])
    
    