import parse_data as pd
import numpy as np
import talib

from talib import abstract
from talib.abstract import *

def realtime_init (exchange, ticker, start_date, end_date, inc_delayed_volume):

	nump_hist_data = np.asarray(pd.pull_historical_data(ticker, start_date, end_date, True), dtype=float)

	inputs = {
  		'open': nump_hist_data[1],
    	'high': nump_hist_data[2],
    	'low': nump_hist_data[3],
    	'close': nump_hist_data[4],
    	'volume': nump_hist_data[5]
	}

	return [inputs, exchange, ticker, inc_delayed_volume]


def realtime_MA(ma_type, timeperiod, init):

	inputs = init[0]
	ma = abstract.MA
	output = MA(inputs, timeperiod, ma_type)
	inputs['close'][len(inputs['close'])-1] = pd.pull_live_data(init[1],init[2],init[3])[1]
	return output[len(output)-1]

def realtime_MACD(ma_type, fastperiod, slowperiod, signalperiod, init):

	inputs = init[0]
	macdreg = abstract.MACD
	macd, macdsignal, macdhist = MACD(inputs, fastperiod, slowperiod, signalperiod)
	inputs['close'][len(inputs['close'])-1] = pd.pull_live_data(init[1],init[2],init[3])[1]
	return [macd[len(macd)-1],macdsignal[len(macdsignal)-1],macdhist[len(macdhist)-1]]

def realtime_RSI(ma_type, timeperiod, init):

	inputs = init[0]
	rsi = abstract.RSI
	output = RSI(inputs, timeperiod, ma_type)
	inputs['close'][len(inputs['close'])-1] = pd.pull_live_data(init[1],init[2],init[3])[1]
	return output[len(output)-1]	

def realtime_BBANDS(ma_type, nbdevup, nbdevdn, timeperiod, init):

	inputs = init[0]
	bbands = abstract.BBANDS
	upperband, middleband, lowerband = BBANDS(inputs, timeperiod, nbdevup, nbdevdn, ma_type)
	inputs['close'][len(inputs['close'])-1] = pd.pull_live_data(init[1],init[2],init[3])[1]
	return [upperband[len(upperband)-1],middleband[len(middleband)-1],lowerband[len(lowerband)-1]]
