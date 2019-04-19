import copy

idx_i = [0,-1,0]
idx_j = [-1,0,1]

def bfs(i,j,ar_list):
    q = []
    q.append((i,j))
    visited_copy[i][j] = 1
    if (i, j) in en_list_copy:
        ar_list.append((i, j))
        return
    while q :
        i,j = q.pop(0)
        for k in range(3) :
            ni = i + idx_i[k]
            nj = j + idx_j[k]
            if 0<=ni<N and 0<=nj<M:
                if visited_copy[ni][nj] == 0 :
                    if visited_copy[i][j] + 1 == D+1 :
                        return
                    if (ni,nj) in en_list_copy :
                        ar_list.append((ni,nj))
                        return
                    visited_copy[ni][nj] = visited_copy[i][j]+1
                    q.append((ni,nj))


N, M, D = map(int,input().strip().split())
en = [list(map(int,input().strip().split())) for _ in range(N)]

max_count = 0

en_list = []
for i in range(N):
    for j in range(M):
        if en[i][j] == 1:
            en_list.append((i,j))



visited = [[0] * M for _ in range(N)]
for ar1 in range(M-2):
    for ar2 in range(ar1+1,M-1):
        for ar3 in range(ar2+1,M):
            en_list_copy = copy.deepcopy(en_list)
            count = 0
            while en_list_copy :
                ar1_kill = []
                ar2_kill = []
                ar3_kill = []
                visited_copy = copy.deepcopy(visited)
                bfs(N - 1, ar1, ar1_kill)
                visited_copy = copy.deepcopy(visited)
                bfs(N - 1, ar2, ar2_kill)
                visited_copy = copy.deepcopy(visited)
                bfs(N - 1, ar3, ar3_kill)

                ar_kill = []
                ar_kill.extend(ar1_kill)
                ar_kill.extend(ar2_kill)
                ar_kill.extend(ar3_kill)
                ar_kill = list(set(ar_kill))

                for de in ar_kill :
                    en_list_copy.remove(de)
                    count += 1

                en_list_copy = list(map(list,en_list_copy))

                for mo in en_list_copy :
                    mo[0] += 1

                en_list_copy_copy = []

                for mo in en_list_copy :
                    if mo[0] != N :
                        en_list_copy_copy.append(mo)

                en_list_copy = list(map(tuple,en_list_copy_copy))

            if max_count < count :
                max_count = count
print(max_count)
