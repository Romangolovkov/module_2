from typing import Iterator

prices_1_str: list[str] = ['10', '30', '40', '50']
prices_2_str: list[str] = ['5', '10', '15', '25', '20']

prices_1_int: list[int] = list(map(int, prices_1_str))
prices_2_int: list[int] = list(map(int, prices_2_str))

index_min_price_1: int = prices_1_int.index(min(prices_1_int))
index_max_price_1: int = prices_1_int.index(max(prices_1_int))
index_min_price_2: int = prices_2_int.index(min(prices_2_int))
index_max_price_2: int = prices_2_int.index(max(prices_2_int))

prices_1_int[index_min_price_1], prices_1_int[index_max_price_1] = max(prices_1_int), min(prices_1_int)
prices_2_int[index_min_price_2], prices_2_int[index_max_price_2] = max(prices_2_int), min(prices_2_int)

print("Новые цены списка №1: ", end = '')
for elem in prices_1_int:
    print(elem, end = ' ')

print()
print("Новые цены списка №2: ", end = '')
for elem in prices_2_int:
    print(elem, end = ' ')