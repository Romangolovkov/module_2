from typing import Callable


def arguments_checking(func: Callable[[str, int], None]) -> Callable[[tuple], None]:
    def wrapper(*args):
        if len(args) == 2:
            if isinstance(args[0], str):
                if isinstance(args[1], int):
                    return func(*args)
                else:
                    print('Ошибка: Второй аргумент не число!')
            else:
                print('Ошибка: Первый аргумент не строка!')
        else:
            print('Ошибка: Неверное количество аргументов!')
    return wrapper





print()
@arguments_checking
def estimate_time(name_project: str, number_tasks: int):
    print('Estimated time calculated successfully.')


estimate_time('Вебсайт', 'пять')
estimate_time('Визитка', 10)
print()
estimate_time(10, 10)
estimate_time('Визитка', 10, 10)
print()