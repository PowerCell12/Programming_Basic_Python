kind_flowers = input()
number_of_flowers = int(input())
finance = int(input())

price = 0

if kind_flowers == "Roses":
    price = 5 * number_of_flowers
    if number_of_flowers > 80:
        price = price * .90
elif kind_flowers == "Dahlias":
    price = 3.80 * number_of_flowers
    if number_of_flowers > 90:
        price = price * .85
elif kind_flowers == "Tulips":
    price = 2.80 * number_of_flowers
    if number_of_flowers > 80:
        price = price * .85
elif kind_flowers == "Narcissus":
    price = 3 * number_of_flowers
    if number_of_flowers < 120:
        price = price * 1.15
elif kind_flowers == "Gladiolus":
    price = 2.50 * number_of_flowers
    if number_of_flowers < 80:
        price = price * 1.20

money_left = abs(finance - price)

if finance >= price:
    print(f"Hey, you have a great garden with {number_of_flowers} {kind_flowers} and {money_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_left:.2f} leva more.")
