import realtime_talib as rtt
import time

# nump_live_data = np.asarray(rtt.pull_live_data('NASDAQ','SPY', False))
# nump_hist_data= np.asarray(rtt.pull_historical_data('NVDA','2017-01-28','2017-02-01'))

# print nump_live_data[1]
# print nump_hist_data[0][0]
# print rtt.formatted_price('NYSE','AAPL',5)

while True:

	init = rtt.realtime_init('NASDAQ','SPY','2017-01-28','2017-02-01',False)
	
	print rtt.realtime_MA(1, 3, init)
	print rtt.realtime_MACD(1, 12, 26, 9, init)[2]
	print rtt.realtime_BBANDS(1, 2, 2, 10, init)[1]
	print rtt.realtime_RSI(1, 25, init)

	time.sleep(1)
