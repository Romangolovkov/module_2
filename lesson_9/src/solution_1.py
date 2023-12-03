def calculate_discount() -> int:
    prices_and_discount = [int(number) for number in input('Введите цены и скидку через запятую: ').split(', ')]
    print(f'Сумма скидки: {sum(prices_and_discount[:-1]) * prices_and_discount[-1] / 100}')


calculate_discount()