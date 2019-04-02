# def f(n,k,l,r) :
#     global u, N, cnt
#     if l < r :
#         return
#     if n == k :
#         cnt += 1
#     else :
#         for i in range(N):
#             if u[i] == 0 :
#                 u[i] = 1
#                 f(n+1,k,l+Weights[i],r)
#                 f(n+1,k,l,r+Weights[i])
#                 u[i] = 0
#
# T = int(input())+1
# for tc in range(1,T):
#     N = int(input())
#     Weights = list(map(int,input().strip().split()))
#     cnt = 0
#     u = [0]*N
#     f(0,N,0,0)
#     print("#{} {}".format(tc,cnt))

def f(n,k,l,r,ld,rd) :
    if l < r :
        return 0
    if n == k :
        return 1
    elif d[ld][rd] != -1 :
        return d[ld][rd]
    else :
        sum = 0
        for i in range(N):
            if u[i] == 0 :
                u[i] = 1
                sum += f(n+1,k,l+Weights[i],r,ld+(1<<i),rd)
                sum += f(n+1,k,l,r+Weights[i],ld,rd+(1<<i))
                u[i] = 0
        d[ld][rd] = sum
        print(d)
        return sum


T = int(input())+1
for tc in range(1,T):
    N = int(input())
    Weights = list(map(int,input().strip().split()))
    d = [[-1]*(2**N) for _ in range(2**N)]
    u = [0]*N

    print("#{} {}".format(tc,f(0,N,0,0,0,0)))