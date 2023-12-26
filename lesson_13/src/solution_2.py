import time
from typing import Callable


def timer_func(func: Callable[[tuple|dict], None]) -> Callable[[tuple|dict], None]:
    def wrapper(*args, **kwargs):
        start_time: float = time.time()
        func(*args, **kwargs)
        end_time: float = time.time()
        print(f'Execution: {end_time - start_time} seconds')
    return wrapper



@timer_func
def create_design(*args, **kwargs):
    print()
    print(*args)


create_design('Логотип Васильевский рынок')
create_design('Макет сайта Логомашины')