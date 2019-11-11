#!/usr/bin/python3
import argparse
from plot import plotTickers

d_help = {
    "AMZN": "Amazon",
    "BIDU": "Baidu",
    "AAPL": "Apple",
    "BABA": "Ali Baba",
    "FB": "Facebook",
    "TWTR": "Twitter",
    "GLD": "Gold",
    "BTC": "Bitcoin",
    "BCH": "Bitcoin Cash",
    "ADA": "Cardano",
    "ETH": "Ethereum",
    "LTC": "Litecoin",
    "XRT": "Ripple"
}

# parser = argparse.ArgumentParser()
# parser.add_argument("-c", "--company", help="Selection of tickers to be analized. Available tickers:{}".format(d_help), nargs="+")
# args = parser.parse_args()
# plotTickers(args)


# parser = argparse.ArgumentParser()
# parser.add_argument('-l', '--list', help="Selection of tickers to be analized. Available tickers:{}".format(d_help), type=str)
# args = parser.parse_args()
# my_list = [item for item in args.list.split(',')]
# plotTickers(my_list)

def parse():
    parser = argparse.ArgumentParser()
    grupo = parser.add_mutually_exclusive_group()
    grupo.add_argument("-p", "--plot_prices", help="Plots line chart with evolution of prices.", action='store_true')
    parser.add_argument('companies', help="Selection of tickers to be analized.\n Available tickers:{}".format(d_help), nargs="+")
    return parser.parse_args()

def main():
    args = parse()
    print(args)
    plotTickers(args.companies)

if __name__=='__main__':
	main()