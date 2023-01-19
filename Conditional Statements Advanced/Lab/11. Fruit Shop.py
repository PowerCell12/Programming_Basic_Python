fruit = input()
day = input()
how_much = float(input())

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
 if fruit == "banana":
  print(format((how_much * 2.50), ".2f"))
 elif fruit == "apple":
  print(format((how_much * 1.20), ".2f"))
 elif fruit == "orange":
   print(format((how_much * 0.85), ".2f"))
 elif fruit == "grapefruit":
    print(format((how_much * 1.45), ".2f"))
 elif fruit == "kiwi":
    print(format((how_much * 2.70), ".2f"))
 elif fruit == "pineapple":
    print(format((how_much * 5.50), ".2f"))
 elif fruit == "grapes":
    print(format((how_much * 3.85), ".2f"))

if day == "Saturday" or day == "Sunday":
 if fruit == "banana":
  print(format((how_much * 2.70), ".2f"))
 elif fruit == "apple":
  print(format((how_much * 1.25), ".2f"))
 elif fruit == "orange":
   print(format((how_much * 0.90), ".2f"))
 elif fruit == "grapefruit":
    print(format((how_much * 1.60), ".2f"))
 elif fruit == "kiwi":
    print(format((how_much * 3.00), ".2f"))
 elif fruit == "pineapple":
    print(format((how_much * 5.60), ".2f"))
 elif fruit == "grapes":
    print(format((how_much * 4.20), ".2f"))


if fruit != "banana" and fruit != "apple" and fruit != "orange" and fruit != "grapefruit" and fruit != "kiwi" and fruit != "pineapple" and fruit != "grapes":
    print("error")
elif day != "Monday" and day != "Tuesday" and day != "Wednesday" and day != "Thursday" and day != "Friday" and day != "Saturday" and day != "Sunday":
    print("error")
