n = int(input('Enter the number: '))
i = 1
result = 1
if n < 0:
    print('Incorrect number')
elif n == 0:
    print(1)
else:
    while i <= n:
        result = result * i
        i = i + 1
    print(result)