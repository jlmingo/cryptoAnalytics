#!/usr/bin/python3
import argparse
from plot import plotTickers, plotIndex, plotAll
from pdf import createPDF

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

def parse():
    parser = argparse.ArgumentParser()
    grupo = parser.add_mutually_exclusive_group()
    grupo.add_argument("-p", "--plot_prices", help="Plots line chart with evolution of prices.", action='store_true')
    grupo.add_argument("-i", "--plot_indexed", help="Plots line chart with indexed evolution of prices.", action='store_true')
    grupo.add_argument("-f", "--file_pdf", help="Prints pdf with charts generated.", action='store_true')
    parser.add_argument("-a", "--plot_all", help="Plots all available tickers' evolution of prices.", action='store_true')
    parser.add_argument("-c", "--companies", help="Selection of tickers to be analized. Available tickers: {}".format(d_help), nargs="+", action="store")
    return parser.parse_args()

def main():
    args = parse()
    print(args)
    if args.plot_prices:
        plotTickers(args.companies)
    elif args.plot_indexed:
        plotIndex(args.companies)
    elif args.plot_all:
        plotAll()
    elif args.file_pdf:
        createPDF()
    if (args.plot_prices or args.plot_indexed or args.plot_all):
        print("The chart has been plotted.")

if __name__=='__main__':
	main()  