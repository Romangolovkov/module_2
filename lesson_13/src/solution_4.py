from typing import Callable


def arguments_checking(func: Callable[[str, int], None]) -> Callable[[tuple], None]:
    def wrapper(*args):
        if len(args) == 2 and type(args[0]) == str and type (args[1]) == int:
            return func(*args)
        elif len(args) == 2 and type(args[0]) == str and type (args[1]) != int:
            print('Ошибка: Второй аргумент не число')
        elif len(args) == 2 and type(args[0]) != str and type (args[1]) == int:
            print('Ошибка: Первый аргумент не строка')
        elif len(args) == 2 and type(args[0]) != str and type (args[1]) != int:
            print('Ошибка: Первый аргумент не строка, а второй аргумент не число')
        elif len(args) != 2:
            print('Ошибка: Неверное количество аргументов')
    return wrapper


print()
@arguments_checking
def estimate_time(name_project: str, number_tasks: int):
    print('Estimated time calculated successfully.')


estimate_time('Вебсайт', 'пять')
estimate_time('Визитка', 10)
print()
estimate_time(10, 10)
estimate_time(10, 'Визитка')
estimate_time('Визитка')
print()