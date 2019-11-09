import requests
import pandas as pd
from functools import reduce

# This function retrieves: Companies profile (Price,Beta,Volume Average, Market Capitalisation, 
# Last Dividend, 52 week range, stock price change, stock price change in percentage,
# Company Name, Exchange, Description, Industry,Sector,CEO,Website and image).


def getStocksDescription(resource):
    url = "https://api.financialmodelingprep.com/api/company/profile/"
    res = requests.get(url+resource+"?datatype=json")
    return res.json()

#This function retrieves historical daily stock prices for each company

def getStocksQuote(resource):
    url = "https://api.financialmodelingprep.com/api/v3/historical-price-full/{}?serietype=line".format(resource)
    res = requests.get(url)
    return res.json()

#Selected tickers for retrieving data. Could be integrated into the function to dinamically retrieve companies.
#In this version, these will be the only companies to be shown.

selected_tickers = ["AMZN", "BIDU", "AAPL", "BABA",  "FB", "TWTR"]

#Arranging DataFrame

stocks_data = [getStocksDescription(e) for e in selected_tickers]
stocks_data2 = [stocks_data[i][e] for i in range(len(stocks_data)) for e in selected_tickers if e in stocks_data[i]]
df = pd.DataFrame(stocks_data2)

#Dropping unnecessary columns:

dropping = ["Beta", "Changes", "ChangesPerc", "LastDiv", "Price", "Range", "VolAvg", "date_bs_filed", "date_cs_filed", "date_is_filed","exchange"]
df = df.drop(dropping, axis=1)

#Rearranging DataFrame

df = df[['image', 'companyName', 'CEO', 'description', 'sector', 'website', 'MktCap']]
df["MktCap_USDbn"] = pd.to_numeric(df["MktCap"]).map(lambda x: x/1000000000).map(lambda x: round(x, 1))
df = df.drop("MktCap", axis=1)

#Exporting to .csv

df.to_csv("companies_description.csv")
print("Companies description csv generated.")

#Getting dataframe with historical stock prices

stocks_data = [getStocksQuote(e) for e in selected_tickers]
dataFramesStocks = [pd.DataFrame(e["historical"]) for e in stocks_data]

#Now each DataFrame is merged to have a common column for stock prices:

dfStocksConsolidated = reduce(lambda x, y: round(pd.merge(x,y, on="date", how="outer"), 1), dataFramesStocks)
dfStocksConsolidated.set_index("date", inplace=True)
dfStocksConsolidated.sort_index(ascending=False, inplace=True)
dfStocksConsolidated.columns = list(df["companyName"])

#Exporting to .csv
dfStocksConsolidated.to_csv("companies_stock_price.csv")
print("Companies stock price csv generated.")
