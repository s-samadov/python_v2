while True:
    print("Enter the year number. If you want to stop enter: exit")
    numb = input()
    result = 0 
    if numb == 'exit':
        print('Exit')
        break
    elif numb.isdigit() == False:
        print("Incorrect type of input")
    else:
        while int(numb) > 0:
            result = result + int(numb) % 10
            numb = int(numb) // 10
        print(result)