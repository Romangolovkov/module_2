def calculate_discount(numbers: list[int]) -> int:
    return sum(numbers[:-1]) * numbers[-1] / 100


numbers = [50, 150, 250, 20]

print(f'Сумма скидки: {calculate_discount(numbers)}')