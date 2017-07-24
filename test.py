from RealtimeTalib import Indicator
import Utilities as utl
import pandas as pd
import ciso8601
import requests
import time
import gdax

POLO_HIST_DATA = 'https://poloniex.com/public?command=returnChartData&currencyPair={}&start={}&end={}&period={}'

def dateToUNIX(date): #format: "YYYYMMDD hhmmss"
	ts = ciso8601.parse_datetime(date)
	return time.mktime(ts.timetuple())

def getCryptoHistoricalData(currencyPair, startDate, endDate, interval):

	stDateUNIX = dateToUNIX(startDate)
	eDateUNIX = dateToUNIX(endDate)
	poloniexJsonURL = POLO_HIST_DATA.format(currencyPair, stDateUNIX, eDateUNIX, interval)
	poloniexJson = requests.get(poloniexJsonURL).json()

	histDataframe = pd.DataFrame.from_records(poloniexJson)
	histDataframe.drop('quoteVolume', axis=1, inplace=True)
	histDataframe.drop('weightedAverage', axis=1, inplace=True)
	histDataframe['date'] = histDataframe['date'].astype(float)

	return histDataframe[["date", "open", "high", "low", "close", "volume"]]

OHLCV = getCryptoHistoricalData("USDT_BTC", "20170720", '20170723', 300)
RT_MA = Indicator(OHLCV, "MA", 2, 1)

tickData = (2800, 2700, 2600, 2900, 9394)
print(RT_MA.getRealtime(tickData, 2)) # histData
