import indicators as ind
import pipeline as pl

ticker = 'SPY'
endDate = '2016-05-12'

HistData = pl.pullHistoricalData(ticker, endDate)
LiveData = pl.pullLiveData(ticker, True)

SPY_Ind = ind.Indicator(ticker, endDate)

print SPY_Ind.MA(0, 14)
print SPY_Ind.RSI(12)
