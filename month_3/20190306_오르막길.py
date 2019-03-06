N = int(input())
numbers = list(map(int,input().split()))
start_num = numbers[0]
next_num = numbers[0]
res = 0
for i in range(1,N) :
    if next_num < numbers[i]:
        next_num = numbers[i]
        if i == N-1 :
            b = next_num - start_num
            if res <= b :
                res = b
    else :
        a = next_num - start_num
        start_num = numbers[i]
        next_num = numbers[i]
        if res <= a :
            res = a
print(res)

