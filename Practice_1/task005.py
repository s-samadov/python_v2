i = int(input("Enter number in carriage: "))
j = int(input("Enter number on carriage: "))
if i == j:
    print("It is not possible to count the number of train carriage")
else:
    count = i + j - 1
    print(f"Count of train carriage {count}")  