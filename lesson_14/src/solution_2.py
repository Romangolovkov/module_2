def func(prices: list[int]) -> list[int]:
    prices: list[int] = [round(price, -2) for price in prices]
    return list(set(filter(lambda price: price % 100 == 0, prices)))


print(func([99, 150, 200, 349, 501]))
