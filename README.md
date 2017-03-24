# Realtime TA-Lib

Fast & Lightweight library that calculates TA-Lib Technical Indicators live. **Built with Python 2.7!**

Provides an open source alternative to something like the TD Ameritrade API, and provides near-identical
results (when it works) and as a result could save each RTT user up to **$500,000** (supposed premium by TD API).

Really useful tool for algotrading or just tracking technical indicators in real-time.

Personally, I'm integrating this tool into a [BTC Trading Bot](https://github.com/shobrook/gecko) and using the live technical signals to form a usable Feature Space for an Recurrent Neural Network.

**Most Recent Update(3/20/2017):** 
* Added Indicator object to vastly simplify use of RTT (still issues with multiple indicators at once)
* Added Multithreading support via a custom use of the threading library Timer class
* Tons of refactoring and optimizing for readbility and performance (hopefully)

**Basic Overview:**
* Uses only native Python libraries (urllib, json) to scrape the Google/Yahoo Finance JSON/CSV data
* Parses JSON, converts CSV, and formats historical & live data into Pandas Dataframe
* Converts Dataframes to NumPy Arrays to form TA-Lib input dictionary
* Indicator Object specifies dataframe attributes via Ticker and Timeframe
* CustomTimer class splits the updating tasks into multiple threads
* [TA-Lib Abstract API](https://mrjbq7.github.io/ta-lib/abstract.html) does remainder of the grunt work

## Installation
```
pip install realtime_talib
```

## Documentation

### Example:

```python
import realtime_talib as rtt

SPY_Ind = rtt.Indicator("SPY", "2016-01-01")
	
print SPY_Ind.MA(1, 3)
print SPY_Ind.(1, 12, 26, 9)[2]
print SPY_Ind.(1, 12, 26, 9)[2]
print SPY_Ind.(1, 12, 26, 9)[2]
print SPY_Ind.BBANDS(1, 2, 2, 10)[1]
print SPY_Ind.RSI(1, 25)

...

 Terminal Outputs:
 226.92278436
 0.0184101640085
 227.320467648
 62.1289093161
```

### Basic Use & Indicator Functions:

* `Indicator(ticker, endDate)`

* `Indicator.MA(ma_type, timeperiod)`
* `Indicator.MACD(ma_type, fastperiod, slowperiod, signalperiod)`
* `Indicator.RSI(ma_type, timeperiod)`
* `Indicator.BBANDS(ma_type, nbdevup, nbdevdn, timeperiod)`

(Check the docs at the [RTT Temporary Indicator Doc](https://shrib.com/9G1SclqXIIwm2Ep) for the full list.)

### Other Useful Functions (Raw Data):

* `pullLiveData(exch, ticker)`
* `pullHistoricalData(ticker, endDate)`

pullLiveData returns a 1D List, and pullHistoricalData returns a [TA-Lib Input Dictionary](https://mrjbq7.github.io/ta-lib/abstract.html)
* `pullLiveData` format: `[ticker_data]`(0 = Current Time|1 = Current Price|2 = 15-Min Delayed Vol)

(Functions support NASDAQ and NYSE, and all the tickers under them.)

```python
import realtime_talib as rtt
from rtt import pipeline 

# Inputs:
print pullLiveData('NYSE','SPY')[1]
pullHistoricalData('NVDA','2015-02-03')[1][2] 
...

Terminal Outputs:
229.34
```

## TODO

- [ ] PyPI support (pip install...)
- [x] Multi-threading support
- [x] Parsing Yahoo Finance historical data
- [x] Calculating Indicators on the fly
- [ ] Add support for 40+ TA-Lib indicators
- [ ] Matplotlib & Pyfolio integration (possibly)
