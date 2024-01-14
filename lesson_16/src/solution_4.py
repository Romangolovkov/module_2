def func(shelves: str, sales: str) -> list[list[int]]:
    return [[int(sales) for sales in shelve.split(',')] for shelve in sales.split(';')]
    

print(func('2', '5,3;7,2'))
print(func('3', '2,6,4;3,5,7;1,2,3'))