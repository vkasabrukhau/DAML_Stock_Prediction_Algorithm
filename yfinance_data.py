import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

#put the names of each company stock here
#Also input date range
stock_names = yf.Tickers('AAPL GOOGL TSLA')
start_date = "2023-10-02"
end_date = "2024-10-02"

stock_data = yf.download("AAPL GOOGL TSLA", period="1mo")
stock_data.plot(kind='line')
plt.xlabel = ("time")
plt.ylabel = ("stock price")
plt.show()