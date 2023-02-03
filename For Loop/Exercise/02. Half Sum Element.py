import sys

numbers_how_many = int(input())
biggest_number = -sys.maxsize
total = 0

for i in range(numbers_how_many):
 number = int(input())
 total += number
 if number > biggest_number:
  biggest_number = number


all_of_them = total - biggest_number
final = abs(all_of_them - biggest_number)
if biggest_number == all_of_them:
    print("Yes")
    print(f'Sum = {all_of_them}')
else:
    print("No")
    print(f'Diff = {final}')
