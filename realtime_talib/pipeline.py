import urllib
import json

def pull_live_data(exchange, ticker, delayed_vol):

	# Exchange support: NASDAQ, NYSE
	url = "http://finance.google.com/finance/info?client=ig&q=" + exchange + "%3A" + ticker

	raw_data = urllib.urlopen(url).read()
 	formatted_data = raw_data[5:len(raw_data)-3]
 	parsed_ticker_data = json.loads(formatted_data)

	# Yahoo Finance Delayed Volume (15-Min)
	if delayed_vol == True:
		delayed_volume = urllib.urlopen('http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20%3D%20%22%27' + ticker + '%27%22%20&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=').read()
		parsed_delayed_volume = json.loads(delayed_volume)
		live_data = [parsed_ticker_data['ltt'],parsed_ticker_data['l_cur'],parsed_delayed_volume['query']['results']['quote']['Volume']]
		return live_data
	
	else:
		live_data = [parsed_ticker_data['ltt'],parsed_ticker_data['l_cur']]
		return live_data



def pull_historical_data(ticker, start_date, end_date, talib_use):

	# Date format: 'Year-Month-Date' --> '2017-01-25'
	url = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.historicaldata%20where%20symbol%20%3D%20%22" + ticker + "%22%20and%20startDate%20%3D%20%22" + start_date + "%22%20and%20endDate%20%3D%20%22" + end_date + "%22&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="

	raw_data = urllib.urlopen(url).read()
	parsed_ticker_data = json.loads(raw_data)

	date = parsed_ticker_data['query']['results']['quote'][0]['Date']  				
	open_price = parsed_ticker_data['query']['results']['quote'][0]['Open']  		    
	close_price = parsed_ticker_data['query']['results']['quote'][0]['Close']  	    
	high_price = parsed_ticker_data['query']['results']['quote'][0]['High']  		    
	low_price = parsed_ticker_data['query']['results']['quote'][0]['Low']  			
	volume = parsed_ticker_data['query']['results']['quote'][0]['Volume']  		

	end_raw = ['Date','Open','Close','High','Low','Volume']
	hist_data = [[date],[open_price],[close_price],[high_price],[low_price],[volume]]

	for i in range(len(hist_data)):
		for j in range(len(parsed_ticker_data['query']['results']['quote'])):
			hist_data[i].append(parsed_ticker_data['query']['results']['quote'][j][end_raw[i]])
		hist_data[i].reverse()

	if talib_use == True:
		for i in range(len(hist_data[0])):
			hist_data[0][i] = hist_data[0][i].replace('-','')
	
	return hist_data

	

def formatted_price(exchange, ticker):

	# Exchange support: NASDAQ, NYSE
	url = "http://finance.google.com/finance/info?client=ig&q="+ exchange + "%3A" + ticker

	raw_data = urllib.urlopen(url).read()
 	formatted_data = raw_data[5:len(raw_data)-3]
 	parsed_ticker_data = json.loads(formatted_data)

	return str(parsed_ticker_data['t'] + '|' +' Price: ' + parsed_ticker_data['l_cur'] + ' | Change: ' + parsed_ticker_data['cp'] + "%")	


def btc_data_pipeline():

	url = 'https://www.bitstamp.net/api/v2/ticker/btcusd'
	raw_data = urllib.urlopen(url).read()
 	parsed_btc_data = json.loads(raw_data)

 	live_btc_data = [parsed_btc_data['high'], parsed_btc_data['low'], parsed_btc_data['open'], parsed_btc_data['last'], parsed_btc_data['volume']]



	
