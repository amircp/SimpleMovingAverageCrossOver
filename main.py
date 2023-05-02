import pandas as pd
import yfinance as yf
import mplfinance as mpf
import numpy as np


yf.pdr_override()

df = pdr.get_data_yahoo("^NDX", start='2020-01-01', end='2023-03-18')


stock_data = df


stock_data['SMA5'] = pta.sma(stock_data['Close'],5)
stock_data['SMA30'] = pta.sma(stock_data['Close'], 30)

stock_data['Buy'] = ((stock_data['SMA5'] > stock_data['SMA30']) & (stock_data['SMA5'].shift(1) <= stock_data['SMA30'].shift(1)))
stock_data['Sell'] = ((stock_data['SMA5'] < stock_data['SMA30']) & (stock_data['SMA5'].shift(1) >= stock_data['SMA30'].shift(1)))


stock_data['Buy_Price'] = np.where(stock_data['Buy'], stock_data['Close'], np.nan)
stock_data['Sell_Price'] = np.where(stock_data['Sell'], stock_data['Close'], np.nan)



sma5_plot = mpf.make_addplot(stock_data['SMA5'], color='blue', ylabel='Price')
sma30_plot = mpf.make_addplot(stock_data['SMA30'], color='red')

buy_plot = mpf.make_addplot(stock_data['Buy_Price'], type='scatter', markersize=100, marker='^', color='g')
sell_plot = mpf.make_addplot(stock_data['Sell_Price'], type='scatter', markersize=100, marker='v', color='r')

mpf.plot(stock_data, type='candle', style='binance', figsize=(10, 6), show_nontrading=False, addplot=[sma5_plot, sma30_plot, buy_plot, sell_plot], title='5 and 30 Period SMAs with Buy and Sell Signals', ylabel='Price')

stock_data.tail()


