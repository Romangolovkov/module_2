def find_max_price(prices: list[int], i: int = 0, max_number: int = 0) -> int:
    if i <= len(prices) - 1:
        if i == 0:
            max_number = prices[0]
        if prices[i] > max_number:
            max_number = prices[i]
        max_number = find_max_price(prices, i + 1, max_number)
    return max_number
    

print()
print(find_max_price([15, 7, 9]))
print(find_max_price([1, 10, 20, 5]))
print(find_max_price([25, 25, 25]))
print(find_max_price([10, 8, 12]))
print(find_max_price([-2, -7, -9, -1]))
print()