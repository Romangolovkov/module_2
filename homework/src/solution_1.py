def find_element(list_elements: list[int|str], element: int|str):
    res: bool = False
    i: int = 0
    while i < len(list_elements):
        if list_elements[i] == element:
            res = True
            break
        else:
            i += 1
    return res    


print(find_element([1, 2, 3, 4, 5], 5))
print(find_element([1, 2, 3, 4, 5], 1))
print(find_element([1, 2, 3, 4, 5], 0))