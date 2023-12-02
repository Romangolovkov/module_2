workers: list[str] = ['Снабжение, Менеджер, Иванов', 'Дизайн, Дизайнер, Смирнов', 'Снабжение, Менеджер, Петров', 'Дизайн, Иллюстратор, Сидоров', 'Маркетинг, Аналитик, Сергеев', 'Дизайн, Дизайнер, Васильев']
workers: list[list[str]]= [worker.split(', ') for worker in workers]

supply: dict[str, str] = {}
design: dict[str, str] = {}

for worker in workers:
    if worker[0] == 'Снабжение':
        supply[worker[1]] = worker[2]
    elif worker[0] == 'Дизайн':
        design[worker[1]] = worker[2]

print(f'Снабжение: {supply}')
print(f'Дизайн: {design}')