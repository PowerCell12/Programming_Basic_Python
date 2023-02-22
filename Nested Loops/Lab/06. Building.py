floors = int(input())
rooms = int(input())
number_to_the_floor = ''
base_number = 9
counter = floors + 1
counter1 = 0
flat_name = ''

for i in range(floors, 0, -1):
        if i % 2 ==0:
           number_to_the_floor = "O"
        else:
            number_to_the_floor = "A"
        
        if i == floors:
            number_to_the_floor = "L"

        counter -= 1
        counter1 = 0


        for a in range(rooms):
           if i == floors:
            counter1 += 1 
            if counter1 < 3:
                base_number += 1
                base_number = 10
                base_number = base_number * counter
            if counter1 > 1:
                base_number += 1
            flat_name = f'L{base_number}'    
            print(flat_name, end=' ')
           if i != floors:
             counter1 += 1 
             if counter1 < 3:
                base_number += 1
                base_number = 10
                base_number = base_number * counter
             if counter1 > 1:
                base_number += 1
             flat_name = f'{number_to_the_floor}{base_number}'    
             print(flat_name, end=' ')
        print()
