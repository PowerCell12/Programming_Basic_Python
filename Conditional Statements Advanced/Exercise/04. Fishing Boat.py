money_of_the_group = float(input())
season = str(input())
how_many = int(input())

price_boat = 0

if season == "Spring":
 price_boat = 3000
elif season == "Summer":
    price_boat = 4200
elif season == "Autumn":
    price_boat = 4200
elif season == "Winter":
    price_boat = 2600

if how_many <= 6:
    price_boat = price_boat * 0.9
elif 6 < how_many < 12:
    price_boat = price_boat * .85
elif how_many > 11:
    price_boat = price_boat * 0.75


if how_many % 2 == 0 and season != "Autumn":
    price_boat = price_boat * 0.95

money = abs(money_of_the_group - price_boat)

if money_of_the_group >= price_boat:
    print(f"Yes! You have {money:.2f} leva left.")
else:
    print(f"Not enough money! You need {money:.2f} leva.")
