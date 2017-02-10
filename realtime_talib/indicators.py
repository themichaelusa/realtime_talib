import pipeline as 
import realtime as 

import talib
from talib import abstract
from talib.abstract import *


# ---------------- OVERLAP THREADING Wrappers ----------------------
def MA(ma_type, timeperiod, init): rt.begin_thread(rt_MA, locals().keys())
def BBANDS(ma_type, nbdevup, nbdevdn, timeperiod, init): rt.begin_thread(rt_BBANDS, locals().keys())

# ---------------- MOMENTUM THREADING Wrappers ----------------------
def MACD(ma_type, fastperiod, slowperiod, signalperiod, init): rt.begin_thread(rt_MACD, locals().keys())
def RSI(timeperiod, init): rt.begin_thread(rt_RSI, locals().keys())
def ADX(timeperiod, init): rt.begin_thread(rt_ADX, locals().keys())
def CCI(timeperiod, init): rt.begin_thread(rt_CCI, locals().keys())
def CMO(timeperiod, init): rt.begin_thread(rt_CMO, locals().keys())
def AROON(timeperiod, init): rt.begin_thread(rt_AROON, locals().keys())
def STOCH(fastk_period, slowk_period, lowk_matype, lowk_matype, slowd_matype, init): rt.begin_thread(rt_STOCH, locals().keys())
def STOCHF(fastk_period, fastd_period, fastd_matype, init): rt.begin_thread(rt_STOCHF, locals().keys())
def ULTOSC(timeperiod1, timeperiod2, timeperiod3, init): rt.begin_thread(rt_ULTOSC, locals().keys())
def WILLR(timeperiod, init): rt.begin_thread(rt_WILLR, locals().keys())

# ---------------- VOLATILITY THREADING Wrappers ----------------------
def ATR(timeperiod, init): rt.begin_thread(rt_ATR, locals().keys())
def NATR(timeperiod, init): rt.begin_thread(rt_NATR, locals().keys())
def TRANGE(init): rt.begin_thread(rt_TRANGE, locals().keys())


# ---------------- OVERLAP STUDIES ----------------------
def rt_MA(ma_type, timeperiod, init):

	inputs = init[0]
	ma = abstract.MA
	inputs['close'][len(inputs['close'])-1] = pl.pull_live_data(init[1],init[2],init[3])[1]
	real = MA(inputs, timeperiod, ma_type)
	return real[len(real)-1]

def rt_BBANDS(ma_type, nbdevup, nbdevdn, timeperiod, init):

	inputs = init[0]
	bbands = abstract.BBANDS
	inputs['close'][len(inputs['close'])-1] = pl.pull_live_data(init[1],init[2],init[3])[1]
	upperband, middleband, lowerband = BBANDS(inputs, timeperiod, nbdevup, nbdevdn, ma_type)
	return [upperband[len(upperband)-1],middleband[len(middleband)-1],lowerband[len(lowerband)-1]]

# ---------------- MOMENTUM INDICATORS ----------------------
def rt_MACD(ma_type, fastperiod, slowperiod, signalperiod, init):

	inputs = init[0]
	macdreg = abstract.MACD
	inputs['close'][len(inputs['close'])-1] = pl.pull_live_data(init[1],init[2],init[3])[1]
	macd, macdsignal, macdhist = MACD(inputs, fastperiod, slowperiod, signalperiod)
	return [macd[len(macd)-1],macdsignal[len(macdsignal)-1],macdhist[len(macdhist)-1]]

def rt_RSI(timeperiod, init):

	inputs = init[0]
	rsi = abstract.RSI
	inputs['close'][len(inputs['close'])-1] = pl.pull_live_data(init[1],init[2],init[3])[1]
	real = RSI(inputs, timeperiod)
	return real[len(real)-1]	

def rt_ADX(timeperiod, init):
	inputs = init[0]
	adx = abstract.ADX
	hist = rt.realtime_init('NASDAQ','SPY',init[4],init[4],False)
	inputs['high'][len(inputs['high'])-1] = hist[1]
	inputs['low'][len(inputs['low'])-1] = hist[2]
	inputs['close'][len(inputs['close'])-1] = pl.pull_live_data(init[1],init[2],init[3])[1]
	real = ADX(inputs, timeperiod)
	return real[len(real)-1]	

def rt_CCI(timeperiod, init):

	inputs = init[0]
	cci = abstract.CCI
	hist = rt.realtime_init('NASDAQ','SPY',init[4],init[4],False)
	inputs['high'][len(inputs['high'])-1] = hist[1]
	inputs['low'][len(inputs['low'])-1] = hist[2]
	inputs['close'][len(inputs['close'])-1] = pl.pull_live_data(init[1],init[2],init[3])[1]	
	real = CCI(inputs, timeperiod)
	return real[len(real)-1]		

def rt_CMO(timeperiod, init):

	inputs = init[0]
	cmo = abstract.CMO
	inputs['close'][len(inputs['close'])-1] = pl.pull_live_data(init[1],init[2],init[3])[1]
	real = CMO(inputs, timeperiod)
	return real[len(real)-1]

def rt_AROON(timeperiod, init):

	inputs = init[0]
	aroon = abstract.AROON
	hist = rt.realtime_init('NASDAQ','SPY',init[4],init[4],False)
	inputs['high'][len(inputs['high'])-1] = hist[1]
	inputs['low'][len(inputs['low'])-1] = hist[2]
	inputs['close'][len(inputs['close'])-1] = pl.pull_live_data(init[1],init[2],init[3])[1]
	aroondown, aroonup = AROON(inputs, timeperiod)
	return [aroonup[len(aroonup)-1],aroondown[len(aroondown)-1]]

def rt_STOCH(fastk_period, slowk_period, lowk_matype, lowk_matype, slowd_matype, init):

	inputs = init[0]
	stoch = abstract.STOCH
	hist = rt.realtime_init('NASDAQ','SPY',init[4],init[4],False)
	inputs['high'][len(inputs['high'])-1] = hist[1]
	inputs['low'][len(inputs['low'])-1] = hist[2]
	inputs['close'][len(inputs['close'])-1] = pl.pull_live_data(init[1],init[2],init[3])[1]
	slowk, slowd = STOCH(inputs, fastk_period, slowk_period, slowk_matype, lowk_matype, slowd_matype)
	return [slowk[len(slowk)-1],slowd[len(slowd)-1]]

def rt_STOCHF(fastk_period, fastd_period, fastd_matype, init):

	inputs = init[0]
	stochf = abstract.STOCHF
	hist = rt.realtime_init('NASDAQ','SPY',init[4],init[4],False)
	inputs['high'][len(inputs['high'])-1] = hist[1]
	inputs['low'][len(inputs['low'])-1] = hist[2]
	inputs['close'][len(inputs['close'])-1] = pl.pull_live_data(init[1],init[2],init[3])[1]
	fastk, fastd = STOCHF(inputs, fastk_period, fastd_period, fastd_matype)
	return [fastk[len(fastk)-1],fastd[len(fastd)-1]]

def rt_ULTOSC(timeperiod1, timeperiod2, timeperiod3, init):

	inputs = init[0]
	ultosc = abstract.ULTOSC
	hist = rt.realtime_init('NASDAQ','SPY',init[4],init[4],False)
	inputs['high'][len(inputs['high'])-1] = hist[1]
	inputs['low'][len(inputs['low'])-1] = hist[2]
	inputs['close'][len(inputs['close'])-1] = pl.pull_live_data(init[1],init[2],init[3])[1]
	real = ULTOSC(inputs, timeperiod1, timeperiod2, timeperiod3)
	return [real[len(real)-1]]

def rt_WILLR(timeperiod, init):

	inputs = init[0]
	willr = abstract.WILLR
	hist = rt.realtime_init('NASDAQ','SPY',init[4],init[4],False)
	inputs['high'][len(inputs['high'])-1] = hist[1]
	inputs['low'][len(inputs['low'])-1] = hist[2]
	inputs['close'][len(inputs['close'])-1] = pl.pull_live_data(init[1],init[2],init[3])[1]
	real = AROON(inputs, timeperiod)
	return [real[len(real)-1]]

# ---------------- VOLATILITY INDICATORS ----------------------
def rt_ATR(timeperiod, init):

	inputs = init[0]
	atr = abstract.ATR
	hist = rt.realtime_init('NASDAQ','SPY',init[4],init[4],False)
	inputs['high'][len(inputs['high'])-1] = hist[1]
	inputs['low'][len(inputs['low'])-1] = hist[2]
	inputs['close'][len(inputs['close'])-1] = pl.pull_live_data(init[1],init[2],init[3])[1]
	real = ATR(inputs, timeperiod)
	return [real[len(real)-1]]

def rt_NATR(timeperiod, init):

	inputs = init[0]
	natr = abstract.NATR
	hist = rt.realtime_init('NASDAQ','SPY',init[4],init[4],False)
	inputs['high'][len(inputs['high'])-1] = hist[1]
	inputs['low'][len(inputs['low'])-1] = hist[2]
	inputs['close'][len(inputs['close'])-1] = pl.pull_live_data(init[1],init[2],init[3])[1]
	real  = NATR(inputs, timeperiod)
	return [real[len(real)-1]]

def rt_TRANGE(init):

	inputs = init[0]
	trange = abstract.TRANGE
	hist = rt.realtime_init('NASDAQ','SPY',init[4],init[4],False)
	inputs['high'][len(inputs['high'])-1] = hist[1]
	inputs['low'][len(inputs['low'])-1] = hist[2]
	inputs['close'][len(inputs['close'])-1] = pl.pull_live_data(init[1],init[2],init[3])[1]
	real = TRANGE(inputs)
	return [real[len(real)-1]]




