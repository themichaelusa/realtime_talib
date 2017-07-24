# Realtime TA-Lib

Fast & Lightweight library that calculates and updates TA-Lib Technical Indicators live, but also provides 
historical Technical Indicator data in the form of Pandas Dataframes.

Really useful tool for algotrading or just tracking technical indicators in real-time.

Best performance when used with concurrency libraries like asyncio. Here's where I [started](https://hackernoon.com/asyncio-for-the-working-python-developer-5c468e6e2e8e).

Also, check out my [concurrency tool](https://github.com/themichaelusa/AsyncPQ) (abstracts 90% of complexity away) for Python 3.

**Most Recent Update(7/24/2017):** 
* Rewrote entire library for use in Trinitum Architecture 
* Far faster and simpler than the previous version

## Installation
```
pip install realtime_talib
```

## Documentation

### Example:

```python
from realtime_talib import Indicator

OHLCV = .... (pandas dataframe with stock data)
rt_BBANDS = Indicator(OHLCV, "BBANDS", 2, 2, 5, 3)
rt_MA = Indicator(OHLCV, "AROON", 2, 1)
	
print(rt_MA.getHistorical(lag=1))
tickData = (2800, 2700, 2600, 2900, 9394) # format of OHLCV
print(rt_BBANDS.getRealtime(tickData, lag=2))
print(rt_BBANDS.getRealtime(tickData, lag=2))

...

 Terminal Outputs:
 [2320.1911391450003, 2322.398211915, ..., 2809.4632536955473]
 (2829.4632537420202, 2809.4632536955473, 2789.4632536490744)
 (2829.4632537420202, 2809.4632536955473, 2789.4632536490744)
	
```

## TODO

- [ ] PyPI support (pip install...)
- [ ] Add support for 40+ TA-Lib indicators
