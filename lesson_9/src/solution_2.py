def convert_to_hex() -> str:
    rgb: list[int] = [int(number) for number in input('Введите три числа цветов (R, G, B) от 0 до 255 через запятую: ').split(', ')]
    print(f'HEX: {rgb[0]:X}{rgb[1]:X}{rgb[2]:X}')
    

convert_to_hex()