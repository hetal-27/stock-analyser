import yfinance as yf
import matplotlib.pyplot as plt

# List of stocks to compare
tickers = ["AAPL", "TSLA", "MSFT", "GOOGL", "AMZN"]

# Date range
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

# Download all stocks at once
data = yf.download(tickers, start=start_date, end=end_date)['Close']

# Calculate daily returns
daily_returns = data.pct_change()

# Calculate cumulative returns
cumulative_returns = (1 + daily_returns).cumprod()

# Plot all stocks on one chart
plt.figure(figsize=(12, 6))

for ticker in tickers:
    plt.plot(cumulative_returns[ticker], linewidth=1.5, label=ticker)

plt.title("Stock Comparison — Cumulative Returns")
plt.xlabel("Date")
plt.ylabel("Growth of $1 invested")
plt.legend()
plt.grid(True)
plt.savefig("comparison_chart.png")
print("Chart saved!")
