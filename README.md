# Crypto Analyzer

## Description

This program takes daily prices for selected cryptocurrencies, tech companies' stocks and gold.

- Inputs come from:
    1. Database with daily pricing of all criptocurrencies [kaggle.com](kaggle.com)
    2. US Stock index price (API) - [Financial Modeling Prep](https://financialmodelingprep.com/)
    3. Gold price (simple web Scrapping for 2019 and scrapping using Selenium for rest of periods) - [USA Gold](https://www.usagold.com/reference/prices/goldhistory.php)

Available tickers for this program are:

- AMZN: Amazon
- BIDU: Baidu
- AAPL: Apple
- BABA: Ali Baba
- FB: Facebook
- TWTR: Twitter
- GLD: Gold
- BTC: Bitcoin
- BCH: Bitcoin Cash
- ADA: Cardano
- ETH: Ethereum
- LTC: Litecoin
- XRT: Ripple

## How it works

When executing main.py, we have available 5 arguments:

1. "--plot_prices": Plots line chart with evolution of prices NEEDS TICKERS INPUT
2. "--plot_indexed": Plots line chart with indexed evolution of prices NEEDS TICKERS INPUT
3. "--file_pdf": Prints pdf with charts generated previously THIS OPTION DOES NOT REQUIRE FURTHER INPUT
4. "--plot_all": Plots all available tickers' evolution of prices. THIS OPTION DOES NOT REQUIRE FURTHER INPUT
5. "--companies": Selection of tickers to be analized. MAXIMUM 6 TICKERS

## Examples

```

python3 main.py -i -c AMZN AAPL GLD

```
 
This command generates a .png image containing a line chart with indexed price for Amazon, Apple and Gold.

```

python3 main.py -a

```

This command generates a .png image containing a line chart with price in USD for all companies.
