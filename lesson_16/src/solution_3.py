def discounts(shelves: list[list[int]]) -> list[list[int]]:
    return [[shelves[i][1] * (i + 1)] * shelves[i][1] for i in range(len(shelves))]


print(discounts([[4, 2], [5, 3], [6, 5]]))
print(discounts([[3, 1], [4, 4]]))