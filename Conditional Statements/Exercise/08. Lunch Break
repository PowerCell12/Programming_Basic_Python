import math
name = str(input())
episode_time = int(input())
timebreak = int(input())

lunch = timebreak * (1 / 8)
otdix = timebreak * (1 / 4)
lasttime = timebreak - lunch - otdix

def round_up(n, decimals=0): 
    multiplier = 10 ** decimals 
    return math.ceil(n * multiplier) / multiplier

freetime = lasttime - episode_time
freetime = round_up(freetime)
neededtime = episode_time - lasttime
neededtime = round_up(neededtime)

if lasttime >= episode_time:
    print(f"You have enough time to watch {name} and left with {freetime:.0f} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {neededtime:.0f} more minutes.")
