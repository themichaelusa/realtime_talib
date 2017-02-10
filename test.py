import realtime_talib as rtt
from rtt import realtime, pipeline, indicators
import time

# nump_live_data = np.asarray(rtt.pull_live_data('NASDAQ','SPY', False))
# nump_hist_data= np.asarray(rtt.pull_historical_data('NVDA','2017-01-28','2017-02-01'))

# print nump_live_data[1]
# print nump_hist_data[0][0]
# print rtt.formatted_price('NYSE','AAPL')

init = realtime_init('NASDAQ','SPY','2016-01-01','2017-02-09',False)

while True:

	# Inputs:
	time = pull_live_data('NASDAQ','SPY', False)[0]
	price = pull_live_data('NASDAQ','SPY', False)[1]

	sma = MA(1, 3, init)[0]
	macdhist = MACD(1, 12, 26, 9, init)[2]
	upperband = BBANDS(1, 2, 2, 10, init)[0]
	rsi = RSI(1, 25, init)


	# Outputs:
	# 226.92278436
	# 0.0184101640085
	# 227.320467648
	# 62.1289093161






