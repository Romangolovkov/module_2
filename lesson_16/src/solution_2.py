def new_shelves_func(shelves: str, products: str) -> list[list[int]]:
    shelves: list[int] = [int(i) for i in shelves.split(',')]
    products: list[int] = [int(i) for i in products.split(',')]
    return list(zip(shelves, products))


print(new_shelves_func('4,5,6', '2,3,5'))
print(new_shelves_func('3,4', '1,4'))