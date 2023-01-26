month = str(input())
how_many_nights = int(input())

studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50 * how_many_nights
    apartment = 65 * how_many_nights
elif month == "June" or month == "September":
    studio = 75.20 * how_many_nights
    apartment = 68.70 * how_many_nights
elif month == "July" or month == "August":
    studio = 76 * how_many_nights
    apartment = 77 * how_many_nights

what_kind = apartment
what_kind2 = studio

if how_many_nights > 14 and what_kind == apartment:
    apartment = apartment * 0.9

if how_many_nights > 14 and what_kind2 == studio and month != "May" and month != "July" and month != "August" and month != "October":
    studio = studio * 0.80

if 7 < how_many_nights < 15 and what_kind2 == studio and month != "June" and month != "July" and month != "August" and month != "September":
    studio = studio * 0.95

if how_many_nights > 14 and what_kind2 == studio and month != "June" and month != "July" and month != "August" and month != "September":
    studio = studio * 0.70


print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")
