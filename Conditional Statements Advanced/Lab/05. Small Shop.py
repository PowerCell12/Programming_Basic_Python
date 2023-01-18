product = str(input())
city = str(input())
how_much = float(input())

if city == "Sofia":
    if product == "coffee":
        print(how_much * 0.50)
    elif product == "water":
        print(how_much * 0.80)
    elif product == "beer":
        print(how_much * 1.20)
    elif product == "sweets":
        print(how_much * 1.45)
    elif product == "peanuts":
        print(how_much * 1.60)
elif city == "Plovdiv":
    if product == "coffee":
        print(how_much * 0.40)
    elif product == "water":
        print(how_much * 0.70)
    elif product == "beer":
        print(how_much * 1.15)
    elif product == "sweets":
        print(how_much * 1.30)
    elif product == "peanuts":
        print(how_much * 1.50)
elif city == "Varna":
    if product == "coffee":
        print(how_much * 0.45)
    elif product == "water":
        print(how_much * 0.70)
    elif product == "beer":
        print(how_much * 1.10)
    elif product == "sweets":
        print(how_much * 1.35)
    elif product == "peanuts":
        print(how_much * 1.55)
