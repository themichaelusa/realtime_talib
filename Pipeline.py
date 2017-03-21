import datetime as dt
import pandas as pd
import numpy as np
import urllib
import json
import time

def pullLiveData(ticker, delayed_vol):

	# Exchange support: NASDAQ, NYSE
	url = "http://finance.google.com/finance/info?client=ig&q=NYSE%3A" + ticker

	raw_data = urllib.urlopen(url).read()
 	formatted_data = raw_data[5:len(raw_data)-3]
 	parsed_ticker_data = json.loads(formatted_data)

	# Yahoo Finance Delayed Volume (15-Min)
	if (delayed_vol == True):
		delayed_volume = urllib.urlopen('http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20%3D%20%22%27' + ticker + '%27%22%20&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=').read()
		parsed_delayed_volume = json.loads(delayed_volume)

		return (parsed_ticker_data['ltt'], parsed_ticker_data['l_cur'], parsed_delayed_volume['query']['results']['quote']['Volume'])
	
	else:
		return (parsed_ticker_data['ltt'], parsed_ticker_data['l_cur'])

def pullHistoricalData(ticker, end_date):

	# Date format: 'Year-Month-Date' --> '20170125'
	# Model URL = "http://real-chart.finance.yahoo.com/table.csv?s="+ ticker +"&d=2&e=01&f=2017&g=d&a=3&b=09&c=2012&ignore=.csv"

	dts = dateShift(end_date) # url dates (start, end)
	urlTicker = "http://real-chart.finance.yahoo.com/table.csv?s=" + ticker
	urlDates =  '&d='+ dts[1] +'&e=' + dts[2] + '&f='+dts[0]+'&g=d&a='+dts[4]+'&b='+dts[5]+'&c='+dts[3]+'&ignore=.csv'
	url = urlTicker + urlDates
	dataframe = pd.read_csv(url)

	dataframe.rename(columns={'Adj Close':'AdjClose'}, inplace=True)
	dataframe['Datetime'] = pd.to_datetime(dataframe['Date'])
	dataframe = dataframe.set_index('Datetime')
	dataframe = dataframe.drop(['Date'], axis=1)
	dataframe = dataframe.drop(['Close'], axis=1)
	dataframe = dataframe[['Open', 'AdjClose', 'High', 'Low', 'Volume']]

	talib_inputs = {
  	'open': np.asarray(dataframe["Open"].tolist()),
    'high': np.asarray(dataframe["High"].tolist()),
    'low': np.asarray(dataframe["Low"].tolist()),
    'close': np.asarray(dataframe["AdjClose"].tolist()),
    'volume': np.asarray(dataframe["Volume"].tolist())
	}

	return talib_inputs

def dateShift(end_date):

	# Date format: 'Year-Month-Date' --> '20170125'
	currentDate = str(dt.date.today())

	if (end_date == False): 
		dateOneYPrior = str(np.datetime64(currentDate) - np.timedelta64(365,'D'))

	else:
		formatted_end = dt.date(int(end_date[:4]), int(end_date[5:7]), int(end_date[8:10]))
		daysToEnd = -(np.busday_count(dt.date.today(), formatted_end, '1111111'))
		dateOneYPrior = str(np.datetime64(currentDate) - np.timedelta64(daysToEnd,'D'))

	curDY = str(currentDate[:4])
	curDM = str(currentDate[5:7])
	curDD = str(currentDate[8:10])

	priDY = str(dateOneYPrior[:4])
	priDM = str(dateOneYPrior[5:7])
	priDD = str(dateOneYPrior[8:10])

	return (curDY, curDM, curDD, priDY, priDM, priDD)
