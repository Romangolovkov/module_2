def count_specific_items_with_while(products: list[str], category: str):
    sum_in_category: int = 0
    i: int = 0
    while i < len(products):
        if products[i] == category:
            sum_in_category += 1
        i += 1
    print(f'Количество {category}: {sum_in_category}')


print()
count_specific_items_with_while(['fruit', 'toy', 'fruit', 'toy'], 'toy')
count_specific_items_with_while(['clothes', 'clothes', 'clothes'], 'clothes')
print()