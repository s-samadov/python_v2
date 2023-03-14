while True:
    print("Enter the year number. If you want to stop enter number: 0000")
    year = input()
    if year.isdigit() == False:
        print("Incorrect type of input")
    elif int(year) == 0000:
        print("Exit")
        break
    elif int(year) % 4 == 0 and int(year) % 400 and int(year) % 100 != 0:
        print("Yes")
    else:
        print("No")