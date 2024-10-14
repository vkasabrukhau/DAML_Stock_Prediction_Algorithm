import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd


# Below is range of time we want to consider. Change this to whatever.
start_date = "2023-10-02"
end_date = "2024-10-02"
# Insert the three stocks (or more) that we want to analyze below
stock_data = yf.download("AAPL GOOGL TSLA", start_date, end_date)
# The "Close" below, focuses on the last price which a stock traded during a day.
# We can change that to other things  depending on what we want to predict
prices = stock_data["Close"]

prices.plot()
plt.xlabel = ("time")
plt.ylabel = ("stock price/close")
plt.show()