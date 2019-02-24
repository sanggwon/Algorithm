def num(N,M):
    if M == 1 :
        return N
    return N*num(N,M-1)
for tc in range(10):
    print(f"#{input()}",end=" ")
    M,N = map(int,input().split())
    print(f"{num(M,N)}")
