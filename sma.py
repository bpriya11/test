# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 17:29:42 2019

@author: DELL
"""

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pyEX as p
ticker = 'AMD'
timeframe = '1y'
df = p.chartDF(ticker, timeframe)
df = df[['close']]
df.reset_index(level=0, inplace=True)
df.columns=['ds','y']
plt.plot(df.ds, df.y)
plt.show()
rolling_mean = df.y.rolling(window=20).mean()
rolling_mean2 = df.y.rolling(window=50).mean()
plt.plot(df.ds, df.y, label='AMD')
plt.plot(df.ds, rolling_mean, label='AMD 20 Day SMA', color='orange')
plt.plot(df.ds, rolling_mean2, label='AMD 50 Day SMA', color='magenta')
plt.legend(loc='upper left')
plt.show()
