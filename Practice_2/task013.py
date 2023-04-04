import random
n = int(input('Enter count of days: '))
temp = list()
count = 0
result = 0

for i in range(int(n)):
    temp.append(random.randint(-50, 50))
print(temp)

for i in range(int(n)):
    if(int(temp[i] > 0)):
        count += 1
    else:
        if(count > result):
            result = count
        count = 0
print(f'Thaw lasted {result} days')

