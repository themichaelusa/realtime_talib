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
		self.LiveData = pl.pullLiveData(ticker, True)

	# ---------------- OVERLAP STUDIES ----------------------
	def MA(self, ma_type, timeperiod):

		inputs = ut.updateInputDict(self.HistoricalData, self.LiveData)
		ma = abstract.MA
		output = MA(inputs, timeperiod, ma_type)
		return ut.firstNotNAN(output)

	def BBANDS(self, ma_type, nbdevup, nbdevdn, timeperiod):

		inputs = ut.updateInputDict(self.HistoricalData, self.LiveData)
		bbands = abstract.BBANDS
		upperband, middleband, lowerband = BBANDS(inputs, timeperiod, nbdevup, nbdevdn, ma_type)
		return (ut.firstNotNAN(upperband), ut.firstNotNAN(middleband), ut.firstNotNAN(lowerband))

	# ---------------- MOMENTUM INDICATORS ----------------------
	def MACD(self, ma_type, fastperiod, slowperiod, signalperiod):

		inputs = ut.updateInputDict(self.HistoricalData, self.LiveData)
		macdreg = abstract.MACD
		macd, macdsignal, macdhist = MACD(inputs, fastperiod, slowperiod, signalperiod)
		return (ut.firstNotNAN(macd), ut.firstNotNAN(macdsignal), ut.firstNotNAN(macdhist))

	def RSI(self, timeperiod):

		inputs = ut.updateInputDict(self.HistoricalData, self.LiveData)
		rsi = abstract.RSI
		real = RSI(inputs, timeperiod)
		return ut.firstNotNAN(real)

	def ADX(self, timeperiod):

		inputs = ut.updateInputDict(self.HistoricalData, self.LiveData)
		adx = abstract.ADX
		real = ADX(inputs, timeperiod)
		return ut.firstNotNAN(real)

	def CCI(self, timeperiod):

		inputs = ut.updateInputDict(self.HistoricalData, self.LiveData)
		cci = abstract.CCI
		real = CCI(inputs, timeperiod)
		return ut.firstNotNAN(real)

	def CMO(self, timeperiod):

		inputs = ut.updateInputDict(self.HistoricalData, self.LiveData)
		cmo = abstract.CMO
		real = CMO(inputs, timeperiod)
		return ut.firstNotNAN(real)

	def AROON(self, timeperiod):

		inputs = ut.updateInputDict(self.HistoricalData, self.LiveData)
		aroon = abstract.AROON
		aroondown, aroonup = AROON(inputs, timeperiod)
		return (ut.firstNotNAN(aroondown),ut.firstNotNAN(aroonup))

	def STOCH(self, fastk_period, slowk_period, lowk_matype, lowk_matype, slowd_matype):

		inputs = ut.updateInputDict(self.HistoricalData, self.LiveData)
		stoch = abstract.STOCH
		slowk, slowd = STOCH(inputs, fastk_period, slowk_period, slowk_matype, lowk_matype, slowd_matype)
		return (ut.firstNotNAN(slowk), ut.firstNotNAN(slowd))

	def STOCHF(self, fastk_period, fastd_period, fastd_matype):

		inputs = ut.updateInputDict(self.HistoricalData, self.LiveData)
		stochf = abstract.STOCHF
		fastk, fastd = STOCHF(inputs, fastk_period, fastd_period, fastd_matype)
		return (ut.firstNotNAN(fastk), ut.firstNotNAN(fastd))

	def ULTOSC(self, timeperiod1, timeperiod2, timeperiod3):

		inputs = ut.updateInputDict(self.HistoricalData, self.LiveData)
		ultosc = abstract.ULTOSC
		real = ULTOSC(inputs, timeperiod1, timeperiod2, timeperiod3)
		return ut.firstNotNAN(real)

	def WILLR(self, timeperiod):

		inputs = ut.updateInputDict(self.HistoricalData, self.LiveData)
		willr = abstract.WILLR
		real = AROON(inputs, timeperiod)
		return ut.firstNotNAN(real)

	# ---------------- VOLATILITY INDICATORS ----------------------
	def ATR(self, timeperiod):

		inputs = ut.updateInputDict(self.HistoricalData, self.LiveData)
		atr = abstract.ATR
		real = ATR(inputs, timeperiod)
		return ut.firstNotNAN(real)

	def NATR(self, timeperiod):

		inputs = ut.updateInputDict(self.HistoricalData, self.LiveData)
		natr = abstract.NATR
		real  = NATR(inputs, timeperiod)
		return ut.firstNotNAN(real)

	def TRANGE(self):

		inputs = ut.updateInputDict(self.HistoricalData, self.LiveData)
		trange = abstract.TRANGE
		real = TRANGE(inputs)
		return ut.firstNotNAN(real)
