money_for_the_trip = float(input())
money_saved = float(input())
how_many_times = 0 
every_time_spend = 0


while True:
    what_does_she_do = input()
    sum = float(input())
    how_many_times += 1
    
    if what_does_she_do == "spend":
        every_time_spend += 1  

    if what_does_she_do == "spend":
      money_saved =  money_saved  - sum
 
    if what_does_she_do == "save":
        money_saved = money_saved + sum
        every_time_spend = 0

    if money_saved < 0:
        money_saved = 0 

    if money_saved >= money_for_the_trip:
        print(f"You saved the money for {how_many_times} days.")
        break

    if every_time_spend == 5:
      print("You can't save the money.")
      print(f"{how_many_times}")
      break
