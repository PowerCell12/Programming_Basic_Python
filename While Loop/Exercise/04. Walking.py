goal = 10000
total = 0
walking_to_home = 0

while True:
    steps = input()

    if steps == "Going home":
        walking_to_home = int(input())
        break

    steps = int(steps)

    total += steps

    if total >= goal:
        break


final = 0
final = abs(total - goal + walking_to_home)
final1 = 0
final1 = abs(goal - total - walking_to_home)
total = total + walking_to_home
if total >= goal:
        print("Goal reached! Good job!")
        print(f"{final} steps over the goal!")
else:
        print(f"{final1} more steps to reach goal.")
