from collections import deque
for tc in range(1,11):
    input()
    numbers = deque()
    numbers.extend(map(int,input().split()))
    cnt = 1
    while numbers[-1] != 0 :
        a = numbers.popleft()-cnt
        if a < 0 :
            a = 0
        numbers.append(a)
        cnt+=1
        if cnt == 6 :
            cnt = 1
    print("#{} {}".format(tc,' '.join(map(str,numbers))))