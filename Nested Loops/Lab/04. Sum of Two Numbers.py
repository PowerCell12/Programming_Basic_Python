first_number = int(input())
last_number = int(input())
number_to_get = int(input())
number = 0
how = False
first1 = 0
last1 = 0


for first in range(first_number, last_number + 1):
    for last in range(first_number,last_number + 1):
        number += 1
        if first + last == number_to_get:
            how = True
            first1 = first
            last1 = last
            break
    if how:
        break
             

if how:
    print(f"Combination N:{number} ({first1} + {last1} = {number_to_get})")           
else:
    print(f"{number} combinations - neither equals {number_to_get}")
