def final_price(price: int, visits: int) -> float:
    if 10 <= visits < 20:
        print(f'Итоговая цена: {int(price * 0.9)}')
    elif visits >= 20:
        print(f'Итоговая цена: {int(price * 0.8)}')
    elif visits < 0:
        print('Количество посещений не может быть отрицательным')
    else:
        print(f'Итоговая цена: {int(price)}')


print()
final_price(100, 5)
final_price(200, 10)
final_price(150, 20)
print()