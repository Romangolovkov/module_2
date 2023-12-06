def calculate_discount(prices: list[float], i: int = 1) -> list[float]:
    if i <= len(prices) - 1:
        prices[- i] = prices[- i] - prices[- i - 1] * 0.1
        calculate_discount(prices, i + 1)
    return prices


print(', '.join([str(price) for price in calculate_discount([100, 200, 300, 400])]))