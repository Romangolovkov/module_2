def binary_find_element(list_elements: list[int], element: int) -> bool:
    start: int = 0
    end: int = len(list_elements)
    res: bool = False
    while start != end and abs(end - start) != 1:
            if list_elements[(start + end) // 2] == element or list_elements[start] == element:
                res = True
                break
            elif list_elements[(start + end) // 2] < element:
                start = (start + end) // 2
            else:
                end = (start + end) // 2
    return res


print(binary_find_element([], 10))
print(binary_find_element([10, 20, 30, 40, 50, 60, 70, 80], 85))
print(binary_find_element([10, 20, 30, 40, 50, 60, 70, 80], 0))
print(binary_find_element([10, 20, 30, 40, 50, 60, 70], 10))
print(binary_find_element([10, 20, 30, 40, 50, 60, 70, 80], 20))
print(binary_find_element([10, 20, 30], 30))