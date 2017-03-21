from threading import _Timer
import pipeline as pl
import math

class CustomTimer(_Timer):

    def __init__(self, interval, function, args=[], kwargs={}):

        self._original_function = function

        super(CustomTimer, self).__init__(
            interval, self._do_execute, args, kwargs)

    def _do_execute(self, *a, **kw):
        self.result = self._original_function(*a, **kw)

    def join(self):

        super(CustomTimer, self).join()
        return self.result

def updateInputDict(ticker, endDate):

	OrigInputDict = pl.pullHistoricalData(ticker, endDate)

	inputRefreshTimer = CustomTimer(1, pl.pullLiveData, (ticker, True))
	inputRefreshTimer.start()
	
	talib_inputs = inputRefreshTimer.join() 

	OrigInputDict['close'][0] = talib_inputs[1]
	OrigInputDict['volume'][0] = talib_inputs[2]

	return OrigInputDict

def firstNotNAN(talibOutput):

	for i in range(len(talibOutput)):
		if (math.isnan(talibOutput[i]) == False): 
			return talibOutput[i]
