import realtime_talib as rtt
import pandas as pd
import numpy as np
# import talib as tb

nump_live_data = np.asarray(rtt.pull_live_data('NASDAQ','SPY', False))
# print nump_live_data

nump_hist_data= np.asarray(rtt.pull_historical_data('NVDA','2017-01-28','2017-02-01'))
# print nump_hist_data

print nump_live_data[1]
print nump_hist_data[0][0]
print rtt.formatted_price('NYSE','AAPL',5)
