def gen(report):
    print('Генератор стрниц отчета')
    for page in report:
        yield page 


print()
print(gen(['Стр 1', 'Стр 2', 'Стр 3']))

for page in gen(['Стр 1', 'Стр 2', 'Стр 3']):
    print(page)

print()