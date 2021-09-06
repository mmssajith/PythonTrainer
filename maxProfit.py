def max_profit(prices):
  max_price = max(prices)
  min_price = min(prices)
  profit = max_price-min_price
  return profit

prices = [150,450,569,552]
print(max_profit(prices))