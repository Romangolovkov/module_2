def calculate_discount(prices: list[int], i: int = 1) -> list[int]:
    if i <= len(prices) - 1:
        prices[- i] = prices[- i] - prices[- i - 1] * 0.1
        calculate_discount(prices, i + 1)
    return [int(price) for price in prices]


print()
print(', '.join([str(price) for price in calculate_discount([1000, 2000, 3000])]))
print(', '.join([str(price) for price in calculate_discount([5000, 10000, 15000])]))
print(', '.join([str(price) for price in calculate_discount([100, 200, 300, 400])]))
print(', '.join([str(price) for price in calculate_discount([50, 100])]))
print()