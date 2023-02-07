howold = int(input())
price = float(input())
one_toy = int(input())
counter = 0
money = 0
all = 0

for i in range(1, howold + 1):
    
    if i % 2 == 0:
      money = money + 10
      all += money
      all = all - 1
    else:
        counter += 1

money_toy =  counter * one_toy

final = money_toy + all

if final >= price:
    final1 = final  - price
    print(f"Yes! {final1:.2f}")
else:
    final2 = price - final
    print(f"No! {final2:.2f}")
