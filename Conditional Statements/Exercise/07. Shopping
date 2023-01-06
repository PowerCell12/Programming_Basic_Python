money = float(input())
videocards = int(input())
processors = int(input())
rampamet = int(input())

sumvideocards = videocards * 250
sumprocessors = sumvideocards * 0.35
sumprocessors = processors * sumprocessors
sumrampamet = sumvideocards * 0.10
sumrampamet = rampamet * sumrampamet

sum_final = sumrampamet + sumprocessors + sumvideocards

if videocards > processors:
    sum_final = sum_final - sum_final * 0.15


money_left = money - sum_final
money_needed = sum_final - money

if sum_final <=  money:
    print(f"You have {money_left:.2f} leva left!")
else:
    print(f'Not enough money! You need {money_needed:.2f} leva more!')
