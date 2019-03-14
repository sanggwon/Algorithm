# def find(i,j,direction,n) :
#     global cnt
#     if i == n-1 and j == n-1 :
#         cnt +=1
#         return
#     else :
#         idx_i = [0,1,1]
#         idx_j = [1,0,1]
#         for k in range(3):
#             ni = i+idx_i[k]
#             nj = j+idx_j[k]
#             if ni < n and nj < n :
#                 if k == 0 and (direction == 0 or direction == 2):
#                     if lists[ni][nj] == 0 :
#                         find(ni,nj,0,n)
#                 elif k == 1 and (direction == 1 or direction == 2):
#                     if lists[ni][nj] == 0 :
#                         find(ni, nj, 1, n)
#                 elif k == 2 :
#                     if lists[ni][nj] == 0 and lists[ni-1][nj] == 0 and lists[ni][nj-1] == 0:
#                         find(ni, nj, 2, n)
#
#
# N = int(input())
# lists = [list(map(int,input().split())) for _ in range(N)]
# cnt = 0
# find(0,1,0,N)
# print(cnt)

#
# def find(i,j,direction,n) :
#     global cnt
#     q = []
#     q.append((i,j,direction))
#     idx_i = [0,1,1]
#     idx_j = [1,0,1]
#     while q :
#         i,j,direction = q.pop(0)
#         for k in range(3):
#             ni = i+idx_i[k]
#             nj = j+idx_j[k]
#             if ni < n and nj < n :
#                 if k == 0 and (direction == 0 or direction == 2):
#                     if lists[ni][nj] == 0 :
#                         if ni != n-1 or nj != n-1:
#                             q.append((ni,nj,0))
#                         if ni == n-1 and nj == n-1:
#                             cnt +=1
#                 elif k == 1 and (direction == 1 or direction == 2):
#                     if lists[ni][nj] == 0 :
#                         if ni != n-1 or nj != n-1:
#                             q.append((ni,nj,1))
#                         if ni == n-1 and nj == n-1:
#                             cnt +=1
#                 elif k == 2 :
#                     if lists[ni][nj] == 0 and lists[ni-1][nj] == 0 and lists[ni][nj-1] == 0:
#                         if ni != n-1 or nj != n-1:
#                             q.append((ni,nj,2))
#                         if ni == n-1 and nj == n-1:
#                             cnt +=1
#
#
# N = int(input())
# lists = [list(map(int,input().split())) for _ in range(N)]
# cnt = 0
# find(0,1,0,N)
# print(cnt)



def find(i,j,direction,n) :
    global cnt
    front = -1
    q = []
    q.append((i,j,direction))
    idx_i = [0,1,1]
    idx_j = [1,0,1]
    while len(q) != front+1 :
        front +=1
        i,j,direction = q[front]
        for k in range(3):
            ni = i+idx_i[k]
            nj = j+idx_j[k]
            if ni < n and nj < n :
                if k == 0 and (direction == 0 or direction == 2):
                    if lists[ni][nj] == 0 :
                        if ni != n-1 or nj != n-1:
                            q.append((ni,nj,0))
                        if ni == n-1 and nj == n-1:
                            cnt +=1
                elif k == 1 and (direction == 1 or direction == 2):
                    if lists[ni][nj] == 0 :
                        if ni != n-1 or nj != n-1:
                            q.append((ni,nj,1))
                        if ni == n-1 and nj == n-1:
                            cnt +=1
                elif k == 2 :
                    if lists[ni][nj] == 0 and lists[ni-1][nj] == 0 and lists[ni][nj-1] == 0:
                        if ni != n-1 or nj != n-1:
                            q.append((ni,nj,2))
                        if ni == n-1 and nj == n-1:
                            cnt +=1


N = int(input())
lists = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
find(0,1,0,N)
print(cnt)

