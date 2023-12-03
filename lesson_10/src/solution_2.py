def color_background(hour: int) -> str:
    if 6 < hour <= 18:
        print("Цвет фона: Светлый")
    elif 0 <= hour <= 6 or 18 < hour <= 23:
        print("Цвет фона: Тёмный")
    else:
        print('Неверно указано текущее время')


print()
hour: int = int(input('Введите текущий час (от 0 до 23): '))

color_background(hour)
print()