# Realtime TA-Lib

A Lightweight Google/Yahoo Finance scraper that calculates TA-Lib Technical Indicators live.

The Quantopian and Pipeline API's are confusing at first, backtrader is confusing... the list goes on.
It's pretty easy to get overwhelmed.

Personally, I think this could be a really useful tool for a beginner in algotrading. 

## Installation
```
pip install realtime_talib
```

## Usage
```
import realtime_talib as rtt
```
Useful Functions:

- pull_price(exchange, ticker, refresh_rate)

(Supports either NASDAQ or NYSE, and all the tickers that fall under it. Refresh rate is in seconds.)
```
print rtt.pull_price ('NYSE','SPY',5)
```

## TODO

-  Parsing Yahoo Finance historical data
-  Calculating Indicators on the fly
-  matplotlib & pyfolio integration (possibly)

