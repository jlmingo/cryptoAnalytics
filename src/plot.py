import pandas as pd
import seaborn as sns; sns.set()
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt

df = pd.read_csv("../output/df_final.csv", index_col="Date", parse_dates=True)

#Plots selected tickers in USD (line chart)

def plotTickers(tickers):
    plot_df = df[df.columns.intersection(tickers)]
    plt.figure(figsize=(14,6))
    plt.title("Selected_Quotes_historical_prices_(USD)")
    sns.set_context("notebook", font_scale=1.6, rc={"lines.linewidth": 2.5})
    ax = sns.lineplot(data=plot_df, style="event")
    ax.figure.savefig('{}.png'.format(tickers))
    return ax

#Plots selected tickers indexed-wise (base=100) (line chart)

def plotIndex(tickers):
    plot_df = df[df.columns.intersection(tickers)]
    try:
        plot_df["GLD"].fillna(method="ffill", inplace = True)
    except:
        pass
    plot_df.fillna(100, inplace = True)
    plot_df_indexed = plot_df / plot_df.iloc[-1] * 100
    plt.figure(figsize=(14,6))
    plt.title("Selected_Indexed_Quote_historical_prices (base=100)")
    sns.set_context("notebook", font_scale=1.6, rc={"lines.linewidth": 2.5})
    ax = sns.lineplot(data=plot_df_indexed, style="event")
    ax.figure.savefig('{} Indexed.png'.format(tickers))
    return ax

#Plots all tickers in USD (line chart)

def plotAll():
    ax = df.plot(figsize=(14,6))
    ax.figure.savefig("Available_Quotes_historical_prices(USD)")
    return ax

