# Realtime TA-Lib

A Lightweight Google/Yahoo Finance scraper that calculates TA-Lib Technical Indicators live.

The Quantopian and Pipeline API's are confusing at first, backtrader is confusing... the list goes on.
It's pretty easy to get overwhelmed.

Personally, I think this could be a really useful tool for a beginner in algotrading. 

Experienced back-testers might also find this useful, as it only relies on native Python Libraries and is much
simpler to use (and fiddle with) than most ticker data retrieval libraries on github.

## Installation
```
pip install realtime_talib
```

## Usage
```
import realtime_talib as rtt
```
### Useful Functions:

* `pull_live_data(exch, ticker)`
* `pull_historical_data(ticker, start_date, end_date)`
* `print_price(exch, ticker, refresh_rate)`

pull_live_data returns a 1D List, and pull_historical_data returns a 2D List.
* `pull_live_data` format: '[ticker_data]'  (E.g, Current Time, Realtime Price, 15-Min Delayed Volume)
* `pull_historical_data` format: '[day][ticker_data]' (E.g, Date, Open, Close, High, Low, Volume)

(Fuctions support NASDAQ and NYSE, and all the tickers under them. Refresh rate is in seconds.)
```
rtt.pull_live_data('NASDAQ','SPY')
rtt.pull_historical_data('SPY','2017-01-28','2017-02-01')
rtt.pull_price ('NYSE','SPY',5)
```

## TODO

*  ~~Parsing Yahoo Finance historical data~~
*  Calculating Indicators on the fly
*  matplotlib & pyfolio integration (possibly)
