def f(n,k,e,c) :
    global minV
    if n==k :
        if minV > c :
            minV = c
    elif minV <= c :
        return
    else:
        if e > 0 :
            f(n+1,k,e-1,c)
        f(n+1,k,bat[n]-1,c+1)

T = int(input())+1
for tc in range(1,T) :
    numbers = list(map(int,input().split()))
    minV = 10000000
    N = numbers[0]
    bat = [0]+numbers[1:]+[0]
    f(2,N,bat[1]-1,0)
    print("#{} {}".format(tc,minV))