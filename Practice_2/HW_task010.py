import random
n = int(input('Enter count of coins: '))
my_list = list()
heads = 0
tails = 0

for i in range(int(n)):
    my_list.append(random.randint(0, 1))
    if my_list[i] != 0:
        heads += 1
    if my_list[i] == 0:
        tails += 1
print(my_list)
if heads > tails:
    print(f'Need to flip {tails} tails')
else:
    print(f'Need to flip {heads} heads')