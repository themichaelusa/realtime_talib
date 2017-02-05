import parse_data as pd
import numpy as np
import talib
import time 

from talib import abstract
from talib.abstract import *

def realtime_init (ticker, start_date, end_date):
	nump_hist_data = np.asarray(pd.pull_historical_data(ticker, start_date, end_date, True), dtype=float)

	inputs = {
  		'open': nump_hist_data[0],
    	'high': nump_hist_data[1],
    	'low': nump_hist_data[2],
    	'close': nump_hist_data[3],
    	'volume': nump_hist_data[4]
	}

	return inputs


def realtime_SMA(exchange, ticker, start_date, end_date, timeperiod, inc_delayed_volume):

	inputs = realtime_init(ticker,start_date,end_date) 
	sma = abstract.SMA
	output = SMA(inputs, timeperiod)
	inputs['close'][len(inputs['close'])-1] = pd.pull_live_data(exchange,ticker,inc_delayed_volume)[1]
	return output[len(output)-1]

def realtime_EMA(exchange, ticker, start_date, end_date, timeperiod, inc_delayed_volume):

	inputs = realtime_init(ticker,start_date,end_date) 
	ema = abstract.EMA
	output = EMA(inputs, timeperiod)
	inputs['close'][len(inputs['close'])-1] = pd.pull_live_data(exchange,ticker,inc_delayed_volume)[1]
	return output[len(output)-1]	

def realtime_DEMA(exchange, ticker, start_date, end_date, timeperiod, inc_delayed_volume):

	inputs = realtime_init(ticker,start_date,end_date) 
	dema = abstract.DEMA
	output = DEMA(inputs, timeperiod)
	inputs['close'][len(inputs['close'])-1] = pd.pull_live_data(exchange,ticker,inc_delayed_volume)[1]
	return output[len(output)-1]	

def realtime_TEMA(exchange, ticker, start_date, end_date, timeperiod, inc_delayed_volume):

	inputs = realtime_init(ticker,start_date,end_date) 
	tema = abstract.TEMA
	output = TEMA(inputs, timeperiod)
	inputs['close'][len(inputs['close'])-1] = pd.pull_live_data(exchange,ticker,inc_delayed_volume)[1]
	return output[len(output)-1]	

