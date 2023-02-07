how_many_sites = int(input())
salary = int(input())
salary1 = 0
salary2 = 0 
salary3 = 0

for i  in range(1,how_many_sites + 1):
    n = str(input())
    if n == "Facebook":
      salary1 +=  -150
    elif n == "Instagram":
       salary2 +=  -100
    elif n == "Reddit":
        salary3 += -50

final = salary1 + salary2 + salary3 + salary
if final <= 0:
    print("You have lost your salary.")
else:
    print(final)
