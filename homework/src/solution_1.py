def find_element(list_elements: list[int|str], element: int|str) -> bool:
    return bool([i for i in list_elements if i == element])


print(find_element([1, 2, 3, 4, 5], 5))
print(find_element([1, 2, 3, 4, 5], 1))
print(find_element([1, 2, 3, 4, 5], 0))