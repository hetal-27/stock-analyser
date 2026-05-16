
import yfinance as yf
import matplotlib.pyplot as plt

# Settings - change these to whatever you want!
ticker = input("Enter ticker symbol (e.g. AAPL, TSLA, MSFT): ").upper()
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

# Download stock data
data = yf.download(ticker, start=start_date, end=end_date)

# Calculate moving averages
data['MA20'] = data['Close'].rolling(20).mean()
data['MA50'] = data['Close'].rolling(50).mean()

# Plot everything
plt.figure(figsize=(12, 5))
plt.plot(data['Close'], color='blue', linewidth=1.5, label='Close Price')
plt.plot(data['MA20'], color='orange', linewidth=1.5, label='20-Day Average')
plt.plot(data['MA50'], color='green', linewidth=1.5, label='50-Day Average')

plt.title(f"{ticker} Stock Price with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.savefig("apple_chart.png")
print("Chart saved!")

