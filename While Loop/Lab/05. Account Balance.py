avaliable_sum = 0

while True:
   current_sum = input()

   if current_sum == "NoMoreMoney":
     break

   current_sum = float(current_sum)

   if current_sum >= 0:
    avaliable_sum += current_sum
    print(f"Increase: {current_sum:.2f}")
   else:
        print("Invalid operation!")
        break

print(f"Total: {avaliable_sum:.2f}")
