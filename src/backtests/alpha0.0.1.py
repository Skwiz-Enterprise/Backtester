from strategies import RSI_MeanReversion
import yfinance as yf
import backtrader as bt


# Create a cerebro entity
cerebro = bt.Cerebro()

# Add a strategy
cerebro.addstrategy(RSI_MeanReversion.RSIMeanReversion)

# Create a Data Feed
c = yf.download('SPY', '2020-01-01', '2023-01-01')
data = bt.feeds.PandasData(dataname=c)

# Add the Data Feed to Cerebro
cerebro.adddata(data)

# Set our desired cash start
cerebro.broker.setcash(10000000.0)

# Set the commission - 0.1% ... divide by 100 to remove the %
cerebro.broker.setcommission(commission=0.001)

# Print out the starting conditions
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

# Run over everything
cerebro.run()

# Print out the final result
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

# Plot the result
# cerebro.plot()
