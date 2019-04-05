T = int(input())+1
for tc in range(1,T):
    N,M = map(int,input().split())
    city = [list(map(int,input().split())) for _ in range(N)]
    home = []
    res = 0
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1 :
                home.append((i,j))

    for i in range(N):
        for j in range(N):
            a = 1
            for k in range(N*2):
                a += 4*k
                p = -(a)
                if len(home)*M >= abs(p) :
                    cnt = 0
                    for ni,nj in home :
                        if abs(i-ni)+abs(j-nj) <= k :
                            cnt +=1
                    p += cnt*M
                    if p >= 0 :
                        if res <= cnt :
                            res = cnt
                else :
                    break
    print("#{} {}".format(tc,res))

