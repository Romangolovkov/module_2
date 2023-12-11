def analyze_ad_efficiency(clicks: int, shows: int, views: int) -> str:
    if clicks / shows < 0.01 and views > shows:
        return 'Недооцененная'
    elif 0.01 <= clicks / shows <= 0.05:
        return 'Низкая'
    elif 0.05 <= clicks / shows <= 0.1 and views > clicks:
        return 'Средняя'
    elif clicks / shows > 0.1:
        return 'Высокая'
    else:
        return 'Неопределенная'


print()
print(f'Эффективность рекламы {analyze_ad_efficiency(50, 10000, 15000)}')
print(f'Эффективность рекламы {analyze_ad_efficiency(200, 10000, 5000)}')
print(f'Эффективность рекламы {analyze_ad_efficiency(700, 10000, 800)}')
print(f'Эффективность рекламы {analyze_ad_efficiency(1200, 10000, 1000)}')
print(f'Эффективность рекламы {analyze_ad_efficiency(500, 10000, 200)}')
print()