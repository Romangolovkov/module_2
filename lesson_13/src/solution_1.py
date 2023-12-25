from typing import Callable


def decorator_change_price(func: Callable[[tuple|dict], None]) -> Callable[[tuple|dict], None]:
    def wrapper(*args, **kwargs):
        print(f'Цена на {args[0]} изменилась! {args[1]} > {args[2]}')
        func(*args, **kwargs)
    return wrapper


@decorator_change_price
def change_price(*data) -> None:
    pass


change_price('Кресло', 5000, 4500)
change_price('Стол', 8000, 7600)