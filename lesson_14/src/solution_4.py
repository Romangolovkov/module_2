from typing import Iterator

def fib_prices() -> Iterator:
    u0: int = 0
    u1: int = 1
    while True:
        yield u0
        u0, u1 = u1, u0 + u1


print(fib_prices())