import pandas as pd
import yfinance as yf

def fetching_data(ticker: str, start: str, end: str):
        df = yf.download(tickers='SPY', start=start, end=end)
        df.to_csv(f'{ticker}.csv')

def plot(ticker: str):
        df: pd.DataFrame = pd.read_csv(f'{ticker}.csv',index_col=0, parse_dates=True)
        df = df[['Close']]
        df.plot()