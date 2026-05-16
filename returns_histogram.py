import yfinance as yf
import matplotlib.pyplot as plt

# Settings
ticker = input("Enter ticker symbol (e.g. AAPL, TSLA, MSFT): ").upper()
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

# Download stock data
data = yf.download(ticker, start=start_date, end=end_date)

# Calculate daily returns
data['Daily_Return'] = data['Close'].pct_change()

# Print key stats
print(f"\n{ticker} Return Statistics:")
print(f"Average daily return: {data['Daily_Return'].mean():.4f}")
print(f"Volatility (std dev): {data['Daily_Return'].std():.4f}")
print(f"Best day:  {data['Daily_Return'].max():.4f}")
print(f"Worst day: {data['Daily_Return'].min():.4f}")

# Plot histogram
plt.figure(figsize=(12, 5))
data['Daily_Return'].dropna().hist(bins=50, 
                                   color='steelblue', 
                                   edgecolor='black')
plt.axvline(x=0, color='red', linestyle='--', linewidth=1.5)
plt.title(f"{ticker} — Distribution of Daily Returns")
plt.xlabel("Daily Return")
plt.ylabel("Number of Days")
plt.grid(False)
plt.savefig("histogram.png")
print("Chart saved!")

