string: str = input('Введите строку')
print(string[len(string)//2:] + string[:len(string)//2])