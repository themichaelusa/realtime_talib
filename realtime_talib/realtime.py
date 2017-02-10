import pipeline as pl
import numpy as np
import thread

def realtime_init (exchange, ticker, start_date, end_date, inc_delayed_volume):

	nump_hist_data = pl.asarray(pd.pull_historical_data(ticker, start_date, end_date, True), dtype=float)

	inputs = {
  		'open': nump_hist_data[1],
    	'high': nump_hist_data[2],
    	'low': nump_hist_data[3],
    	'close': nump_hist_data[4],
    	'volume': nump_hist_data[5]
	}

	return [inputs, exchange, ticker, inc_delayed_volume, end_date]

def begin_thread(func_name, raw_params): thread.start_new_thread(func_name, raw_params)

