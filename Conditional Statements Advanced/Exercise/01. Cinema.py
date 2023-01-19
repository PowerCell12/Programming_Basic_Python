type_project = str(input())
lines = int(input())
colums = int(input())

all_of_the_holle = lines * colums

if type_project == "Premiere":
    print(format(all_of_the_holle * 12, ".2f") + " leva")
elif type_project == "Normal":
    print(format(all_of_the_holle * 7.50, '.2f') + " leva")
elif type_project == "Discount":
    print(format(all_of_the_holle * 5, '.2f') + ' leva')
