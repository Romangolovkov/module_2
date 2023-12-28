from typing import Callable


def check_order(order: dict[str, int|str]) -> bool:
    return bool(order['items'])


def package_order(order: dict[str, int|str]) -> str|None:
        return f'Упакован заказ {order["id"]}'


def send_order(check_order: Callable[[dict[str, int|str]], bool], package_order: Callable[[dict[str, int|str]], str], order: dict[str, int|str]) -> str:
    if check_order(order):
        return 'Отправка: ' + package_order(order)
    return f'Отправка: Заказ {order["id"]} пуст'


order1 = {'id': 1, 'items': ['book', 'pen']}
order2 = {'id': 2, 'items': []}

print(send_order(check_order, package_order, order1))
print(send_order(check_order, package_order, order2))