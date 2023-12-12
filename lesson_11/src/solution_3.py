def track_low_stock_with_for(products: dict[str, int], level: int):
    print('Низкий запас:')
    for product, number in products.items():
        if products[product] < level:
            print(f"{product} - {number}")


print()
track_low_stock_with_for({'': 50, 'bananas': 10, 'cherries': 3}, 15)
print()