N1 = int(input())
N2 = int(input())
operator = str(input())

if operator == "+":
    result = N1 + N2
    if result % 2 == 0:
        print(f"{N1} {operator} {N2} = {result} - even")
    else:
        print(f"{N1} {operator} {N2} = {result} - odd")

if operator == "-":
    result = N1 - N2
    if result % 2 == 0:
        print(f"{N1} {operator} {N2} = {result} - even")
    else:
        print(f"{N1} {operator} {N2} = {result} - odd")

if operator == "*":
    result = N1 * N2
    if result % 2 == 0:
        print(f"{N1} {operator} {N2} = {result} - even")
    else:
        print(f"{N1} {operator} {N2} = {result} - odd")

if operator == "/":
    if N2 != 0:
      result = N1 / N2
      print(f"{N1} / {N2} = {result:.2f}")
    elif N2 == 0:
        print(f"Cannot divide {N1} by zero")

if operator == "%":
    if N2 != 0:
        result = N1 % N2
        print(f"{N1} % {N2} = {result}")
    elif N2 == 0:
        print(f"Cannot divide {N1} by zero")
