day = input()

if day == "Monday" or day == "Tuesday" or day =="Wednesday" or day == "Thursday" or day == "Friday":
    print("Working day")

elif day == "Saturday" or day == "Sunday":
    print("Weekend")

elif day != "Monday" and day != "Tuesday" and day != "Wednesday" and day != "Thursday" and day != "Friday" and day != "Saturday" and day != "Sunday":
    print("Error")
