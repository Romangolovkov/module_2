def choose_ad_platform(budget: int) -> str:
    if budget < 1000:
        return 'Google'
    elif 1000 <= budget <= 5000:
        return 'Facebook'
    else:
        return 'Instagram'


print(choose_ad_platform(6000))