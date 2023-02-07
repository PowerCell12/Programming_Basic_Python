name = str(input())
points = float(input())
howmany = int(input())
allpoitsgive = 0
counter = 0
final1 = points

for i in range(howmany):
    name1 = str(input())
    pointsgiven = float(input())
    final = final1
    final1  = final + ((len(name1) * pointsgiven) / 2)
    counter += 1       
     
    if counter == 1:
       final = 0

    if final1  > 1250.5:
        print(f"Congratulations, {name} got a nominee for leading role with {final1:.1f}!")
        break

otherone = 1250.5 - final1

if final1 < 1250.6:
    print(f'Sorry, {name} you need {otherone:.1f} more!')
