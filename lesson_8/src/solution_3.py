products: dict[str, int] = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}

for key in products:
    if products[key] == max(products.values()):
        print(f'Самый дорогой: {key} - {products[key]} руб.')
    elif products[key] == min(products.values()):
        print(f'Самый дешёвый: {key} - {products[key]} руб.')