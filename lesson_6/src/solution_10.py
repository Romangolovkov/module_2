from typing import Iterator

prices: list[str] = "10, 20, 30, 40, 50".split(',')
prices: list[int] = list(map(int, prices))

print(f"Средняя цена товаров: {sum(prices)/len(prices)}")