def f(i, j, n):
    cnt = 1 # 단지 갯수 스타트
    i_idx = [0,1,0,-1] # 방향
    j_idx = [1,0,-1,0]
    q = [] # 큐
    q.append(i) # 좌표 저장
    q.append(j)
    visited[i][j] = 1 # 저장
    while len(q) != 0 : # 더 이상 갈 곳이 없는 경우
        i = q.pop(0) # 좌표
        j = q.pop(0)

        for k in range(4): # 이동
            ni = i + i_idx[k]
            nj = j + j_idx[k]

            if ni >= 0 and ni < n and nj >= 0 and nj < n : # 틀 지정
                if farm[ni][0][nj] != "0" and visited[ni][nj] == 0 : # 방문한 곳이 0이 아니고 방문하지 않았으면
                    q.append(ni) # 좌표 이동
                    q.append(nj)
                    visited[ni][nj] =1 # 방문표시
                    cnt +=1
    return cnt


N = int(input())
farm = [input().split() for _ in range(N)]
visited = []
for _ in range(N):
    visited.append([0]*N)
cnt_list = []
res = 0
for i in range(N):
    for j in range(N):
        if farm[i][0][j] == "1" and visited[i][j] != 1:
            res +=1
            cnt_list.append(f(i,j,N))
print(res)
for n in sorted(cnt_list):
    print(n)


