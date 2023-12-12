def convert_units_with_while(meters: list[int]):
    i: int = 0
    while i < len(meters):
        print(f"{meters[i]} meter(s) = {meters[i] * 3.28084} foot(feet)")
        i += 1


convert_units_with_while([1, 2])   