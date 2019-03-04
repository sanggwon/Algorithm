
def f(i, j, n):
    global cnt
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    if maze[i][j] == 3 :
        return 1
    else :
        maze[i][j] = 1
        for k in range(4) :
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < n and nj >= 0 and nj < n :
                if maze[ni][nj] != 1 :
                    r = f(ni, nj, n)
                    if r == 1 :
                        cnt += 1
                        return 1
        return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze =  [list(map(int,input())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2 :
                if f(i,j,N) == 1:
                    print("#{} {}".format(tc, cnt-1))
                else :
                    print("#{} 0".format(tc))
                break