import yfinance as yf
import pandas as pd

stocks_list = ['ACN', 'ADI', 'ALLE', 'AVY', 'CFG', 'COP', 'CTAS', 'DPZ', 'FANG', 'FCX', 'FITB', 
               'HBAN', 'HD', 'HII', 'HPQ', 'JKHY', 'KEY', 'LOW', 'LUV', 'MAS', 'MCO', 'MKTX', 
               'MSCI', 'MSI', 'NDAQ', 'NKE', 'NSC', 'NXPI', 'ORCL', 'OTIS', 'PH', 'PNC', 'RF', 
               'RHI', 'SNA', 'SPGI', 'STT', 'SWKS', 'SYK', 'TJX', 'TT', 'UNH', 'UNP', 'VMC', 'VTRS', 'ZTS']



def z_scores(serie):
    return (serie - serie.mean()) / serie.std()


ticker_vals = yf.Tickers(stocks_list)

my_series = ticker_vals.history(period="4y",
                                interval="1wk").Close.pct_change()

df = my_series.apply(z_scores).tail(1).T

df.reset_index(inplace=True)

df.columns = ['Ticker', 'Weekly Z-Score']

df.sort_values(by='Weekly Z-Score',
               ascending=True,
               inplace=True)


print(df.head(5))
