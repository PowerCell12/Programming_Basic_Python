number1 = int(input())
number2 = int(input())

for i in range(number1, number2 + 1):
  number_to_str = str(i)
  odd_sum = 0
  even_sum = 0

  for a, b in enumerate(number_to_str):
    if a % 2 == 0:
      odd_sum += int(b)
    else:
      even_sum += int(b)

  if even_sum == odd_sum:
    print(i, end=" ")
