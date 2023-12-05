def find_max_price(prices: list[int], i: int = 0, max_number: int = 0) -> int:
    if i <= len(prices) - 1:
        if prices[i] > max_number:
            max_number = prices[i]
        max_number = find_max_price(prices, i + 1, max_number)
    return max_number
    

print(find_max_price([2, 5, 4, 10, 7]))