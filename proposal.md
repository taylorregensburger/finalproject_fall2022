# Proposal

## What will (likely) be the title of your project?

Stock Valuation Chart Generator

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

The project is designed to output valuation graphs for any stocks listed on an American exchange, using the correct multiple data. 

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

The user will be prompted to input a stock ticker. The ticker will then be assigned to an industry, allowing the function to identify the proper multiple for the company (EV/EBITDA, P/Bk, P/E, etc). The software will then pull the valuation data from Bloomberg and chart it according to the multiple. Additionally, the 52 week high and low for the mulitple and price will be returned for the user.

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

N/A

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

Taylor Regensburger: tul19202@temple.edu - Zhengkang Fan
Anika Villivalam: tuo54923@temple.edu - Bin Li
Nick Bertel: tuk10799@temple.edu - Zhengkang Fan & Xinwen Zhang

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

For this project, a good outcome would be for a user to input a stock symbol and a well formatted data chart is outputted. The user in theory should be able to utilize this type of chart in a fundamental analysis. 

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

A better outcome would be to create a function that can properly recognize the different types of multiples in respective industries. In theory, if it were a Healthcare company it would be able to print both, EV/EBITDA and P/E but understand that P/Bk is not applicable. 

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

The user could tell the function the timeframe it wants to chart. Rather than having a blanket function of five years, one year charts could be created as well. The user would also be able to decide whether they would prefer a NTM (next twelve months) or LTM (last twelve months) valuation. 

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

Anika and Taylor will begin to figure out how to connect Bloomberg software and Python. To properly execute this, we must understand how to not only connect the two programs, but how to "clean" the data and prepare it to be charted. Nick will begin looking into how to formally create a chart in Python, as this is a skill we haven't formally used in class. From there, we will be able to combine these two skillsets to make an effetive program. 
