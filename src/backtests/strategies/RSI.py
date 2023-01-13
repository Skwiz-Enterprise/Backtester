import backtrader as bt

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
