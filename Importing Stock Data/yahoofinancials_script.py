#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Getting data using Yahoo Financials package
@author: arch_camen
"""

from yahoofinancials import YahooFinancials
import datetime as dt
import pandas as pd

all_tickers = ['MSFT', 'AAPL', 'CSCO', 'AMZN', 'INTC']

# Extracting stock data (historical close prices) for the stocks classified

close_prices = pd.DataFrame()

end_date = (dt.date.today()).strftime("%Y-%m-%d")
start_date = (dt.date.today() - dt.timedelta(1825)).strftime("%Y-%m-%d")

for ticker in all_tickers:
    yahoo_financials = YahooFinancials(ticker)
    json_obj = yahoo_financials.get_historical_price_data(start_date=start_date,
                                                          end_date = end_date, 
                                                          time_interval = "daily")
    ohlv = json_obj[ticker]['prices']
    temp = pd.DataFrame(ohlv)[['formatted_date', 'adjclose']]
    temp.set_index('formatted_date', inplace=True)
    temp.dropna(inplace=True)
    close_prices[ticker] = temp['adjclose']

