import pipeline as pl
import threading
import time
import math

refreshTimer = TimerClass()

class TimerClass(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()

    def run(self):
        while not self.event.is_set():
            # print "Refresh thread for: "
            self.event.wait(1)

    def stop(self):
        self.event.set()

def updateInputDict(histData, liveData):

	refreshTimer.start()
	refreshTimer.sleep(65)
	refreshTimer.stop()
	
	histData['close'][0] = liveData[1]
	histData['volume'][0] = liveData[2]

	return histData

def firstNotNAN(talibOutput):

	for i in range(len(talibOutput)):
		if (math.isnan(talibOutput[i]) == False): 
			return talibOutput[i]
