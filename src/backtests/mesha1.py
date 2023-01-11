import backtrader as bt
import yfinance as yf
from datetime import datetime
from src.strategies import RSI_Custom
from strategies import RSI_strat


startcash = 1000000
cerebro = bt.Cerebro()
cerebro.addstrategy(RSI_strat)

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
