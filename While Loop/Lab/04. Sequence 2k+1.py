number = int(input())
valid_numbers = 1

while valid_numbers <= number:
    print(valid_numbers)
    valid_numbers = 2 * valid_numbers + 1
