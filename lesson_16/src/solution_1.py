def new_shelves_func(quantity_shelves: str, lengths_shelves: str) -> list[list[int]]:
    lengths_shelves: list[int] = [int(i) for i in lengths_shelves.split(',')]
    return [[lengths_shelves[i], 0] for i in range(int(quantity_shelves))]


print(new_shelves_func('3', '4,5,6'))
print(new_shelves_func('2', '3,4'))
