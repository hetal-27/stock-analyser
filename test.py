import yfinance as yf
import matplotlib.pyplot as plt

# Download Apple stock data
data = yf.download("AAPL", start="2024-01-01", end="2024-06-01")

# Calculate moving averages
# For each day, take the average of the last 20 days
data['MA20'] = data['Close'].rolling(20).mean()

# For each day, take the average of the last 50 days
data['MA50'] = data['Close'].rolling(50).mean()

# Plot everything
plt.figure(figsize=(12, 5))
plt.plot(data['Close'], color='blue', linewidth=1.5, label='Close Price')
plt.plot(data['MA20'], color='orange', linewidth=1.5, label='20-Day Average')
plt.plot(data['MA50'], color='green', linewidth=1.5, label='50-Day Average')

plt.title("Apple Stock Price with Moving Averages - 2024")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()  # this shows the colour key
plt.grid(True)
plt.savefig("apple_chart.png")
print("Chart saved!")
