for tc in range(1,int(input())+1):
    N,K = map(int,input().split())
    F = [list(map(int,input().split())) for _ in range(N)]
    T = []
    M = []
    B = []
    res = 9999
    r_check = 0
    l_check = 0
    for i in range(N-K+1):
        for j in range(N-K+1):
            for n in range(K):
                if K//2 == i-i+n:
                    if K%2 :
                        M.append(F[i+n][j:j+K])
                    else :
                        B.append(F[i+n][j:j+K])
                elif  K/2 > i+n:
                    T.append(F[i+n][j:j+K])
                else :
                    B.append(F[i+n][j:j+K])
            for x in range(len(T)):
                r_check += T[x][x]
                l_check += T[x][-(x+1)]
            T = []
            for y in range(len(M)):
                r_check += M[y][y+K//2]
                l_check += M[y][y+K//2]
            M = []
            for z in range(len(B)):
                r_check += B[-(z+1)][-(z+1)]
                l_check += B[-(z+1)][z]
            B = []
            a = abs(r_check-l_check)
            r_check = 0
            l_check = 0
            if res > a :
                res = a
    print(res)

