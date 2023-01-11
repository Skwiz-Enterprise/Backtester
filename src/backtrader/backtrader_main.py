import datetime
import os.path
import sys
import backtrader as bt
import backtrader_test_strategy as strat
import yfinance as yf

# Create a cerebro entity
cerebro = bt.Cerebro()

# Add a strategy
cerebro.addstrategy(strat.SMAStrategy)

# Datas are in a subfolder of the samples. Need to find where the script is
# because it could have been called from anywhere
modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
datapath = os.path.join(modpath, '../SPY.csv')

# Create a Data Feed
data = bt.feeds.YahooFinanceCSVData(
    dataname=yf.download('SPY', '2022-01-12', '2023-01-01'),
    # Do not pass values before this date
    fromdate=datetime.datetime(2022, 1, 1),
    # Do not pass values before this date
    todate=datetime.datetime(2022, 12, 31),
    # Do not pass values after this date
    reverse=False)

# Add the Data Feed to Cerebro
cerebro.adddata(data)

# Set our desired cash start
cerebro.broker.setcash(100000.0)

# Set the commission - 0.1% ... divide by 100 to remove the %
cerebro.broker.setcommission(commission=0.001)

# Print out the starting conditions
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

# Run over everything
cerebro.run()

# Print out the final result
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

# Plot the result
cerebro.plot()
