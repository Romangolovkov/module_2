books = int(input('Введите количество коробок с книгами'))
stationery = int(input('Введите количество коробок с канцтоварами'))
toys = int(input('Введите количество коробок с игрушками'))
print(f'Общий объём коробок с товарами равен {books * 2 + stationery * 1.5 + toys * 3} кубических метров')