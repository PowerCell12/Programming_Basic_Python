number = int(input())
number1 = 0

while True:
    number1 += int(input())

    if number1 != number and number1 < number:
        continue
 
    if number1 == number or number1 > number:
        print(number1)
        break
