n = int(input('Enter size of chocolate (n):'))
m = int(input('Enter size of chocolate (m):'))

while True:
    numb = input('To stop, enter "exit". Enter the size you want to break:')
    if numb == 'exit':
        print('You stopped the program!')
        break
    elif numb.isdigit() == False:
        print('Incorrect! You have to enter number!')
    elif int(numb) > n * m:
        print('Chocolate is too small! You have to enter another number!')
    elif int(numb) == n * m:
        print('Take it entirely it can not be broken!')
    elif int(numb) % 2 != 0:
        print('No')
    else:
        print('Yes')