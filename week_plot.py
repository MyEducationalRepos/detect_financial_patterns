
import sys
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def z_scores(serie):
    return (serie - serie.mean()) / serie.std()


def weekly_var(ticker):

    ticker_vals = yf.Ticker(ticker)

    weekly_series = ticker_vals.history(period="4y",
                                        interval="1wk").Close

    # We just care about the % change
    z_scores_series = z_scores(weekly_series.pct_change().dropna())

    # Generate first plot with Daily Close
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 6))

    sns.lineplot(weekly_series, ax=ax1)
    ax1.title.set_text('Cierre semanal')
    ax1.tick_params(axis='x', rotation=90)

    # Generate second plot with Z-Score

    sns.lineplot(z_scores_series, ax=ax2)

    ax2.axhline(y=z_scores_series.mean() + 2 * z_scores_series.std(),
                color='orange',
                linestyle='--')
    ax2.axhline(y=z_scores_series.mean() - 2 * z_scores_series.std(),
                color='orange',
                linestyle='--')

    ax2.title.set_text('Z-Score de la variación semanal')

    ax2.tick_params(axis='x', rotation=90)

    fig.suptitle('El mono de ' + ticker)

    plt.show()


def main():
    if len(sys.argv) >= 2:  # Checking number of parameters
        arg = sys.argv[1]
        print("Ticker:", arg)
        weekly_var(arg)
    else:
        print("ERROR: no argument provided.")


if __name__ == '__main__':
    main()
