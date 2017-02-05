import realtime_talib as rtt
import time


nump_live_data = np.asarray(rtt.pull_live_data('NASDAQ','SPY', False))
nump_hist_data= np.asarray(rtt.pull_historical_data('NVDA','2017-01-28','2017-02-01'))

print nump_live_data[1]
print nump_hist_data[0][0]
print rtt.formatted_price('NYSE','AAPL',5)


while True:

	print rtt.realtime_SMA('NYSE','SPY','2017-01-23','2017-02-04',2,False)
	time.sleep(1)
