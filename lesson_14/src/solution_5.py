def categorization(list_products: list[tuple[str]]) -> dict[str, int]:   
   types_products: list[str] = list(map(lambda product: product[1], list_products))
   return {type: types_products.count(type) for type in types_products}
   

print()
print(categorization([('Рубашка', 'Одежда'), ('Кружка', 'Посуда')]))
print(categorization([('Рубашка', 'Одежда'), ('Штаны', 'Одежда'), ('Кружка', 'Посуда')]))
print(categorization([('Ручка', 'Канцелярия'), ('Тетрадь', 'Канцелярия'), ('Кружка', 'Посуда'), ('Стул', 'Мебель')]))
print()