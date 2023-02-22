prime = 0
non_prime = 0
bool = True

while True:
    number = input()

    if number == "stop":
        break

    number = int(number)

    if number < 0:
        print("Number is negative.")
        continue

    for i in range(2, number):
        for j in range(2, number):
            final = i *  j

            if final == number:
                non_prime += number
                bool = False
                break

        if bool == False:
            break

    if bool:
        prime += number

    bool = True



print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {non_prime}")
