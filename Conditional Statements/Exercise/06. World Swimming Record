record_in_seconds = float(input())
raztoqnie = float(input())
secondsfor1m = float(input())

seconds = raztoqnie * secondsfor1m

vreme1 = raztoqnie / 15 
vreme1 = int(vreme1)
vreme2 = vreme1 * 12.5
all_time = vreme2 + seconds

time_needed = all_time - record_in_seconds

if all_time < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {all_time:.2f} seconds.')
elif all_time >= record_in_seconds:
    print(f"No, he failed! He was {time_needed:.2f} seconds slower.")
