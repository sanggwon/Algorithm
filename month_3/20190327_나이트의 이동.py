def bfs(i,j):
    global ind_i,ind_j,N,start_i,start_j
    front = 0
    q = []
    q.append((i,j))
    while front != len(q) :
        i,j = q[front]
        front +=1
        for k in range(8):
            ni = i + ind_i[k]
            nj = j + ind_j[k]
            if 0<=ni<N and 0<=nj<N:
                if visitied[ni][nj] == 0 :
                    q.append((ni,nj))
                    visitied[ni][nj] = visitied[i][j]+1
                    if ni == start_i and nj == start_j :
                        return

ind_i = [-1,-2,-2,-1,1,2,2,1]
ind_j = [2,1,-1,-2,-2,-1,1,2]
for tc in range(1,int(input())+1):
    N = int(input())
    start_i,start_j = map(int,input().split())
    end_i, end_j = map(int,input().split())
    visitied = [[0]*N for _ in range(N)]
    visitied[end_i][end_j] = 1
    bfs(end_i,end_j)
    print(visitied[start_i][start_j]-1)