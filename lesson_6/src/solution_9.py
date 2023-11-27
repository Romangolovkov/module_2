from random import randrange

amount_prices: int = int(input('Введите количество цен: '))
prices: list[int] = [randrange(10, 100, 10) for i in range(amount_prices)]
print(prices)

new_prices: list[str] = []

for i in range(len(prices)):
    new_prices.append(str(prices.pop(prices.index(max(prices)))))

print(f"Отсортированные цены: {', '.join(new_prices)}")