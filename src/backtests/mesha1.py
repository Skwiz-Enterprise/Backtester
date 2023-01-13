import backtrader as bt
import yfinance as yf
from strategies.RSI import RSI

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
