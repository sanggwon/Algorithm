T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    tk = [0]*N
 
    for i in range(N):
        tk[i] = int(input())
     
    t = max(tk)
    l = 1
    r = t*M
    while(l<r): # 이분탐색으로 시간의 범위를 좁혀감
        s = 0
        mid = (l+r)//2
        for i in range(N):
            s += mid//tk[i]
        if(s<M):
            l = mid+1
        else:
            r = mid
 
    print('#', end='')
    print(tc, end=' ')
    print(l)
