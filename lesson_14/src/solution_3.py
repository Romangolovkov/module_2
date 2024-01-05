from typing import Iterator

def pages_report(report: list[str]) -> Iterator:
    for page in report:
        yield page 


print()
print(pages_report(['Стр 1', 'Стр 2', 'Стр 3']))

for page in pages_report(['Стр 1', 'Стр 2', 'Стр 3']):
    print(page)

print()