products: list[str] = ['Чай', 'Кофе', 'Сахар', 'Мёд']
delete_posotion: int = int(input('Введите позицию для удаления товара'))
products.pop(delete_posotion - 1)
print(f"Товары на полке: {', '.join(products)}")