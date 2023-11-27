prices: list[int] = [10, 20, 30, 40, 50]
new_prices: list[str] = []

for i in range(len(prices)):
    new_prices.append(str(prices.pop(prices.index(max(prices)))))

print(f"Отсортированные цены: {', '.join(new_prices)}")