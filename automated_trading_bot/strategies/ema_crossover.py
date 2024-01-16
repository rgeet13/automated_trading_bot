import pandas as pd
import backtrader as bt
import sys
print(sys.path)
from brokers.fyers.data import get_historical_data

data = get_historical_data("NSE:SBIN-EQ", "D", "2022-01-01", "2024-01-10", 0)

# Extract Close values while maintaining the original order
close_values = [candle[4] for candle in data['candles']]
data = {
    'Date': pd.date_range(start='2022-01-01', end='2024-01-10'),
    'Close': close_values
}

df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

class EMAStrategy(bt.Strategy):
    params = (
        ("short_period", 20),
        ("long_period", 50)
    )

    def __init__(self):
        self.ema_short = bt.indicators.ExponentialMovingAverage(self.data.close, period=self.params.short_period)
        self.ema_long = bt.indicators.ExponentialMovingAverage(self.data.close, period=self.params.long_period)
        self.crossover = bt.indicators.CrossOver(self.ema_short, self.ema_long)

    def next(self):
        if self.crossover > 0:
            self.buy()
        elif self.crossover < 0:
            self.sell()

# Create a backtrader Cerebro engine
cerebro = bt.Cerebro()

# Add the data to Cerebro
data = bt.feeds.PandasData(dataname=df)

cerebro.adddata(data)
cerebro.addstrategy(EMAStrategy)

# Set the initial cash amount for the backtest
cerebro.broker.set_cash(10000)

# Print the starting cash amount
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

# Run the backtest
cerebro.run()

# Print the final cash amount
print('Ending Portfolio Value: %.2f' % cerebro.broker.getvalue())
