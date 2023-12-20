from typing import Callable

data_sets: list[tuple[list[int], Callable[[int], bool]]] = [
    ([10, 23, 35, 47], lambda x: x % 2 == 1),
    ([5, 7, 8, 10], lambda x: x > 7),
    ([1, 2, 3, 5, 6], lambda x: x < 5),
    ([10, 20, 30, 40, 50], lambda x: x % 5 == 0 and x % 8 == 0)
]


def filter_data(data: list[int], filter_func: Callable[[int], bool]) -> list[int]:
    filtred_data: list[int] = []
    for elem in data:
        if filter_func(elem):
            filtred_data.append(elem)
    return filtred_data


print()
for data, filter_func in data_sets:
    filtered_data: list[int] = filter_data(data, filter_func)
    print(f'Отфильтрованные данные: {filtered_data}')
print()