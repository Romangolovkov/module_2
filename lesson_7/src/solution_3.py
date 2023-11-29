numbers: list[int] = [1, 2, 3, 4, 5]
sublist_numbers: list[int] = numbers[numbers[0]: numbers[-1] + 1: numbers[1]]
sublist_numbers: list[str] = [str(number) for number in sublist_numbers]
print(f'Числа подсписка: {", ".join(sublist_numbers)}')