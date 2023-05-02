
# Simple Moving Average Crossover Strategy


Install dependencies:
```
pip install mplfinance
pip install yfinance
```

Just clone this repostiory and run the main script or open and run it into a jupyter book.

# Signals 
The strategy takes the close prices and gets the 5 and 30 moving averages in order to trigger BUY/SELL signals everytime the 5 crosses the 30 SMA.

The signals are going to be plotted into the chart using MPL Finance library.

