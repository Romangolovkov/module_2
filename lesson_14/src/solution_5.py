def sort(products):
    products_dict = {}
    for product in products:
        if product[1] in products_dict:
            products_dict[product[1]] = products_dict[product[1]] + 1
        else:
         products_dict[product[1]] = 1
    return products_dict

def sort2(products):
   products_dict = {}
   return map(lambda product: products_dict[product[1]] = 1, products)


print(sort2([('Рубашка', 'Одежда'), ('Кружка', 'Посуда')]))
print(sort2([('Рубашка', 'Одежда'), ('Штаны', 'Одежда'), ('Кружка', 'Посуда')]))