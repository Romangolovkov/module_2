from typing import Callable


def check_order(order):
    return bool(order['items'])


def package_order(order):
    if check_order(order):
        return f'Упакован заказ {order["id"]}'
    else:
        return f'Заказ {order["id"]} пуст'


def send_order(check_order, package_order, order):
    return 'Отправка: ' + package_order(order)


order1 = {'id': 1, 'items': ['book', 'pen']}
order2 = {'id': 2, 'items': []}

print(send_order(check_order, package_order, order1))
print(send_order(check_order, package_order, order2))