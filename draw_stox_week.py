import yfinance as yf
import pandas as pd

stocks_list = ['AAL', 'AAPL', 'AAPL', 'ABBV', 'ABT', 'ADBE', 'ADI', 'ADI',
               'ADM', 'ADP', 'ADSK', 'ALGN', 'ALL', 'AM', 'AMAT', 'AMAT', 'AMD',
               'AMGN', 'AMZN', 'AMZN', 'ANSS', 'APA', 'APTV', 'ASML', 'ATVI',
               'AUY', 'AVGO', 'BA', 'BA', 'BAC', 'BDX', 'BIDU', 'BIIB', 'BKNG',
               'BMRN', 'BSX', 'C', 'CAMP', 'CCL', 'CCL', 'CDNS', 'CDW',
               'CHE', 'CHK', 'CHKP', 'CHRW', 'CHTR', 'CIM', 'CMCSA', 'CMCSA',
               'CNP', 'COLM', 'COP', 'COP', 'COST', 'COST', 'CPE', 'CPRT', 'CSCO',
               'CSGP', 'CSX', 'CTAS', 'CTSH', 'CVS', 'CVX', 'CVX', 'DAKT',
               'DAL', 'DE', 'DGX', 'DIS', 'DLTR', 'DVN', 'DVN', 'EA', 'EBAY', 'EMN',
               'EPD', 'ESRT', 'EXPE', 'F', 'FAST', 'FCX', 'FDP', 'FDX',
               'FICO', 'FISV', 'FOX', 'FOXA', 'FSLR', 'GCI', 'GE', 'GGB', 'GILD',
               'GLW', 'GM', 'GOOG', 'GOOGL', 'GPS', 'HAL', 'HD', 'HON', 'HPQ',
               'IDXX', 'IFF', 'ILMN', 'INCY', 'INTC', 'INTU', 'ISRG', 'ITW',
               'JD', 'JNJ', 'JPM', 'KEY', 'KGC', 'KHC', 'KLAC', 'KMX', 'KO', 'KR',
               'KSS', 'LBTYA', 'LBTYK', 'LRCX', 'LULU', 'LUV', 'M', 'MAC', 'MAR',
               'MCHP', 'MCHP', 'MCK', 'MDLZ', 'MDT', 'MELI', 'META', 'MFA', 'MGM',
               'MMM', 'MNST', 'MOS', 'MRO', 'MS', 'MSFT', 'MU', 'MUR', 'MYGN', 'NBR',
               'NEM', 'NFLX', 'NKE', 'NLY', 'NSC', 'NTAP', 'NTES', 'NVDA',
               'NVO', 'NXPI', 'ORA', 'ORCL', 'ORLY', 'OXY', 'PAYX', 'PAYX', 'PCAR',
               'PCG', 'PEP', 'PFE', 'PG', 'PLD', 'PRGO', 'PRU', 'PSA', 'PYPL',
               'QCOM', 'RCL', 'REGN', 'RF', 'RIG', 'RMD', 'ROST', 'ROST',
               'RRC', 'SBUX', 'SBUX', 'SCHN', 'SEE', 'SGEN', 'SIEGY', 'SIRI', 'SJM',
               'SLB', 'SLB', 'SM', 'SMG', 'SNPS', 'SPLK', 'SQ', 'STT', 'SU', 'SWKS',
               'SWN', 'SYK', 'SYY', 'T', 'TCOM', 'TGT', 'TKR', 'TMUS', 'TREX', 'TSLA',
               'TTWO', 'TUP', 'TXN', 'UAL', 'ULTA', 'UNH', 'UNP', 'UPS', 'V', 'VLO',
               'VMI', 'VOD', 'VRSK', 'VRSN', 'VRTX', 'VZ', 'WBA', 'WDC',
               'WFC', 'WHR', 'WM', 'WMB', 'WTI', 'X', 'XEL', 'XOM',
               'XRAY', 'ZBRA']


def z_scores(serie):
    return (serie - serie.mean()) / serie.std()


ticker_vals = yf.Tickers(stocks_list)

my_series = ticker_vals.history(period="4y",
                                interval="1wk").Close.pct_change().dropna()

df = my_series.apply(z_scores).tail(1).T

df.reset_index(inplace=True)

df.columns = ['Ticker', 'Weekly Z-Score']

df.sort_values(by='Weekly Z-Score',
               ascending=True,
               inplace=True)


print(df[df['Weekly Z-Score'] < -1])
