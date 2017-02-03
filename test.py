import realtime_talib as rtt

rtt.pull_live_data('NASDAQ','SPY')
rtt.pull_historical_data('SPY','2017-01-28','2017-02-01')
