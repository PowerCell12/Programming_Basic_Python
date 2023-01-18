hours = int(input())
day = str(input())

if hours == 10 or hours == 11 or hours == 12 or hours == 13 or hours == 14 or hours == 15 or hours == 16:
 if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday":
       print("open")
 else:
     print("closed")
else:
    print("closed")
