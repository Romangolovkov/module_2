def sort_objects(list_dicts: list[dict[str: int]], str_key: str) -> list[dict[str: int]]:
    return sorted(list_dicts, key=lambda x: x[str_key])



list_dicts: list[dict[str: int]] = [{'red': 100, 'green': 100, 'blue': 100}, 
                                    {'red': 10, 'green': 10, 'blue': 10}, 
                                    {'red': 50, 'green': 50, 'blue': 50},
                                    {'red': 0, 'green': 0, 'blue': 0}]

print(sort_objects(list_dicts, 'red'))