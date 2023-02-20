money_needed = float(input())

money_needed_coins = money_needed * 100
coins_final = 0


while True:
   if money_needed_coins >= 200:
      coins_final +=1
      money_needed_coins = money_needed_coins - 200
      if money_needed_coins == 200:
        continue

   elif money_needed_coins >= 100:
      coins_final +=1
      money_needed_coins = money_needed_coins - 100
      if money_needed_coins == 100:
        continue

   elif money_needed_coins >= 50:
      coins_final +=1
      money_needed_coins = money_needed_coins - 50
      if money_needed_coins == 50:
        continue

   elif money_needed_coins >= 20:
      coins_final +=1
      money_needed_coins = money_needed_coins - 20
      if money_needed_coins == 20:
        continue
    
   elif money_needed_coins >= 10:
      coins_final +=1
      money_needed_coins = money_needed_coins - 10
      if money_needed_coins == 10:
        continue

   elif money_needed_coins >= 5:
      coins_final +=1
      money_needed_coins = money_needed_coins - 5
      if money_needed_coins == 5:
        continue

   elif money_needed_coins >= 2:
      coins_final += 1
      money_needed_coins = money_needed_coins - 2      
      if money_needed_coins == 2:
        continue


   elif money_needed_coins >= 1:
      coins_final +=1
      money_needed_coins = money_needed_coins - 1

   elif money_needed_coins == 0:
            break
   else:
       break


print(coins_final)
