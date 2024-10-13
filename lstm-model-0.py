# First, we need to import the necessary libraries and dataframes.
# Then, we split data into training and testing and write our function for training the data
# STRUCTURE:
# 1. Input Layer -> LSTM 1 (Large context size) -> Dropout -> LSTM 2 (Small context size) -> Dropout -> OUT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras import Sequential
from keras import layers
import math
from sklearn.metrics import mean_squared_error
import yfinance as yf

model = Sequential()
model.add(layers.LSTM(units=100, return_sequences=True))
model.add(layers.Dropout(0.2))
model.add(layers.LSTM(units=50))
model.add(layers.Dropout(0.2))
model.compile(optimizer='adam', loss='mean_squared_error')