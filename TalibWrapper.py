import time
import numpy as np
import pandas as pd
import Utilities as utl

import talib as tb
from talib.abstract import *

class TalibWrapper(object):

	def __init__(self, indicator, iArgs, histOHLCV):

		self.indicator, self.tbArgs = indicator, iArgs
		self.inputs, self.histCache = None, []
		self.histDF = histOHLCV
		self.generateInputDict()

		self.inputsDict = {
		'MA': MA, #tbArgs:  ma_type, timeperiod
		'BBANDS': BBANDS, #tbArgs: timeperiod, nbdevup, nbdevdn, ma_type
		'AROON': AROON
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

		try:

			outputs = self.inputsDict[self.indicator](self.inputs, *self.tbArgs)
			listOfLists = any(isinstance(sl, list) for sl in outputs)

			if (not listOfLists): outputs = [outputs]
			outputs = [utl.removeNaN(techInd.tolist()) for techInd in outputs]
			outputs = [utl.extendList(techInd, histLag) for techInd in outputs]

			return outputs

		except ValueError: pass

	def getRealtimeIndicator(self, tickData, indLag):

		if (self.histCache == []):

			tickData = [(k,v) for k,v in zip(utl.KEY_VALS, tickData)]
			tickData.insert(0, ('date', time.time()))
			self.histDF = self.histDF.append({k:float(v) for k,v in tickData}, ignore_index=True)

			self.generateInputDict()
			outputs = self.getIndicator(indLag) 
			self.histCache = utl.getCurrentInds(outputs, indLag)
		
		return self.histCache.pop()
