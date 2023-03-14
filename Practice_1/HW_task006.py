while True:
    numb = input('To stop, enter "exit". Enter a six-digit number:')
    if numb == 'exit':
        print('You stopped the program!')
        break
    elif numb.isdigit() == False:
        print('Incorrect! You have to enter number!')
    elif len(numb) <= 5 or len(numb) > 6:
        print('Incorrect number! Try again!')
    else:
        if int(numb[0]) + int(numb[1]) + int(numb[2]) == int(numb[-3]) + int(numb[-2]) + int(numb[-1]):
            print("Yes")
        else:
            print("No")
