book_searching_for = input()
how_many = 0


while True:
    book = input()

    if book == book_searching_for:
        print(f"You checked {how_many} books and found it.")
        break
    
    if book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {how_many} books.")
        break

    how_many += 1
