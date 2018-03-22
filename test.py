
### COPIED FROM TRINITUM REPO ###

import time
import ciso8601
from datetime import datetime, timedelta

def getCurrentTimeUNIX():
	return time.time()

def dateToUNIX(date): #format: "YYYYMMDD hhmmss"
	ts = ciso8601.parse_datetime(date)
	return time.mktime(ts.timetuple())

def getCurrentDateStr():
	return time.strftime("%Y%m%d")

def datetimeDiff(datetime1, daysNum, order = "%Y%m%d"):
	formattedDT = datetime1[:10].replace("-", "")
	now = datetime.strptime(formattedDT, order).date()
	return str(now - timedelta(days=daysNum)).replace("-", "")

GDAX_TO_POLONIEX = {'BTC-USD': "USDT_BTC", 'LTC-USD': "USDT_LTC", 'ETH-USD': "USDT_ETC"}

class Pipeline(object):

	def __init__(self, interval): 
		self.interval = interval
		self.POLO_URL = 'https://poloniex.com/public'
		self.POLO_HIST_DATA = self.POLO_URL + '?command=returnChartData&currencyPair={}&start={}&end={}&period={}'

	def getCryptoHistoricalData(self, symbol, endTime, histPeriod, vwap=False):
		endTimeUNIX = dateToUNIX(endTime)
		startDate = getCurrentDateStr()
		priorDate = datetimeDiff(startDate, histPeriod)
		gdaxTicker = GDAX_TO_POLONIEX[symbol]

		stDateUNIX = dateToUNIX(priorDate)
		eDateUNIX = dateToUNIX(startDate)
		poloniexJsonURL = self.POLO_HIST_DATA.format(gdaxTicker, stDateUNIX, eDateUNIX, self.interval)

		import json
		import requests
		poloniexJson = requests.get(poloniexJsonURL).json()

		from pandas import DataFrame
		histDataframe = DataFrame.from_records(poloniexJson)
		histDataframe.drop('quoteVolume', axis=1, inplace=True)
		histDataframe.drop('weightedAverage', axis=1, inplace=True)
		histDataframe['date'] = histDataframe['date'].astype(float)

		return histDataframe[["date", "open", "high", "low", "close", "volume"]]

""" # TEST RTT
if __name__ == '__main__':
	pl = Pipeline(interval=300)
	df = pl.getCryptoHistoricalData(symbol='BTC-USD', endTime='20180201', histPeriod=30)

	from realtime_talib import Indicator
	obv = Indicator(df, 'OBV')
	trix = Indicator(df, 'TRIX', 20)
	rocr = Indicator(df, 'ROCR', 20)
	atr = Indicator(df, 'ATR', 20)

	print(obv.getHistorical(), trix.getHistorical(), rocr.getHistorical(), atr.getHistorical())
	test_ohlcv = [4000, 4100, 3900, 4200, 960]
	print(obv.getRealtime(test_ohlcv), trix.getRealtime(test_ohlcv), rocr.getRealtime(test_ohlcv), atr.getRealtime(test_ohlcv))
"""