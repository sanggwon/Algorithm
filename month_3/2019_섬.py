def f(i,j,n):
    global Q
    global res
    res.append(C[i][j])
    idx_i = [0,1,0,-1]
    idx_j = [1,0,-1,0]
    Q.append(i)
    Q.append(j)
    C[i][j] = 0
    while Q :
        i = Q.pop(0)
        j = Q.pop(0)
        for k in range(4):
            ni = i + idx_i[k]
            nj = j + idx_j[k]
            if ni >= 0 and ni < n and nj >= 0 and nj < n :
                if C[ni][nj] != 0 :
                    res.append(C[ni][nj])
                    Q.append(ni)
                    Q.append(nj)
                    C[ni][nj] = 0

for tc in range(1,int(input())+1):
    N = int(input())
    C = [list(map(int,input().split())) for _ in range(N)]
    Q = []
    res = []
    cnt = 0
    for i in range(N):
        for j in range(N) :
            if C[i][j] != 0 :
                f(i,j,N)

                cnt += 1
    print("#{} {} {}".format(tc,cnt, max(res)))

