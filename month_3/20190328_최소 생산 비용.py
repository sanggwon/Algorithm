def f(n,k,s):
    global minV, u
    if n==k :
        if minV > s :
            minV = s
    elif minV < s:
        return
    else :
        for i in range(k):
            if u[i] == 0 :
                u[i] = 1
                f(n+1,k,s+arr[n][i])
                u[i] = 0

T = int(input())+1
for tc in range(1,T) :
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    u = [0]*N
    minV = 10000000
    f(0,N,0)
    print("#{} {}".format(tc,minV))