from typing import Callable


def authentication(func: Callable[[tuple], None]) -> Callable[[tuple], None]:
    def wrapper(*args):
        if args[0] == 'Роман' and args[1] == 'correctpassword':
            print('Доступ получен. Данные: ...')
            func(*args)
        else:
            print('В доступе отказано!')
    return wrapper


@authentication
def access_client_data(*args):
    pass

print()
access_client_data('Роман', 'correctpassword')
print()
access_client_data('Виктор', 'wrongpassword')
print()