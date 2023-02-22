total = 0
flag = False


while True:
    city = str(input())
    if city == "End":
        break
    budget = float(input())
    while True:
        money = float(input())
        total += money
        if total >= budget:
            print(f"Going to {city}!")
            flag = True
            total = 0
            break
