how_many_days = int(input())
kind_of_apartment = str(input())
grade = str(input())

percentage = 0
nights = how_many_days - 1
price = 0

if kind_of_apartment == "room for one person":
    price = 18
    percentage = 1
elif kind_of_apartment == "apartment":
    price = 25
    if how_many_days < 10:
        percentage = 0.7
    elif 10 < how_many_days < 15:
        percentage = 0.65
    elif how_many_days > 15:
        percentage = 0.5
elif kind_of_apartment == "president apartment":
    price = 35
    if how_many_days < 10:
        percentage = 0.9
    elif 10 < how_many_days < 15:
        percentage = 0.85
    elif how_many_days > 15:
        percentage = 0.80

if grade == "positive":
    percentage = percentage  + percentage * 0.25
elif grade == "negative":
     percentage = percentage - percentage * 0.1

final = nights * percentage * price
print(f'{final:.2f}')
