number_how_many = int(input())
how_many_numbers1 = 0 
how_many_numbers2 = 0
how_many_numbers3 = 0
how_many_numbers4 = 0
how_many_numbers5 = 0
all_of_the_numbers = 0


for i in range(number_how_many):
    number = int(input()) 
    if number < 200:
        all_of_the_numbers = number
        how_many_numbers1 += (number / number_how_many * 100)  / all_of_the_numbers
    elif 199 < number < 400:
        all_of_the_numbers = number
        how_many_numbers2 += (number / number_how_many * 100) / all_of_the_numbers
    elif 399 < number < 600:
        all_of_the_numbers = number
        how_many_numbers3 += (number / number_how_many * 100) / all_of_the_numbers
    elif 599 < number < 800:
        all_of_the_numbers = number
        how_many_numbers4 += (number / number_how_many * 100) / all_of_the_numbers
    elif number > 799:
        all_of_the_numbers = number
        how_many_numbers5 += (number / number_how_many * 100) / all_of_the_numbers


print(f'{how_many_numbers1:.2f}%')
print(f'{how_many_numbers2:.2f}%')
print(f'{how_many_numbers3:.2f}%')
print(f'{how_many_numbers4:.2f}%')
print(f'{how_many_numbers5:.2f}%')
