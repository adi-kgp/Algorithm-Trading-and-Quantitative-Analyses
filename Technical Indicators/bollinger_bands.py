#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementation of Bollinger Bands Technical Indicator
"""

import yfinance as yf

tickers = ['AMZN', 'GOOG', 'MSFT']
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period='1mo', interval='5m')
    temp.dropna(how='any', inplace=True)
    ohlcv_data[ticker] = temp
    
# Implementation of Bollinger bands
def BollingerBand(DF, n=14):
    df = DF.copy()
    df['MB'] = df['Adj Close'].rolling(n).mean()
    df['UB'] = df['MB'] + df['Adj Close'].rolling(n).std(ddof=0)*2
    df['LB'] = df['MB'] - df['Adj Close'].rolling(n).std(ddof=0)*2
    df['BB_width'] = df['UB'] - df['LB']
    return df[['MB', 'UB', 'LB', 'BB_width']]

for ticker in ohlcv_data:
    ohlcv_data[ticker][['MB', 'UB', 'LB', 'BB_Width']] = BollingerBand(ohlcv_data[ticker], 20)
    
