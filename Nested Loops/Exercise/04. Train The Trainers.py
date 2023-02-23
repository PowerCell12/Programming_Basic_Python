NumberOfPeople = int(input())
all = 0
all1 = 0
counter = 0

while True:
    name = input()

    if name == "Finish":
        all1 = all1 / counter 
        print(f"Student's final assessment is {all1:.2f}.")
        break

    for i in range(0, NumberOfPeople):
        grade = float(input())
        all += grade
        all1 += grade
        counter += 1

    all = all / NumberOfPeople
    print(f"{name} - {all:.2f}.")
    all = 0
