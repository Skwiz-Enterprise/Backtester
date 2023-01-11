import requests
import pandas as pd
import matplotlib.pyplot as plt

# Get data from Alpha Vantage
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo'
response = requests.get(url)

# Convert data to JSON format
data = response.json()

# Get data series from JSON
time_series = data['Time Series (Daily)']

# Create dataframe with Pandas
data_frame = pd.DataFrame.from_dict(time_series, orient='index')
data_frame.index = pd.to_datetime(data_frame.index)
data_frame.drop(['1. open', '2. high', '3. low',
                '5. volume'], axis=1, inplace=True)

# Calculate Bollinger Bands
rolling_mean = data_frame['4. close'].rolling(window=20).mean()
rolling_std = data_frame['4. close'].rolling(window=20).std()
upper_band = rolling_mean + (rolling_std * 2)
lower_band = rolling_mean - (rolling_std * 2)

# Plot the data
plt.plot(data_frame.index, data_frame['4. close'], label='Close Price')
plt.plot(data_frame.index, rolling_mean, label='20 Day SMA')
plt.fill_between(data_frame.index, lower_band, upper_band,
                 color='green', alpha=0.3, label='Bollinger Bands')
plt.title('MSFT Close Price with 20 Day SMA and Bollinger Bands')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend(loc='upper left')
plt.show()
