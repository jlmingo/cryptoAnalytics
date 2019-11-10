import pandas as pd
#update paths in order to have access to files from src folder
#Reading dataframes. These will be consolidated.
df_crypto = pd.read_csv("../input/consolidated_coin_data.csv")
df_gold = pd.read_csv("../output/gold_quotes_historical.csv")
df_stocks = pd.read_csv("../output/companies_stock_price.csv")


#Dropping selected columns from Cryptocurrency DataFrame:
dropping = ["Open", "High", "Low", "Volume"]
df_crypto = df_crypto.drop(dropping, axis=1)

#Pivoting table to unify structure of dates / quotes; filtering and changing formates and column/index names.
df_crypto = df_crypto.pivot(index="Date", columns = "Currency", values= "Close")
df_crypto.columns = ['Binance-coin', 'Bitcoin', 'Bitcoin-cash', 'Cardano', 'EOS', 'Ethereum',
       'Litecoin', 'Ripple', 'Stellar', 'Tether']
df_crypto.index= pd.to_datetime(df_crypto.index)
df_crypto.sort_index(ascending=False, inplace=True)

#Dropping selected criptocurrencies
dropping = ['Stellar', 'Tether', 'Binance-coin','EOS']
df_crypto = df_crypto.drop(dropping, axis=1)
df_crypto = df_crypto.loc[df_crypto.index >= '2014-01-01']

#Formatting Gold DataFrame
df_gold.set_index('Date', inplace=True)
df_gold.rename(columns = {"Quote": "Gold"}, inplace=True)

#Formatting Stocks DataFrame
df_stocks.set_index('date', inplace=True)
df_stocks.index.names = ['Date']

#Consolidating DataFrame
df_final = df_stocks.join(df_gold).join(df_crypto)
df_final = df_final.loc[df_final.index < '2019-04-24']
col = ["AMZN", "BIDU", "AAPL", "BABA",  "FB", "TWTR", "GLD", "BTC", "BCH", "ADA", "ETH", "LTC", "XRT"]
df_final.columns = col

#Exporting to .csv
df_final.to_csv("df_final.csv")
print("DataFrame exported")