import talib
import pandas as pd
import matplotlib.pyplot as plt
from data import get_historical_data

crucks = get_historical_data("NSE:SBIN-EQ", "D", "2023-01-01", "2023-11-10", 0)

# Extract Close values and corresponding dates
candles = crucks['candles']
close_values = [candle[4] for candle in candles]
date_values = [pd.to_datetime(candle[0], unit='s').strftime('%Y-%m-%d') for candle in candles]

# Dates to be excluded
exclude_dates = ['2023-01-26', '2023-03-07', '2023-03-15', '2023-03-30', '2023-04-04', '2023-04-07',
                 '2023-04-14', '2023-05-01', '2023-06-28', '2023-08-15', '2023-09-19', '2023-10-02',
                 '2023-10-24', '2023-1-14', '2023-1-27', '2023-12-25'
                 ]  # Add your specific dates here

# Filter out weekends and specified dates
filtered_data = [(date, close) for date, close in zip(date_values, close_values) if pd.to_datetime(date).weekday() < 5 and date not in exclude_dates]

# Create DataFrame with 'Date' and 'Close' columns
df = pd.DataFrame(filtered_data, columns=['Date', 'Close'])
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Calculate EMA
df['EMA_20'] = talib.EMA(df['Close'], timeperiod=20)
df['EMA_50'] = talib.EMA(df['Close'], timeperiod=50)

# Generate signals
df['Signal'] = 0  # 0 indicates no signal
df['Signal'][df['EMA_20'] > df['EMA_50']] = 1  # Buy signal
df['Signal'][df['EMA_20'] < df['EMA_50']] = -1  # Sell signal

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['Close'], label='Close Price')
plt.plot(df['EMA_20'], label='20 EMA')
plt.plot(df['EMA_50'], label='50 EMA')

# Plot Buy signals
plt.plot(df[df['Signal'] == 1].index, df['EMA_20'][df['Signal'] == 1], '^', markersize=10, color='g', label='Buy Signal')

# Plot Sell signals
plt.plot(df[df['Signal'] == -1].index, df['EMA_20'][df['Signal'] == -1], 'v', markersize=10, color='r', label='Sell Signal')

plt.title('EMA Crossover Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
