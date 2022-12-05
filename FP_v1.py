import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

intro = str(input("Would you like to learn more about stocks? Enter Y if Yes or N if No:"))
if intro == "Y":
    tickerstring = str(input("Input a Ticker Symbol:"))
    pd.options.display.width= None
    pd.options.display.max_columns= None
    pd.set_option('display.max_rows', 3000)
    pd.set_option('display.max_columns', 3000)
    tick = yf.Ticker(tickerstring)
    dict = tick.info
    df = pd.DataFrame.from_dict(dict,orient='index')
    df = df.reset_index()
else:
    print("Okay! Maybe next time!")
    quit()


def module_1 ():
    price = dict['currentPrice']
    price = round(price,2)
    print("\n""The current price of", tickerstring,"is $",price,".", "As a beginner investor, it is easy to assume that evaluating the Company's current trading price is the""\n""primary place to start. However, calculating a Company's valuation multiples provides a clearer indication of a Company's underlying fundamentals.""\n""You will see the price chart when you have completed all the modules!""\n")
    periodlength = str(input("Input a length of time for the graph(1y,6mo,2wk,5d,etc):"))
    tickhist = tick.history(period=periodlength)
    tickhist['Close'].plot(title=tickerstring+" Price Graph")


def module_2 ():
    earnings = dict['trailingEps']
    price = dict['currentPrice']
    sector = dict['sector']
    priceToEarnings = price / earnings
    evToEbitda = dict['enterpriseToEbitda']
    priceToBook = dict['priceToBook']
    z = ''
    if sector in ['Communication Services', 'Consumer Cyclical', 'Consumer Defensive', 'Healthcare', 'Technology']:
        z = 'Price to Earnings Ratio'
    if sector in ['Basic Materials', 'Energy', 'Industrials', 'Utilities']:
        z = 'EV to EBITDA Ratio'
    if sector in ['Financial Services','Real Estate']:
        z = 'Price to Book Ratio'
    y = print(tickerstring,"is a", sector,"company. For each sector, there are different ratios to value the company. For this company, the ratio used is a",z, ".")
    if sector in ['Communication Services', 'Consumer Cyclical', 'Consumer Defensive', 'Healthcare', 'Technology']:
        x = print("Price to Earnings Ratio is", round(priceToEarnings,2),"x" "\n")
    if sector in ['Basic Materials', 'Energy', 'Industrials', 'Utilities']:
        x = print("EV/EBITDA Ratio is",round(evToEbitda,2),"x" "\n")
    if sector in ['Financial Services','Real Estate']:
        x = print("Price to Book Ratio is",round(priceToBook,2),"x" "\n")
    return (y,x)

def module_3 ():
    print("\n""While you look at the multiple to look at the value of the company, there are other metrics you could also focus on, such as revenue and earnings.""\n""You want to keep an eye on what the street's expectations are for the Company")
    print(tick.earnings)
    print("Here's a table that shows the previous years revenue and earnings of Company, and 2022's expected.""\n""If you look at the table, you can calculate the percentage change between 2021 earnings and 2022 earnings to see whether there is expected growth in the Company.""\n")

def module_4():
    print("Making decisions on buying a stock can also be based on what Wall Street banks and analysts have been rating it.""\n""It's a good general idea to look at what other analysts think about the Company's future performance. Here's a list of analyst recommendations.")
    print(tick.recommendations.tail(5))
    print ("\n")

def module_5():
    print("With this, you can make a generalized consensus about the Company.""\n""Congrats! You have completed our beginner's module!")
    conclusion = input("Are you satisfied with your experience? Enter Y if Yes or N if No")
    if conclusion == "Y":
        print("Yay!")
    else:
        print("Okay thank you for your honest feedback. We are always looking to improve!")

second_Step= input("Would you like to learn about the Company's current price? Enter Y if Yes or N if No:")
if second_Step == "Y":
    module_1()
third_Step = input("Would you like to learn about a way to value a company based on the industry it is in? Enter Y if Yes or N if No:")
if third_Step == "Y":
    module_2()
fourth_Step = input("Would you like to learn about earnings? Enter Y if Yes or N if No:")
if fourth_Step == "Y":
    module_3()
fifth_Step = input("Would you like to learn about how analysts rate the Company's future performance? Enter Y if Yes or N if No:")
if fifth_Step == "Y":
    module_4()
module_5()

plt.show()

