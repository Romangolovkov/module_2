from typing import Callable

cashe: list[tuple, dict, int] = []


def decorator_cashe(func: Callable[[tuple, dict], int]) -> Callable[[tuple, dict], None]:
    def wrapper(*args, **kwargs):
        if (args, kwargs) in cashe:
            print(f'Загрузили из кеша: {cashe[cashe.index((args, kwargs)) + 1]}')
        else:
            print(f'Посчитали цену: {func(*args, **kwargs)}')
            cashe.append((args, kwargs))
            cashe.append(func(*args, **kwargs))
            
    return wrapper


@decorator_cashe
def calculate_project_cost(*args, **kwargs) -> int:
    return 3000


calculate_project_cost('Логотип', 'малый бизнес')
calculate_project_cost('Логотип', 'малый бизнес')
calculate_project_cost({1, 2, 3}, a=2)
calculate_project_cost({1, 2, 3}, a=2)