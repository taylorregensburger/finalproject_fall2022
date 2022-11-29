
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

tickerstring = str(input("Input a ticker"))
tick = yf.Ticker(tickerstring)
tickhist = tick.history(period="6mo")
tickhist['Close'].plot(title="apple stock price")
plt.show()



