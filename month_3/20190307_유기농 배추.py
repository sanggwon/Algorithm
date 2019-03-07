def f(i,j,m,n):
    idx_i = [0,1,0,-1]
    idx_j = [1,0,-1,0]

    q = []
    q.append(i)
    q.append(j)
    visited[i][j] = 1
    while len(q) != 0 :
        i = q.pop(0)
        j = q.pop(0)

        for k in range(4):
            ni = i + idx_i[k]
            nj = j + idx_j[k]

            if ni >=0 and ni < n and nj >= 0 and nj < m :
                if farm[ni][nj] != 0 and visited[ni][nj] == 0:
                    q.append(ni)
                    q.append(nj)
                    visited[ni][nj] = 1
    return


for tc in range(1,int(input())+1):
    M,N,K = map(int,input().split())
    farm = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    res = 0
    for _ in range(K):
        j, i = map(int,input().split())
        farm[i][j] = 1

    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and visited[i][j] != 1:
                f(i,j,M,N)
                res += 1
    print(res)
