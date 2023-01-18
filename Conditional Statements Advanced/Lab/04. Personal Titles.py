years_old = float(input())
pol = input()

if pol == "m":
    if years_old >= 16:
        print("Mr.")
    else:
        print("Master")
elif pol == "f":
    if years_old >= 16:
        print("Ms.")
    else:
        print("Miss")
