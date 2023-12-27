cashe = {}

def decorator_cashe(func):
    def wrapper(*args):
        if args in cashe:
            print(f'Загрузили из кеша: {cashe[args]}')
        else:
            print(f'Посчитали цену: {func(*args)}')
            cashe[args] = func(*args)
    return wrapper
        






@decorator_cashe
def calculate_project_cost(*args, **kwargs):
    return 3000


calculate_project_cost('Логотип', 'малый бизнес')
calculate_project_cost('Логотип', 'малый бизнес')