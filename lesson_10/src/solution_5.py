def analyze_ad_efficiency(clicks: int, shows: int, views: int) -> str:
    if clicks / shows < 0.01 and views > shows:
        return 'Недооценённая'
    elif 0.01 <= clicks / shows <= 0.05:
        return 'Низкая'
    elif 0.05 <= clicks / shows <= 0.1 and views > clicks:
        return 'Средняя'
    elif clicks / shows > 0.1:
        return 'Высокая'
    else:
        return 'Неопределённая'


print(f'Эффективность рекламы {analyze_ad_efficiency(500, 100000, 200)}')