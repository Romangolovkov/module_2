products: dict[str, int] = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}
input_product: str = input('Введите товар: ')

if input_product in products:
    print(f'Цена: {products[input_product]} руб.')
else:
    print('Данного товара нет')