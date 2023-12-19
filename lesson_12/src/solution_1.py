from typing import Callable


def summarize_data(argument: float):
    print(f'Среднее значение: {argument}')


def process_data(numbers: list[int]) -> Callable[[float], None]:
    return summarize_data(sum(numbers) / len(numbers))


def collect_data(list_of_numbers: list[int]) -> Callable[list[int], Callable[[float], None]]:
    return process_data(list_of_numbers)


collect_data([1, 2, 3, 4, 5])
collect_data([10, 15, 5, 20])