from collections import deque


def mine(paping, N) :
    global idx_i,idx_j
    for i in range(N):
        for j in range(N):
            if paping[i][j] == -1 :
                for k in range(8):
                    ni = i + idx_i[k]
                    nj = j + idx_j[k]
                    if 0<=ni<N and 0<=nj<N :
                        if paping[ni][nj] != -1 :
                            paping[ni][nj] +=1

def bfs(paping, n, m) :
    global idx_i, idx_j
    q = deque()
    q.append((n,m))
    paping[n][m] = -2

    while q :
        n, m = q.popleft()
        for k in range(8) :
            ni = n + idx_i[k]
            nj = m + idx_j[k]
            if 0 <= ni < N and 0 <= nj < N:
                if paping[ni][nj] != -1 and paping[ni][nj] == 0 :
                    q.append((ni,nj))
                paping[ni][nj] = -2

for tc in range(1, int(input()) + 1) :
    N = int(input())
    paping = [list(input()) for _ in range(N)]
    idx_i = [-1, -1, -1, 0, 1, 1, 1, 0]
    idx_j = [-1, 0, 1, 1, 1, 0, -1, -1]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if paping[i][j] == "*" :
                paping[i][j] = -1
            else :
                paping[i][j] = 0

    mine(paping, N)

    for n in range(N):
        for m in range(N):
            if paping[n][m] == 0 :
                cnt += 1
                bfs(paping, n, m)

    for x in range(N) :
        for y in range(N):
            if paping[x][y] > 0 :
                cnt += 1

    print("#{} {} ".format(tc, cnt))
