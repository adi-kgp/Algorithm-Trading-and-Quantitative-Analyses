#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Getting data using yfinance library
@author: arch_camen
"""

import yfinance as yf

data = yf.download("MSFT", period="1mo", interval="5m")

data
