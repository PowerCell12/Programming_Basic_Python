how_many_groups = int(input())
climbing_musala = 0 
climbing_monblan = 0
climbing_kilimindsharo = 0
climbing_K2 = 0
climbing_everest = 0
all_of_the_people = 0
group_musala = 0
group_monblan = 0
group_kilimindsharo = 0
group_K2 = 0
group_everest = 0


for i in range(1, how_many_groups + 1):
    groups_people = int(input())
    all_of_the_people += groups_people
    if groups_people < 6:
     group_musala += groups_people
    elif 5 < groups_people < 13:
      group_monblan += groups_people
    elif 12 < groups_people < 26:
       group_kilimindsharo += groups_people
    elif 25 < groups_people < 41:
        group_K2 += groups_people
    elif groups_people > 40:
        group_everest += groups_people

climbing_musala = (group_musala / all_of_the_people) * 100
climbing_monblan = (group_monblan / all_of_the_people) * 100
climbing_kilimindsharo = (group_kilimindsharo / all_of_the_people) * 100
climbing_K2 = (group_K2 / all_of_the_people) * 100
climbing_everest = (group_everest / all_of_the_people) * 100
     
print(f'{climbing_musala:.2f}%')
print(f"{climbing_monblan:.2f}%")
print(f"{climbing_kilimindsharo:.2f}%")
print(f"{climbing_K2:.2f}%")
print(f"{climbing_everest:.2f}%")
