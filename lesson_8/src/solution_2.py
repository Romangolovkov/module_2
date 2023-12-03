input_word = 1
words: dict[str, str] = {'Красивый': 'Прекрасный', 'Уродливый': 'Некрасивый', 'Сложный': 'Запутанный', 'Простой': 'Легкий'}
print()

while input_word != '0':
    input_word: str = input('Введите слово для получения синонима, либо "0" для выхода: ')

    if input_word in words:
        print(f'Синоним: {words[input_word]}')

    elif input_word in words.values():
        for key, val in words.items():
            if input_word == val:
                print(f'Синоним: {key}')

    elif input_word != '0':
        words[input_word] = input('Данного слова в словаре нет, введите его синоним, чтобы добавить в словарь: ')

print()
print(f'Словарь синонимов: {words}')
print()