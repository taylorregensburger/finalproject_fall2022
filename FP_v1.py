import pandas as pd
import yfinance_ez as yf
import matplotlib.pyplot as plt

#this is just setting up the data frame, only need to change the line highlited
tickerstring = str(input("Input a Ticker Symbol:"))
pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)
tick = yf.Ticker(tickerstring)#change this line to a ticker "amzn" and such
dict = tick.info
df = pd.DataFrame.from_dict(dict,orient='index')
df = df.reset_index()
#print (df)
#df.set_index("index", inplace = True)    #this line is to be able to do the highlighted line below


sector = dict['sector']
#print(sector)
price = dict['currentPrice']
print("The current price of", tickerstring,"is $",price,".", "As a beginner investor, it is easy to assume that evaluating the Company's current trading price is the""\n""primary place to start. However, calculating a Company's valuation multiples provides a clearer indication of a Company's underlying fundamentals.", "\n")

earnings = dict['trailingEps']
priceToEarnings = price / earnings


evToEbitda = dict['enterpriseToEbitda']
priceToBook = dict['priceToBook']

def company ():
    z = ''
    if sector in ['Communication Services', 'Consumer Cyclical', 'Consumer Defensive', 'Healthcare', 'Technology']:
        z = 'Price to Earnings Ratio'
    if sector in ['Basic Materials', 'Energy', 'Industrials', 'Utilities']:
        z = 'EV to EBITDA Ratio'
    if sector in ['Financial Services','Real Estate']:
        z = 'Price to Book Ratio'
    y = print(tickerstring, "is a", sector,"company. For each sector, there are different ratios to value the company. For this company, the ratio used is a",z, ".")
    if sector in ['Communication Services', 'Consumer Cyclical', 'Consumer Defensive', 'Healthcare', 'Technology']:
        x = print("Price to Earnings Ratio is ", round(priceToEarnings,2))
        z = 'Price to Earnings Ratio'
    if sector in ['Basic Materials', 'Energy', 'Industrials', 'Utilities']:
        x = print(round(evToEbitda,2))
        z = 'EV to EBITDA Ratio'
    if sector in ['Financial Services','Real Estate']:
        x = print(round(priceToBook,2))
        z = 'Price to Book Ratio'
    return (y,x)
company()

periodlength = str(input("Input a length of time for the graph(1yr,6mo,2wk,5d):"))
tickhist = tick.get_history(period=periodlength)
tickhist['Close'].plot(title="apple stock price")
plt.show()


#print(df)
#ebitda = df.loc['ebitda']   #this needs line above to work, change ebitda to find other data
#print(ebitda)



#indexing the complete list based on left column
#this line is the best way to index, it only shows a single number


#currentprice = df.loc['currentPrice'] # this is same as 2 above, indexing by name
#print(currentprice)

#print (dict['revenuePerShare'])
#print (dict['currentPrice'])

