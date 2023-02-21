lenght = int(input())
width = int(input())
height = int(input())

space = lenght  * width * height


while True:
    space_taken_from_boxe =  input()

    if space_taken_from_boxe == "Done":
        break

    space_taken_from_boxe = int(space_taken_from_boxe)

    space = space - space_taken_from_boxe

    if space <= 0:
        break

final = 0 
final = abs(space)

if space >= 0:
    print(f"{final} Cubic meters left.")
else:
     print(f"No more free space! You need {final} Cubic meters more.")
