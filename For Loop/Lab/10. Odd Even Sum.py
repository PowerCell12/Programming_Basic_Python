how_many_number = int(input())
sum1 = 0
sum2 = 0

for _ in range(1, how_many_number + 1):
    number = int(input())
    if _ % 2 == 0:
        sum1 += number
    else:
        sum2 += number

final = abs(sum1 - sum2)
if sum1 == sum2:
    print("Yes")
    print(f'Sum = {sum1}')
else:
    print("No")
    print(f"Diff = {final}")
