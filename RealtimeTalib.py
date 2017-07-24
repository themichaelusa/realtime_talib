import TalibWrapper as tbw

class Indicator(object):

	def __init__(self, dfOHLCV, ind, *indArgs):
		self.tbWrapper = tbw.TalibWrapper(ind, indArgs, dfOHLCV)

	def getRealtime(self, tickData, lag = 1):
		return self.tbWrapper.getRealtimeIndicator(tickData, lag)

	def getHistorical(self, lag = 1):
		output = self.tbWrapper.getIndicator(lag)
		if (len(output) == 1): return output[0]
		else: return output 
			