lenght = int(input())
width = int(input())

pieces = lenght * width

while True:
    takes = input()

    if takes == "STOP":
        break

    takes = int(takes)

    pieces = pieces - takes

    if pieces <= 0:
        break


final = 0
final = abs(pieces)

if pieces >= 0:
    print(f"{final} pieces are left.")
elif pieces < 0:
    print(f"No more cake left! You need {final} pieces more.")
