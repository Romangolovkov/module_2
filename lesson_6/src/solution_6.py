products: list[str] = ['Чай', 'Кофе', 'Сахар']
products.insert(1, 'Мёд')
print(f"Товары на полке: {', '.join(products)}")