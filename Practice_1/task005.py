while True:
    i = input("Enter number in carriage: ")
    j = input("Enter number on carriage: ")
    if i.isdigit() == False or j.isdigit == False:
        print("Incorrect type of input")
    else:
        break  

if i == j:
    print("It is not possible to count the number of train carriage")
else:
    count = int(i) + int(j) - 1
    print(f"Count of train carriage {count}")  