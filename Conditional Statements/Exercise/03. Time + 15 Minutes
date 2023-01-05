hours = int(input())
minutes = int(input())

all_the_time_in_minutes = hours * 60 + minutes + 15

hours2 = all_the_time_in_minutes // 60
minutes2 = all_the_time_in_minutes % 60

if minutes2 < 10 and hours2 < 24:
    print(f'{hours2}:0{minutes2}')
elif minutes2 >= 10 and hours2 < 24:
    print(f'{hours2}:{minutes2}')

if hours2 >= 24 and 10 > minutes2:
    print(f'0:0{minutes2}')
elif hours2 >= 24 and 10 <= minutes2:
    print(f'0:{minutes2}')
