from typing import Callable

cashe: dict[tuple: int] = {}


def decorator_cashe(func: Callable[[tuple], int]) -> Callable[[tuple], None]:
    def wrapper(*args):
        if args in cashe:
            print(f'Загрузили из кеша: {cashe[args]}')
        else:
            print(f'Посчитали цену: {func(*args)}')
            cashe[args] = func(*args)
    return wrapper


@decorator_cashe
def calculate_project_cost(*args) -> int:
    return 3000


calculate_project_cost('Логотип', 'малый бизнес')
calculate_project_cost('Логотип', 'малый бизнес')
calculate_project_cost({1, 2, 3})