import math
from numpy import nan
import itertools as itert

NO_LAG = 1
KEY_VALS = ("open", "high", "low", "close", "volume")

#--------- LIST OPERATION METHODS------------

def extendList(listToExtend, extenMultiplier): 
	
	extendedListTuple = tuple(itert.repeat(listToExtend, extenMultiplier))
	return list(itert.chain.from_iterable(zip(*extendedListTuple)))

#--------- TA-LIB OPERATION METHODS---------------------

def removeNaN(listToChange):

	index = 0
	for i in listToChange:
		if (math.isnan(i) == True):
			index += 1
		else: 
			break
	
	return listToChange[index:]

def getCurrentInds(indsToParse, lag):
	
	currentInds = [tuple([float(i[len(i)-1]) for i in indsToParse])]
	laggedInds = extendList(currentInds, lag)
	return laggedInds
