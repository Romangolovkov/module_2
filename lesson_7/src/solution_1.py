words: list[str] = 'Hello world'.split(' ')
reverse_words: list[str] = [word[::-1] for word in words]
print(' '.join(reverse_words))