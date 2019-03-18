import sys
sys.stdin = open("input.txt", "r")
for tc in range(1, int(input())+1):
    N,X = map(int,input().split())
    airstrip = [list(map(int,input().split())) for _ in range(N)]
    cnt = N*2
    res = set()
    for i in range(N):
        visited = [0]*N
        for _ in range(2):
            start = airstrip[i][0]
            q = []
            for j in range(N):
                if airstrip[i][j] == start :
                    q.append(j)
                else :
                    if airstrip[i][j] > start :
                        if airstrip[i][j] - start != 1 :
                            res.add(i)
                        elif len(q) < X :
                            res.add(i)
                        else :
                            for m in range(X):
                                if visited[q[len(q)-m-1]] == 1 :
                                    res.add(i)
                                    break
                                else :
                                    visited[q[len(q)-m-1]] = 1
                    q = [j]
                    start = airstrip[i][j]
            for n in range(N // 2):
                airstrip[i][n], airstrip[i][N-n-1] = airstrip[i][N-n-1], airstrip[i][n]
                visited[n], visited[N-n-1] = visited[N-n-1], visited[n]
    cnt -= len(res)
    res = set()
    for i in range(N):
        visited = [0]*N
        for _ in range(2):
            start = airstrip[0][i]
            q = []
            for j in range(N):
                if airstrip[j][i] == start :
                    q.append(j)
                else :
                    if airstrip[j][i] > start :
                        if airstrip[j][i] - start != 1 :
                            res.add(i)
                        elif len(q) < X :
                            res.add(i)
                        else :
                            for m in range(X):
                                if visited[q[len(q)-m-1]] == 1 :
                                    res.add(i)
                                    break
                                else :
                                    visited[q[len(q)-m-1]] = 1

                    q = [j]
                    start = airstrip[j][i]
            for n in range(N // 2):
                airstrip[n][i], airstrip[N-n-1][i] = airstrip[N-n-1][i], airstrip[n][i]
                visited[n], visited[N-n-1] = visited[N-n-1], visited[n]
    cnt -= len(res)
    print("#{} {}".format(tc,cnt))


