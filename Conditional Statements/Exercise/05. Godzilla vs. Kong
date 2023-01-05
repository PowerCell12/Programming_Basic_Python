budget = float(input())
statists = int(input())
price_for_cloth_statists = float(input())

decor = budget * (10 / 100)

sum_for_cloth = statists * price_for_cloth_statists

if statists > 150:
    percentage = sum_for_cloth * (10 / 100)
    for_cloth = sum_for_cloth - percentage
    money = for_cloth + decor
    if budget >= money:
        money2 = budget - money
        money3 = format(money2, '.2f')
        print("Action!")
        print(f"Wingard starts filming with {money3} leva left.")
    elif money > budget:
        money4 = money - budget
        money5 = format(money4, '.2f')
        print("Not enough money!")
        print(f"Wingard needs {money5} leva more.")
else:
    money6 = sum_for_cloth + decor
    if budget >= money6:
        money7 = budget - money6
        money10 = format(money7, '.2f')
        print("Action!")
        print(f"Wingard starts filming with {money10} leva left.")
    elif money6 > budget:
        money8 = money6 - budget
        money9 = format(money8, '.2f')
        print("Not enough money!")
        print(f"Wingard needs {money9} leva more.")
