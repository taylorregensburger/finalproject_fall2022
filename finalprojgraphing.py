
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

tickerstring = str(input("Input a ticker"))
periodlength = str(input("Input a length of time for the graph(1yr,6mo,2wk,5d")
tick = yf.Ticker(tickerstring)
tickhist = tick.history(period=periodlength)
tickhist['Close'].plot(title="apple stock price")
plt.show()



