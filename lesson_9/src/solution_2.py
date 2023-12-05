def convert_to_hex(rgb: tuple[int]) -> str:
    return f'{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}'
    

print(f'HEX: {convert_to_hex((0, 0, 255))}')
