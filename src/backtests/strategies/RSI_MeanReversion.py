import backtrader as bt


class RSIMeanReversion(bt.Strategy):
    def __init__(self):
        self.rsi = bt.indicators.RSI(self.data.close, period=21)
        self.wait = []

    def next(self):
        pos_size = self.broker.getvalue() // self.data.close[0]

        print(self.rsi >= 50)
        if self.position:
            print('We hve the meats')
            self.wait.append(self.data.datetime.date())
            if (len(self.wait) >= 7):
                self.wait = []
                self.sell(size=pos_size)

        if self.position and self.rsi > 80:
            print('sell')
            self.close(size=pos_size)
            self.wait = []

        if not self.position and self.rsi < 20:
            self.buy(size=pos_size)
