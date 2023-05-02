
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

![Captura de Pantalla 2023-05-02 a la(s) 12 11 56](https://user-images.githubusercontent.com/495849/235752058-85a9092e-0447-4427-bcbb-05ee00cad6c4.png)
