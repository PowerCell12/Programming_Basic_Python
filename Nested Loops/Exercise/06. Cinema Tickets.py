counter = 0
counter1 = 0
kids = 0
standard = 0
student = 0

while True:
    name = input()

    if name == "Finish":
        final1 = (student / counter1) * 100
        final2 = (standard / counter1) * 100
        final3 = (kids / counter1) * 100
        print(f"Total tickets: {counter1}")
        print(f'{final1:.2f}% student tickets.')
        print(f'{final2:.2f}% standard tickets.')
        print(f'{final3:.2f}% kids tickets.')
        break

    space = int(input())

    while True:
        typeTicket = str(input())
        
        if typeTicket == "End":
            break

        counter += 1
        counter1 += 1

        if typeTicket == "student":
            student += 1

        if typeTicket == "standard":
            standard += 1

        if typeTicket == "kid":
            kids += 1

        if space ==  counter:
            break
        
    final = (counter / space) * 100 
    print(f"{name} - {final:.2f}% full.")
    counter = 0
