prices_1: list[str] = ['50', '45', '30', '25']
prices_2: list[str] = ['100', '90', '85', '70', '60']
print("Цены без скидки: " + ', '.join(prices_1[1::2]))
print("Цены без скидки: " + ', '.join(prices_2[1::2]))