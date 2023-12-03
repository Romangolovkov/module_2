def final_price(price: float, visits: int) -> float:
    if 10 <= visits < 20:
        print(f'Итоговая цена: {price * 0.9}')
    elif visits >= 20:
        print(f'Итоговая цена: {price * 0.8}')
    elif visits < 0:
        print('Количество посещений не может быть отрицательным')
    else:
        print(f'Итоговая цена: {price}')


price: float = float(input('Введите цену: '))
visits: int = int(input('Введите количество посещений: '))

final_price(price, visits)