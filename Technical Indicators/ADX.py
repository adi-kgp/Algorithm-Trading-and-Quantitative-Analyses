#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculation of ADX (Average Directional Index) Technical Indicator
@author: zerone
"""

import yfinance as yf
import numpy as np

# Download historical data for required stocks
tickers = ['AMZN', 'GOOG', 'MSFT']
ohlcv_data = {}

# looping over tickers and storing ohlcv dataframes for each ticker in dictionary
for ticker in tickers:
    temp = yf.download(ticker, period='1mo', interval='5m')
    temp.dropna(inplace=True)
    ohlcv_data[ticker] = temp

def ATR(DF, n=14):
    df = DF.copy()
    df['H-L'] = df['High'] - df['Low']
    df['H-PC'] = df['High'] - df['Adj Close'].shift(1)
    df['L-PC'] = df['Low'] - df['Adj Close'].shift(1)
    df['TR'] = df[['H-L', 'L-PC', 'H-PC']].max(axis=1, skipna=False)
    df['ATR'] = df['TR'].ewm(com=n, min_periods = n).mean()
    return df.loc[:, ['ATR']]

def ADX(DF, n=20):
    df = DF.copy()
    df['ATR'] = ATR(df, n)
    df['upmove'] = df['High'] - df['High'].shift(1)
    df['downmove'] = df['Low'].shift(1) - df['Low']
    df['+dm'] = np.where((df['upmove'] > df['downmove']) & (df['upmove'] > 0), df['upmove'], 0)
    df['-dm'] = np.where((df['downmove'] > df['upmove']) & (df['downmove'] > 0), df['downmove'], 0)
    df['+di'] = 100 * (df['+dm']/df['ATR']).ewm(com = n, min_periods=n).mean()
    df['-di'] = 100 * (df['-dm']/df['ATR']).ewm(com = n, min_periods=n).mean()
    df['ADX'] = 100 * abs((df['+di'] - df['-di'])/(df['+di'] + df['-di'])).ewm(com = n, min_periods=n).mean()
    return df['ADX']

for ticker in ohlcv_data:
    ohlcv_data[ticker]['ADX'] = ADX(ohlcv_data[ticker], 20)
    

    
    
    
    
    
    
    
    