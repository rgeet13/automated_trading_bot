import backtrader as bt
import pandas as pd
import talib
import numpy as np
import matplotlib.pyplot as plt
from data import get_historical_data

# Function to get historical data with date exclusion
def fetch_data(symbol, start_date, end_date, exclude_dates=None):
    crucks = get_historical_data(symbol, "D", start_date, end_date, 0)
    candles = crucks['candles']
    
    # Extract Close values and corresponding dates
    close_values = [candle[4] for candle in candles]
    date_values = [pd.to_datetime(candle[0], unit='s').strftime('%Y-%m-%d') for candle in candles]

    # Exclude specified dates
    if exclude_dates:
        date_values, close_values = zip(*[(date, close) for date, close in zip(date_values, close_values) if date not in exclude_dates])

    # Filter out weekends
    filtered_data = {'date': pd.to_datetime(date_values), 'close': close_values}

    return pd.DataFrame(filtered_data)

class EMAStrategy(bt.Strategy):
    params = (
        ("short_period", 20),
        ("long_period", 50),
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

# Get data with exclusion
symbol = "NSE:SBIN-EQ"
start_date = "2023-01-01"
end_date = "2023-11-10"
exclude_dates = ['2023-01-26', '2023-03-07', '2023-03-15', '2023-03-30', '2023-04-04', '2023-04-07',
                 '2023-04-14', '2023-05-01', '2023-06-28', '2023-08-15', '2023-09-19', '2023-10-02',
                 '2023-10-24', '2023-11-14', '2023-11-27', '2023-12-25'
                 ]  # Add your specific dates here

data = fetch_data(symbol, start_date, end_date, exclude_dates)

# Remove NaN and Inf values
data = data.replace([np.inf, -np.inf], np.nan).dropna()

# Create a backtrader Cerebro engine
cerebro = bt.Cerebro()

# Add the data to Cerebro
data = bt.feeds.PandasData(dataname=data.set_index('date'))

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

# Plot the strategy
cerebro.plot()
