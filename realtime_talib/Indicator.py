from .TalibWrapper import TalibWrapper

class Indicator(object):

	def __init__(self, dfOHLCV, ind, *indArgs):
		self.tbWrapper = TalibWrapper(dfOHLCV, ind, indArgs)

	def getRealtime(self, tickData, lag = 1):
		return self.tbWrapper.getRealtimeIndicator(tickData, lag)

	def getHistorical(self, lag = 1):
		output = self.tbWrapper.getIndicator(lag)
		if (len(output) == 1): return output[0]
		else: return output

	def getDataframe(self):
		return self.tbWrapper.histDF
			