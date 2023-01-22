budget = float(input())
season = str(input())

where = "Bulgaria" or "Balkans" or "Europe"
what = "Camp" or "Hotel"

if budget <= 100:
    where = "Bulgaria"
    if season == "summer":
        budget = budget * 0.3
        what = "Camp"
    elif season == "winter":
        budget = budget * 0.7
        what = "Hotel"
elif 100 < budget < 1001:
    where = "Balkans"
    if season == "summer":
        budget = budget * 0.4
        what = "Camp"
    elif season == "winter":
        budget = budget * 0.8
        what = "Hotel"
elif budget > 1000:
    where = "Europe"
    budget = budget * 0.9
    what = "Hotel"

print(f"Somewhere in {where}")
print(f"{what} - {budget:.2f}")
