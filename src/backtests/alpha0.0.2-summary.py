# This iteration performs backtest on multiple different assets
# This iteration also displays summary information on the backtests, along with the graph view

from strategies import RSI_MeanReversion
import yfinance as yf
import backtrader as bt

'⬆ ⇑ ⥣ ⤽ ⤋ ⤊'

def pad(val, padding=0, char=' '):
  return (str(val).ljust(padding, char))

def getAsset(ticker, periodStart, periodEnd):
  data = yf.download(ticker.upper(), periodStart, periodEnd)
  return {
    'ticker': ticker.upper(),
    'symbol': ticker.upper(),
    'data': data
  }

assets = [
  getAsset('SPY', '2020-01-01', '2023-01-01'),
  getAsset('AAPL', '2020-01-01', '2023-01-01'),
  getAsset('COST', '2020-01-01', '2023-01-01'),
  getAsset('MSFT', '2020-01-01', '2023-01-01'),
  getAsset('AMZN', '2020-01-01', '2023-01-01'),

  getAsset('TSLA', '2020-01-01', '2023-01-01'),
  getAsset('NFLX', '2020-01-01', '2023-01-01'),
  getAsset('NVDA', '2020-01-01', '2023-01-01'),
]

initialInvestment = 10000.00

def run(ticker, assetData):
  # Create a cerebro entity
  cerebro = bt.Cerebro()
  # Set our desired cash start
  cerebro.broker.setcash(initialInvestment)
  # Create a Data Feed and Add the Data Feed to Cerebro
  data = bt.feeds.PandasData(dataname=assetData)
  cerebro.adddata(data)
  # Set the commission - 0.1% ... divide by 100 to remove the %
  cerebro.broker.setcommission(commission=0.001)
  # Add a strategy
  cerebro.addstrategy(RSI_MeanReversion.RSIMeanReversion)
  cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name = 'sharpe')

  # Print out the starting conditions
  # print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
  # Run over everything
  backtest = cerebro.run()
  # Print out the final result
  # print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

  endValue = cerebro.broker.getvalue()
  dollarDifference = round(endValue - initialInvestment, 3)
  percentageDifference = round((100/initialInvestment)*endValue-100, 3)
  cagr = round((((endValue / initialInvestment)**(1/3)) - 1) * 100, 3)
  sharpeRatio = float(backtest[0].analyzers.sharpe.get_analysis()['sharperatio'])
  direction = '\x1b[32m⤊\x1b[0m' if dollarDifference > 0 else '\x1b[31m⤋\x1b[0m'
  
  print(
    '\x1b[1m' + pad(ticker, 4, ' ') + '\x1b[0m', '|',
    '$' + pad(round(initialInvestment, 3), 10, ' '), '|',
    '$' + pad(round(endValue, 3), 10, ' '), direction,
    pad(
      ' $' + pad(dollarDifference) + ' ('
      + pad(percentageDifference) + '%) ',
    25, ' '), '|',

    pad(str(cagr) + '%', 8, ' '), '|',
    pad(round(sharpeRatio, 3), 10, ' '), '|',
  )

  # Plot the result
  # cerebro.plot()

print('\nrunning...\n')
print( 'Asset', 'Initial', 'Final', 'CAGR', 'Sharpe','\n',)
for asset in assets:
  run(asset['ticker'], asset['data'])
