import requests
import statistics
from functools import reduce
import matplotlib.pyplot as plt
import numpy as np


def calcChange(curr, prev):
    return (curr - prev) / prev
# %Change (currentClose - prevClose)/prevClose


# mean of close data, sqroot((summation(closedata - mean)^2)/pop size)
packageSize = 31
l = 0
closeData = []
changeData = []
rollingData = []
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=SPY&apikey=99X2EJ7Y48PSML6N'
r = requests.get(url)
data = r.json()["Time Series (Daily)"]
dates = list(data.keys())

for i in dates:
    closeData.append(float(data[i]['4. close']))
closeData.reverse()

for x in range(len(closeData)):
    if x != 0:
        ans = calcChange(float(closeData[x-1]), float(closeData[x]))
        changeData.append(ans)

while l < (len(closeData) - packageSize):
    std = statistics.stdev(closeData[l:l + packageSize])
    rollingData.append(std)
    l = l+1

x = np.array(dates[packageSize:100])
y = np.array(closeData[packageSize:100])
plt.plot(x, y)
plt.xticks(rotation=85)
plt.title("Date and Closing Data")
plt.xlabel("Dates")
plt.ylabel("Closing Data")
plt.show()
