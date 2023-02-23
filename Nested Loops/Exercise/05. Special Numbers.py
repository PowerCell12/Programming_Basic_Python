special = int(input())
bool = True

for i in range(1111, 10000):
    final1 = str(i)
    for j in range(len(final1)):
        final =  final1[j]
        final = int(final)

        if final == 0:
            bool = False
            break

        if special % final == 0:
            bool = True
        else:
            bool = False
            break
    if bool:
        print(i ,end=" ")
    
    bool = True
