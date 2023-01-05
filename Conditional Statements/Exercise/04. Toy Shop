ekskurziq = float(input())
puzzles = int(input())
dolls = int(input())
bear = int(input())
minion = int(input())
kamion = int(input())

sum1 = puzzles * 2.60 + dolls * 3 + bear * 4.10 + minion * 8.20 + kamion * 2
all = puzzles + dolls + bear + minion + kamion

if all >= 50:
    sum1 = sum1 - sum1 * 0.25

sum1 = sum1 - sum1 * 0.10
price_without_money = ekskurziq - sum1
price_without_money1 = sum1 - ekskurziq

if sum1 >= ekskurziq:
    print(f"Yes! {price_without_money1:.2f} lv left.")
else:
   print(f"Not enough money! {price_without_money:.2f} lv needed.")
