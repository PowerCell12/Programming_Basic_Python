deposit_sum = float(input())
term = int(input())
annual_interest_rate = float(input()) / 100


suma = deposit_sum + term * ((deposit_sum * annual_interest_rate) / 12)

print(suma)
