import pandas as pd
import matplotlib.pyplot as plt

def plot(ticker: str):
    df = pd.read_csv(f"{ticker}.csv", parse_dates=["Date"], index_col='Date')
    df = df.tail(30)
    df = df[['Close', 'Open']]

    df.plot(xlabel='Date')


plot('SPY')
plt.show()