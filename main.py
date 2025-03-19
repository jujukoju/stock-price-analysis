import numpy as np

stock_prices = np.random.randint(100, 500, size=30)
days = np.arange(1, 31)


def moving_average(prices, window):
    return np.convolve(prices, np.ones(window)/window, mode='valid')


ma_7 = moving_average(stock_prices, 7)

daily_change = np.diff(stock_prices)/stock_prices[:-1] * 100

maximum_price = np.max(stock_prices)
minimum_price = np.min(stock_prices)

print(f"Stock Prices for 30 days: {stock_prices}")
print(f"Daily Change: {daily_change}")
print(f"Max price: {maximum_price}, Min price: {minimum_price}")
