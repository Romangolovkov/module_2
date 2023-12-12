def sales_schedule_with_range(days_amount: int):
    print(f'Дни распродаж: {list(range(3, days_amount + 1, 3))}')


print()
sales_schedule_with_range(30)
sales_schedule_with_range(31)
print()