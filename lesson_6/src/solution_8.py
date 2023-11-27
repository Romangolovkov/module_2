from typing import Iterator

products: list[str] = ['Чай', 'Мёд', 'Сахар']

replace_positions: list[str] = input('Введите 2 номера позиций для перестановки через запятую').split(',')
replace_positions: list[int] = list(map(int, replace_positions))

products[replace_positions[0] - 1], products[replace_positions[1] - 1] = products[replace_positions[1] - 1], products[replace_positions[0] - 1]

print(f'На полке: {", ".join(products)}')