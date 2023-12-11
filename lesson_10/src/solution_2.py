def color_background(hour: int) -> str:
    if 6 < hour <= 18:
        print("Цвет фона: Светлый")
    elif 0 <= hour <= 6 or 18 < hour <= 23:
        print("Цвет фона: Тёмный")
    else:
        print('Неверно указано текущее время')


print()
color_background(10)
color_background(20)
color_background(5)
print()