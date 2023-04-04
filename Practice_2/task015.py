import random
n = int(input('Enter count of watermelons: '))
wm_weight = list()

for i in range(int(n)):
    wm_weight.append(random.randint(1, 10))
print(wm_weight)

min = wm_weight[0]
max = wm_weight[0]

for i in range(int(n)):
    if(wm_weight[i] < min):
        min = wm_weight[i]
    if(wm_weight[i] > max):
        max = wm_weight[i]
print(f'Min weight is {min}, Max weight is {max}')

