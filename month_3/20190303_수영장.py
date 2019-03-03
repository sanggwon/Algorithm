import sys 
sys.stdin = open("input.txt","r")

for tc in range(1,int(input())+1):
    D,M,T,Y = map(int,input().split())
    plan = list(map(int,input().split()))
    
    res = Y
    stack = []
    my_sum = 0
    for i in plan :
        if i != 0 :
            if i*D <= M :
                stack.append(i*D)
            elif i*D > M :
                stack.append(M)
            if len(stack) == 3:
                if sum(stack) > T :
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    my_sum += T
                else :
                    my_sum += stack.pop(0)
    if sum(stack) < T :
        my_sum += sum(stack)
    else :
        my_sum+=T
    if res > my_sum :
        res = my_sum
    print(f"#{tc} {res}")

