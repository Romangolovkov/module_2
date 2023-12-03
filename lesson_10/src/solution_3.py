def best_worker():
    quantity = int(input('Введите количество сотрудников: '))
    workers = [input(f'Введите имя {i + 1}-го сотрудника: ') for i in range(quantity)]
    tasks = [int(input(f'Введите количество задач, которые выполнил {worker}: ')) for worker in workers]
    workers_dict = dict(zip(workers, tasks))
    return [keys for keys, values in workers_dict.items() if values == max(workers_dict.values())]


print()
print(f'Самый ответственный работник: {", ".join(best_worker())}')
print()