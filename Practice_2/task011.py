n = int(input('Enter the number: '))
a = 0
b = 1
i = 0
if n == 0:
    print(i)
else:
    while a < n:
        a, b = b, a + b
        i = i + 1
    if n == a:
        print(f"Counter of number {i}")
    else:
        print('-1')