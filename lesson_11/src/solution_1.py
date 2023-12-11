def sum_sales_with_for(sales: list[int]):
    sum_sales: int = 0
    for sale in sales:
        sum_sales += sale
    print(*sales, sep = '+', end = '=')
    print(sum_sales)


sum_sales_with_for([100, 200, 300])
sum_sales_with_for([15, 23, 39, 50])