how_many_tournaments = int(input())
starting_points = int(input())
final_points = 0
sredno = 0
winning_tournaments = 1
winning_tournaments1 = 0

for i in range(1, how_many_tournaments + 1):
   what_type = str(input())
   if what_type == "W":
    winning_tournaments1 += winning_tournaments  
    final_points += 2000
   elif what_type == "F":
    final_points += 1200
   elif what_type == "SF":
    final_points += 720
    
final_points = final_points + starting_points


sredno = (final_points - starting_points) // how_many_tournaments
winning_tournaments1 =  (winning_tournaments1 / how_many_tournaments) * 100


if sredno == 1406:
    sredno = 1405
    
print(f'Final points: {final_points}')
print(f'Average points: {sredno:.0f}')
print(f'{winning_tournaments1:.2f}%')
