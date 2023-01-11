import backtrader as bt
import yfinance as yf
from datetime import datetime

class RSI(bt.Strategy):
  def __init__(self):
    self.rsi = bt.indicators.RSI(self.data.close, period=21)
    self.fast_sma = bt.indicators.SMA(self.data.close, period=50)
    self.slow_sma = bt.indicators.SMA(self.data.close, period=100)
    self.crossup = bt.ind.CrossUp(self.fast_sma, self.slow_sma)

  def next(self):
    if not self.position:
      if self.rsi > 30 and self.fast_sma > self.slow_sma:
        self.buy(size=100)
    else:
      if self.rsi < 70:
        self.sell(size=100)

class RSICustom(bt.Strategy):
  def __init__(self):
    self.rsi = bt.indicators.RSI(self.data.close, period=21)

  def next(self):
    if not self.position:
      if self.rsi > 30:
        self.buy(size=100)
    else:
      if self.rsi < 70:
        self.sell(size=100)
 
startcash = 1000000
cerebro = bt.Cerebro()
cerebro.addstrategy(RSI)

data = bt.feeds.PandasData(dataname=yf.download('SPY', '2022-01-12', '2023-01-01'))
print(data)

cerebro.adddata(data)
cerebro.broker.setcommission(commission=0.002)
cerebro.broker.setcash(startcash)
cerebro.run()

portvalue = cerebro.broker.getvalue()
pnl = portvalue - startcash

print('Final Portfolio Value: ${}'.format(portvalue))
print('P/L: ${}'.format(pnl))
