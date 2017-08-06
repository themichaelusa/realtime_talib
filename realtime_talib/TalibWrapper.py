import time
from realtime_talib import Utilities as utl

import numpy as np
import talib as tb
from talib.abstract import *

class TalibWrapper(object):

	def __init__(self, histOHLCV, indicator, iArgs):

		self.indicator, self.tbArgs = indicator, iArgs
		self.inputs, self.histCache = None, []
		self.histDF = histOHLCV
		self.generateInputDict()

		self.inputsDict = {
		'MA': MA, #tbArgs: timeperiod, ma_type
		'BBANDS': BBANDS, #tbArgs: timeperiod, nbdevup, nbdevdn, ma_type
		'HT_TRENDLINE': HT_TRENDLINE, #tbArgs: N/A
		'MAVP': MAVP, #tbArgs: periods, minperiod, maxperiod, matype
		'MIDPOINT': MIDPOINT, #tbArgs: timeperiod
		'MIDPRICE': MIDPRICE, #tbArgs: timeperiod
		'SAR': SAR, #tbArgs: acceleration, maximum
		'SAREXT': SAREXT, #tbArgs: too long, pls google it
		'ADX': ADX, #tbArgs: timeperiod
		'ADXR': ADXR, #tbArgs: timeperiod
		'APO': APO, #tbArgs: fastperiod, slowperiod, matype
		'AROON': AROON, #tbArgs: timeperiod
		'AROONOSC': AROONOSC, #tbArgs: timeperiod
		'BOP': BOP, #tbArgs: N/A
		'CCI': CCI, #tbArgs:  timeperiod
		'CMO': CMO, #tbArgs:  timeperiod
		'DX': DX, #tbArgs:  timeperiod
		'MACD': MACD, #tbArgs: fastperiod=12, slowperiod=26, signalperiod=9
		'MACDEXT': MACDEXT, #tbArgs: too long
		'MACDFIX': MACDFIX,  #tbArgs: signalperiod=9
		'MFI': MFI, #tbArgs: timeperiod
		'MINUS_DI': MINUS_DI, #tbArgs: timeperiod
		'MINUS_DM': MINUS_DM, #tbArgs: timeperiod
		'MOM': MOM, #tbArgs: timeperiod
		'PPO': PPO,  #tbArgs: fastperiod=12, slowperiod=26, matype=0, 
		'RSI': RSI, 
		'STOCH': STOCH,
		'STOCHF': STOCHF, 
		'STOCHRSI': STOCHRSI,
		'TRIX': TRIX,
		'ULTOSC': ULTOSC,
		'WILLR': WILLR,
		'AD': AD, 
		'ADOSC': ADOSC,
		'OBV': OBV,
		'ATR': ATR,
		'NATR': NATR,
		'TRANGE': TRANGE
		}    

	def generateInputDict(self): 

		self.inputs = {
		'open': np.asarray(self.histDF["open"].tolist(), dtype ='f8'),
		'high': np.asarray(self.histDF["high"].tolist(), dtype ='f8'),
		'low': np.asarray(self.histDF["low"].tolist(), dtype ='f8'),
		'close': np.asarray(self.histDF["close"].tolist(), dtype ='f8'),
		'volume': np.asarray(self.histDF["volume"].tolist(), dtype ='f8')
		}

	def getIndicator(self, histLag):

		outputs = self.inputsDict[self.indicator](self.inputs, *self.tbArgs)
		listOfLists = any(isinstance(sl, np.ndarray) for sl in outputs) 
		if (listOfLists == False): outputs = [outputs]
		outputs = [utl.removeNaN(techInd.tolist()) for techInd in outputs]
		
		if (histLag == utl.NO_LAG): return outputs
		else: return [utl.extendList(techInd, histLag) for techInd in outputs]

	def getRealtimeIndicator(self, tickData, indLag):

		if (self.histCache == []):

			tickData = [(k,v) for k,v in zip(utl.KEY_VALS, tickData)]
			tickData.insert(0, ('date', time.time()))
			self.histDF = self.histDF.append({k:float(v) for k,v in tickData}, ignore_index=True)

			self.generateInputDict()
			outputs = self.getIndicator(utl.NO_LAG) 
			self.histCache = utl.getCurrentInds(outputs, indLag)
		
		return self.histCache.pop()
