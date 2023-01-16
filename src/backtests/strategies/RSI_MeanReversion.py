import backtrader as bt

class RSIMeanReversion(bt.Strategy):
    def __init__(self):
        self.rsi = bt.indicators.RSI(self.data.close, lookback=21, period=21, safediv=True)
        self.wait = []

    def next(self):
        pos_size = int(self.broker.getvalue() / self.data.close[0])
        # print(self.data.datetime.date(), self.broker.getvalue(), str(self.data.close[0]), pos_size)

        if self.position:
            # print('holding')
            self.wait.append(self.data.datetime.date())
            if (len(self.wait) >= 7):
                # print('sell', pos_size)
                self.wait = []
                self.close(size=pos_size)

        if self.position and self.rsi >= 80:
            # print('sell')
            self.wait = []
            self.close(size=pos_size)

        if (not self.position) and self.rsi <= 20:
            # print('buy', pos_size)
            self.buy(size=pos_size)
