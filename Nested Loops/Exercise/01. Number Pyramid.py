number = int(input())
current_num = 1

flag = False

for i in range(1, number + 1):
    for n in range(1, i + 1):
      if current_num > number:
        flag = True
        break
      print(str(current_num) + "", end=' ')
      current_num += 1
    if flag:
        break
    print()
