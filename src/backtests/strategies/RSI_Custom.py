import backtrader as bt
import datetime


class RSICustom(bt.Strategy):
    def __init__(self):
        self.rsi = bt.indicators.RSI(self.data.close, period=30)
        self.add_timer(when=bt.timer.SESSION_START,
                       timer=True,
                       cheat=False,
                       offset=datetime.timedelta(),
                       repeat=datetime.timedelta(),
                       weekdays=[])

    def next(self):
        pos_size = self.broker.getvalue() // self.data.close[0]

        if self.rsi < 30 and self.rsi < 20:  # BUY condition
            if self.position and (self.rsi < 30 and self.rsi < 20):
                self.close()
            self.order = self.buy(size=pos_size)

        if self.data.datetime.date().weekday() == 2:  # SELL condition
            if self.position:
                self.close()
            self.order = self.sell(size=pos_size)
