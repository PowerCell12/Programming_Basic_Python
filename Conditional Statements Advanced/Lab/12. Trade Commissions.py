city = str(input())
how_big = float(input())

if city == "Sofia":
    if 0 <= how_big <= 500:
        how_big_1 = how_big * 0.05
        print(format(how_big_1, '.2f'))
    elif 500 < how_big <= 1000:
        how_big2 = how_big * 0.07
        print(format(how_big2, ".2f"))
    elif 1000 < how_big <= 10000:
        how_big3 = how_big * 0.08
        print(format(how_big3, ".2f"))
    elif how_big > 10000:
        how_big4 = how_big * 0.12
        print(format(how_big4, ".2f"))

if city == "Varna":
    if 0 <= how_big <= 500:
        how_big_5 = how_big * (4.5 / 100)
        print(format(how_big_5, '.2f'))
    elif 500 < how_big <= 1000:
        how_big6 = how_big * (7.5 / 100)
        print(format(how_big6, ".2f"))
    elif 1000 < how_big <= 10000:
        how_big7 = how_big * 0.1
        print(format(how_big7, ".2f"))
    elif how_big > 10000:
        how_big8 = how_big * 0.13
        print(format(how_big8, ".2f"))

if city == "Plovdiv":
    if 0 <= how_big <= 500:
        how_big_9 = how_big * (5.5 / 100)
        print(format(how_big_9, '.2f'))
    elif 500 < how_big <= 1000:
        how_big10 = how_big * 0.08
        print(format(how_big10, ".2f"))
    elif 1000 < how_big <= 10000:
        how_big11 = how_big * 0.12
        print(format(how_big11, ".2f"))
    elif how_big > 10000:
        how_big12 = how_big * (14.5 / 100)
        print(format(how_big12, ".2f"))


if city != "Sofia" and city != "Varna" and city != "Plovdiv" or how_big < 0:
    print('error')
