def best_worker(workers: dict[str, int]) -> str:
    return ', '.join([keys for keys, values in workers.items() if values == max(workers.values())])


workers: dict[str, int] = {'Анна': 5, 'Боб': 7, 'Сюзан': 9}

print()
print(f'Самый ответственный работник: {best_worker(workers)}')
print()