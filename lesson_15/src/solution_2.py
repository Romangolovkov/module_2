def update_stock(item: str, quantity: int, stock: dict[str: dict[str: int]]) -> None:
   if item in stock:
      stock[item]['quantity'] += quantity
   else:
      stock[item] = {'quantity': quantity}


def get_item_quantity(item_name: str, stock: dict[str: dict[str: int]]) -> int:
   return stock[item_name]['quantity']


def remove_item(item, stock) -> None:
   if item in stock:
      del stock[item]


stock: dict[str: dict[str: int]] = {}

update_stock('Apple', 50, stock)
update_stock('Banana', 30, stock)
update_stock('Coffee', 20, stock)

print(get_item_quantity('Apple', stock))

remove_item('Banana', stock)

print(stock)