import urllib
import json
import time

def pull_price (exch, ticker, refresh_rate):

	if (exch == 'NASDAQ'):
		url = "http://finance.google.com/finance/info?client=ig&q=NASDAQ%3A" + ticker

	elif (exch == 'NYSE'):
		url = "http://finance.google.com/finance/info?client=ig&q=NYSE%3A" + ticker

	raw_data = urllib.urlopen(url).read()
	formatted_data = raw_data[5:len(raw_data)-3]
	parsed_ticker_data= json.loads(formatted_data)

	return str((parsed_ticker_data['t'] + '|' +' Price: ' + parsed_ticker_data['l_cur'] + ' | Change: ' + parsed_ticker_data['cp'] + "%"))
	time.sleep(refresh_rate)

	






