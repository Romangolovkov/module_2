from typing import Callable


def check_order(order: dict[str, int|str]) -> bool:
    return bool(order['items'])


def package_order(order: dict[str, int|str]) -> str:
    if check_order(order):
        return f'Упакован заказ {order["id"]}'
    else:
        return f'Заказ {order["id"]} пуст'


def send_order(check_order: Callable[[dict[str, int|str]], bool], package_order: Callable[[dict[str, int|str]], str], order: dict[str, int|str]) -> str:
    return 'Отправка: ' + package_order(order)


order1 = {'id': 1, 'items': ['book', 'pen']}
order2 = {'id': 2, 'items': []}

print(send_order(check_order, package_order, order1))
print(send_order(check_order, package_order, order2))