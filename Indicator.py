import talib
from talib import abstract
from talib.abstract import *

import pipeline as pl
import utilities as ut

class Indicator(object):

	def __init__(self, ticker, endDate = False):

		self.ticker = ticker
		self.endDate = endDate
		self.HistoricalData = pl.pullHistoricalData(ticker, endDate)
		self.UpdatedDict = ut.updateInputDict(ticker, endDate)

	# ---------------- OVERLAP STUDIES ----------------------
	def MA(self, ma_type, timeperiod):

		inputs = self.UpdatedDict
		ma = abstract.MA
		output = MA(inputs, timeperiod, ma_type)
		return ut.firstNotNAN(output)

	def BBANDS(self, ma_type, nbdevup, nbdevdn, timeperiod):

		inputs = self.UpdatedDict		
		bbands = abstract.BBANDS
		upperband, middleband, lowerband = BBANDS(inputs, timeperiod, nbdevup, nbdevdn, ma_type)
		return (ut.firstNotNAN(upperband), ut.firstNotNAN(middleband), ut.firstNotNAN(lowerband))

	# ---------------- MOMENTUM INDICATORS ----------------------
	def MACD(self, ma_type, fastperiod, slowperiod, signalperiod):

		inputs = self.UpdatedDict
		macdreg = abstract.MACD
		macd, macdsignal, macdhist = MACD(inputs, fastperiod, slowperiod, signalperiod)
		return (ut.firstNotNAN(macd), ut.firstNotNAN(macdsignal), ut.firstNotNAN(macdhist))

	def RSI(self, timeperiod):

		inputs = self.UpdatedDict
		rsi = abstract.RSI
		real = RSI(inputs, timeperiod)
		return ut.firstNotNAN(real)

	def ADX(self, timeperiod):

		inputs = self.UpdatedDict
		adx = abstract.ADX
		inputs['high'][0] = self.HistoricalData[1]
		inputs['low'][0] = self.HistoricalData[2]
		inputs['close'][0] = self.HistoricalData[3]
		real = ADX(inputs, timeperiod)
		return ut.firstNotNAN(real)

	def CCI(self, timeperiod):

		inputs = self.UpdatedDict
		cci = abstract.CCI
		inputs['high'][0] = self.HistoricalData[1]
		inputs['low'][0] = self.HistoricalData[2]
		inputs['close'][0] = self.HistoricalData[3]
		real = CCI(inputs, timeperiod)
		return ut.firstNotNAN(real)

	def CMO(self, timeperiod):

		inputs = self.UpdatedDict
		cmo = abstract.CMO
		real = CMO(inputs, timeperiod)
		return ut.firstNotNAN(real)

	def AROON(self, timeperiod):

		inputs = self.UpdatedDict
		aroon = abstract.AROON
		inputs['high'][0] = self.HistoricalData[1]
		inputs['low'][0] = self.HistoricalData[2]
		inputs['close'][0] = self.HistoricalData[3]
		aroondown, aroonup = AROON(inputs, timeperiod)
		return (ut.firstNotNAN(aroondown),ut.firstNotNAN(aroonup))

	def STOCH(self, fastk_period, slowk_period, lowk_matype, lowk_matype, slowd_matype):

		inputs = self.UpdatedDict
		stoch = abstract.STOCH
		inputs['high'][0] = self.HistoricalData[1]
		inputs['low'][0] = self.HistoricalData[2]
		inputs['close'][0] = self.HistoricalData[3]
		slowk, slowd = STOCH(inputs, fastk_period, slowk_period, slowk_matype, lowk_matype, slowd_matype)
		return (ut.firstNotNAN(slowk), ut.firstNotNAN(slowd))

	def STOCHF(self, fastk_period, fastd_period, fastd_matype):

		inputs = self.UpdatedDict
		stochf = abstract.STOCHF
		inputs['high'][0] = self.HistoricalData[1]
		inputs['low'][0] = self.HistoricalData[2]
		inputs['close'][0] = self.HistoricalData[3]
		fastk, fastd = STOCHF(inputs, fastk_period, fastd_period, fastd_matype)
		return (ut.firstNotNAN(fastk), ut.firstNotNAN(fastd))

	def ULTOSC(self, timeperiod1, timeperiod2, timeperiod3):

		inputs = self.UpdatedDict
		ultosc = abstract.ULTOSC
		inputs['high'][0] = self.HistoricalData[1]
		inputs['low'][0] = self.HistoricalData[2]
		inputs['close'][0] = self.HistoricalData[3]
		real = ULTOSC(inputs, timeperiod1, timeperiod2, timeperiod3)
		return ut.firstNotNAN(real)

	def WILLR(self, timeperiod):

		inputs = self.UpdatedDict
		willr = abstract.WILLR
		inputs['high'][0] = self.HistoricalData[1]
		inputs['low'][0] = self.HistoricalData[2]
		inputs['close'][0] = self.HistoricalData[3]
		real = AROON(inputs, timeperiod)
		return ut.firstNotNAN(real)

	# ---------------- VOLATILITY INDICATORS ----------------------
	def ATR(self, timeperiod):

		inputs = self.UpdatedDict
		atr = abstract.ATR
		inputs['high'][0] = self.HistoricalData[1]
		inputs['low'][0] = self.HistoricalData[2]
		inputs['close'][0] = self.HistoricalData[3]
		real = ATR(inputs, timeperiod)
		return ut.firstNotNAN(real)

	def NATR(self, timeperiod):

		inputs = self.UpdatedDict
		natr = abstract.NATR
		inputs['high'][0] = self.HistoricalData[1]
		inputs['low'][0] = self.HistoricalData[2]
		inputs['close'][0] = self.HistoricalData[3]
		real  = NATR(inputs, timeperiod)
		return ut.firstNotNAN(real)

	def TRANGE(self):

		inputs = self.UpdatedDict
		trange = abstract.TRANGE
		inputs['high'][0] = self.HistoricalData[1]
		inputs['low'][0] = self.HistoricalData[2]
		inputs['close'][0] = self.HistoricalData[3]
		real = TRANGE(inputs)
		return ut.firstNotNAN(real)

