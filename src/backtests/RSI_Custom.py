import backtrader as bt


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
