hourdexam = int(input())
minutesexam = int(input())
hoursthere = int(input())
minutesthere = int(input())

minutesexamfinal = hourdexam * 60 + minutesexam
minutesthere = hoursthere * 60  + minutesthere
if1 = minutesthere - minutesexamfinal
diff = abs(minutesexamfinal - minutesthere)
diff1 = diff // 60
diff2 = diff %  60

if minutesthere > minutesexamfinal:
    print("Late")
    if diff >= 60:
        hours = diff // 60
        minutes = diff % 60
        print(f'{hours}:{minutes:02d} hours after the start')
    else:
        print(f'{diff} minutes after the start')
elif diff <= 30 or minutesthere == minutesexamfinal:
    print("On time")
    if diff > 0:
     print(f"{diff} minutes before the start")
else:
    minutesthere  < minutesexamfinal
    print("Early")
    if diff >= 60:
        hours = diff // 60
        minutes = diff % 60
        print(f'{hours}:{minutes:02d} hours before the start')
    else:
        print(f'{diff} minutes before the start')
