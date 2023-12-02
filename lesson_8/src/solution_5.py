# Хлеб, Молоко, Сыр
# Молоко, Йогурт, Сок
# Кофе, Чай, Сахар
# Какао, Чай, Сгущёнка

first_shop: set[str] = set(input('Введите товары первого магазина: ').split(', '))
second_shop: set[str] = set(input('Введите товары второго магазина: ').split(', '))

common_products: set[str] = first_shop & second_shop

print()
print(f'Только в первом магазине: {", ".join(list(first_shop - common_products))}')
print(f'Только во втором магазине: {", ".join(list(second_shop - common_products))}')
print()