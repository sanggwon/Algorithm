# import sys
# sys.stdin = open("input3.txt","r")
#
# def f(i, j, c, n): # i,j : 좌표, c : 지나온 칸수, n : 크기
#     di = [0,1,0,-1]
#     dj = [1,0,-1,0]
#     global maxV
#     if maxV < c+1:
#         maxV = c+1
#     for k in range(4): # 탐색할 방향
#         ni = i + di[k]
#         nj = j + dj[k]
#
#         if ni >= 0 and ni < n and nj >= 0 and nj < n : # 영역을 벗어나지 않고
#             if M[i][j] > M[ni][nj] : # 더 낮은곳으로 이동
#                 f(ni, nj, c+1, n)
# for tc in range(1,int(input())+1):
#     N,K = map(int,input().split())
#     M = [list(map(int,input().split())) for _ in range(N)]
#     maxV = 0
#     si = 0
#     sj = 0
#     for i in range(N):
#         for j in range(N):
#             if M[si][sj] < M[i][j]:
#                 si = i
#                 sj = j
#             f(i, j, 0, N)
#     print("#{} {}".format(tc,maxV))



import sys
sys.stdin = open("input3.txt","r")

def f(i, j, c, k, n): # i,j : 좌표, c : 지나온 칸수, n : 크기
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    global maxV
    if maxV < c:
        maxV = c
    visited[i][j] = 1
    for p in range(4): # 탐색할 방향
        ni = i + di[p]
        nj = j + dj[p]

        if ni >= 0 and ni < n and nj >= 0 and nj < n : # 영역을 벗어나지 않고
            if visited[ni][nj] != 1 : # 지나온 경로를 깎는 것을 방지
                if M[i][j] > M[ni][nj] : # 더 낮은곳으로 이동
                    f(ni, nj, c+1, k, n)
                elif  M[i][j] > M[ni][nj]-k: # 깍아서 이동
                    pre = M[ni][nj]
                    M[ni][nj] = M[i][j] -1
                    f(ni, nj, c+1, 0, n)
                    M[ni][nj] = pre
    visited[i][j] = 0

for tc in range(1,int(input())+1):
    N,K = map(int,input().split())
    M = [list(map(int,input().split())) for _ in range(N)]
    maxV = 0
    si = 0
    sj = 0
    visited = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if M[si][sj] < M[i][j]:
                si = i
                sj = j
    for i in range(N):
        for j in range(N):
            if M[si][sj] == M[i][j] :
                f(i, j, 1, K, N)
    print("#{} {}".format(tc,maxV))
