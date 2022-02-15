# Tom-Demark-Indicator
Financial charting with Tom DeMark indicator overlay

In it's current form, TD_plotter.py looks at Bitcoin price data, but it could be easily
adapted to investigate any financial asset for which you have historical price data.

In addition to moving averages, exponential moving averages, MACD, volume, and volume trend,
TD_plotter.py will also display the lesser known Tom DeMark indicator on a candle chart.
Details on how this indicator works and how it should be interpreted can be found [here](http://cs.calstatela.edu/wiki/images/c/cb/DeMark.pdf).

By default TD_plotter.py will show 10 and 30 day exponential moving averages, MACD,
volume, and a 28 day moving average for volume.  These can be changed by commenting/uncommenting
clearly marked sections of the code.

Note that TD_plotter.py uses Python modules outside the standard library. Specifically,
[requests](http://docs.python-requests.org/en/master/), [matplotlib](https://matplotlib.org/), [numpy](https://www.numpy.org/), and [pandas](https://pandas.pydata.org/).

Sample data is provided in the price_data.csv file.  You should update this file with
current price information before running.  I recommend sourcing the data from [here](https://coinmarketcap.com/currencies/bitcoin/historical-data/).

To use this software, place all files in this repository into a common directory, set it
as your current working directory, then launch TD_plotter.py.
