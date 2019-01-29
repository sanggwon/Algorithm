import random

number = int(input())
count = 0

for i in range(number):
    if (random.random()**2+random.random()**2)**0.5 <= 1 :
        count += 1
print((count/number)*4)