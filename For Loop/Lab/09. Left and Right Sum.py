how_many_numbers = int(input())
total_fr1 = 0
total_fr2 = 0

for _ in range(how_many_numbers):
    current_number = int(input())
    total_fr1 += current_number


for _ in range(how_many_numbers):
    current_number2 = int(input())
    total_fr2 += current_number2


total_fr3 = abs(total_fr1 - total_fr2)
if total_fr1 == total_fr2:
    print(f'Yes, sum = {total_fr1}')
else:
    print(f'No, diff = {total_fr3}')
