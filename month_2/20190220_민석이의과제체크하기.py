for tc in range(int(input())) :
    N, K = input().split()
    S = map(int,input().split())
    print(f"#{tc+1} {' '.join(map(str,list(set(range(1,int(N)+1))-set(S))))}")
