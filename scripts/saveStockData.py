import yfinance as yf

def getAsset(ticker, periodStart, periodEnd):
  data = yf.download(ticker.upper(), periodStart, periodEnd)
  return {
    'ticker': ticker.upper(),
    'symbol': ticker.upper(),
    'data': data
  }

assets = [
  getAsset('TSLA', '2020-01-01', '2023-01-01'),
  # getAsset('NFLX', '2020-01-01', '2023-01-01'),
  # getAsset('NVDA', '2020-01-01', '2023-01-01'),

  getAsset('SPY', '2020-01-01', '2023-01-01'),
  getAsset('AAPL', '2020-01-01', '2023-01-01'),
  getAsset('COST', '2020-01-01', '2023-01-01'),
  getAsset('MSFT', '2020-01-01', '2023-01-01'),
  getAsset('AMZN', '2020-01-01', '2023-01-01'),
]

stock = []
keys = ['Open','High','Low','Close','Adj Close','Volume']

for index in range(len(assets[0]['data'].Close)):
  dic = {}
  for key in keys:
    dic[key] = assets[0]['data'][key][index]
  stock.append(dic)

h = 'Open, High, Low, Close, Adj Close, Volume\n'
for record in stock:
  for key in record:
    h = h + str(round(record[key], 2)) + ', '
  h = h + '\n'

f = open("./fixtures/test.txt", "w")
f.write(h)
f.close()
