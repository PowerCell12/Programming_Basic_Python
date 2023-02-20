how_many_bad_grades = int(input())
counting_for_bad_grades = 0 
counting_for_number = 0
total = 0
average = 0
last_problem = ''
name_of_problem = ''


while True:
    last_problem = name_of_problem 
    name_of_problem = str(input())

    if name_of_problem == "Enough":
        print(f"Average score: {average:.2f}")
        print(f"Number of problems: {counting_for_number}")
        print(f"Last problem: {last_problem}")
        break
    
    grade = int(input())
    counting_for_number += 1
 
    if grade  <= 4:
      counting_for_bad_grades += 1


    if counting_for_bad_grades >= how_many_bad_grades:
        print(f"You need a break, {counting_for_bad_grades} poor grades.")
        break
 
    total += grade
    average = total / counting_for_number
