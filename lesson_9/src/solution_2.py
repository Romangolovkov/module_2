def convert_to_hex(rgb: tuple[int]) -> str:
    return f'{rgb[0]:X}{rgb[1]:X}{rgb[2]:X}'
    

print(f'HEX: {convert_to_hex((0, 0, 255))}')