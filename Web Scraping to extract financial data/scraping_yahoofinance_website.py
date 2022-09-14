#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Getting financial data from yahoo finance using web scraping
@author: arch_camen
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

tickers = ["AAPL", "FB", "CSCO", "INFY.NS", "3988.HK"]

income_statement_dict = {}
balancesheet_dict = {}
cashflow_statement_dict = {}

for ticker in tickers:    
    #scraping income statement
    url = "https://finance.yahoo.com/quote/{}/financials?p={}".format(ticker, ticker)
    income_statement = {}
    table_title = {}
    
    headers = {"User-Agent": "Chrome/104.0.5112.110"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content, "html.parser")
    tabl = soup.find_all("div", {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    for t in tabl:
        heading = t.find_all("div", {"class": "D(tbr) C($primaryColor)"})
        for top_row in heading:
            table_title[top_row.get_text(separator="|").split("|")[0]] = top_row.get_text(separator="|").split("|")[1:]
        rows = t.find_all("div", {"class":"D(tbr) fi-row Bgc($hoverBgColor):h"})
        for row in rows:
            income_statement[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[1:]

    temp = pd.DataFrame(income_statement).T
    temp.columns = table_title["Breakdown"]
    income_statement_dict[ticker] = temp
    
    #scraping balance sheet
    url = "https://finance.yahoo.com/quote/{}/balance-sheet?p={}".format(ticker, ticker)
    balance_sheet = {}
    bs_table_title = {}
    headers = {"User-Agent": "Chrome/104.0.5112.110"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content, "html.parser")
    for t in tabl:
        heading = t.find_all("div", {"class": "D(tbr) C($primaryColor)"})
        for top_row in heading:
            bs_table_title[top_row.get_text(separator="|").split("|")[0]] = top_row.get_text(separator="|").split("|")[1:]
        rows = t.find_all("div", {"class":"D(tbr) fi-row Bgc($hoverBgColor):h"})
        for row in rows:
            balance_sheet[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[1:]

    temp = pd.DataFrame(balance_sheet).T
    temp.columns = bs_table_title["Breakdown"]
    balancesheet_dict[ticker] = temp
    
    #scraping cashflow statement
    url = "https://finance.yahoo.com/quote/{}/cash-flow?p={}".format(ticker, ticker)
    cashflow_statement = {}
    cf_table_title = {}
    headers = {"User-Agent": "Chrome/104.0.5112.110"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content, "html.parser")
    for t in tabl:
        heading = t.find_all("div", {"class": "D(tbr) C($primaryColor)"})
        for top_row in heading:
            cf_table_title[top_row.get_text(separator="|").split("|")[0]] = top_row.get_text(separator="|").split("|")[1:]
        rows = t.find_all("div", {"class":"D(tbr) fi-row Bgc($hoverBgColor):h"})
        for row in rows:
            cashflow_statement[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[1:]

    temp = pd.DataFrame(cashflow_statement).T
    temp.columns = cf_table_title["Breakdown"]
    cashflow_statement_dict[ticker] = temp