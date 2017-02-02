import realtime_talib as rtt

while True: 

	print rtt.pull_price('NYSE','SPY', 1)
