import pandas as pd
import seaborn as sns; sns.set()
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt

df = pd.read_csv("../output/df_final.csv", index_col="Date", parse_dates=True)

def plotTickers(tickers):
    plot_df = df[df.columns.intersection(tickers)]
    plt.figure(figsize=(14,6))
    plt.title("Selected Quotes historical prices (USD)")
    sns.set_context("notebook", font_scale=1.6, rc={"lines.linewidth": 2.5})
    ax = sns.lineplot(data=plot_df, style="event")
    ax.figure.savefig('{}.png'.format(tickers))
    return ax