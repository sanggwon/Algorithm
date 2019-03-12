def find(i,j,n):
    cnt = 1
    idx_i = [0,1,0,-1]
    idx_j = [1,0,-1,0]
    q = []
    q.append((i,j))
    while q :
        i,j = q.pop(0)
        for k in range(4):
            ni = i + idx_i[k]
            nj = j + idx_j[k]
            if 0 <= ni < n and 0 <= nj < n :
                if room[ni][nj] - room[i][j] == 1 :
                    cnt += 1
                    q.append((ni,nj))
    return cnt




for tc in range(1,int(input())+1):
    N = int(input())
    room = [list(map(int,input().split())) for _ in range(N)]
    res = 0
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            a = find(i,j,N)
            if max_cnt < a :
                max_cnt = a
                res = room[i][j]
            elif max_cnt == a :
                if res > room[i][j] :
                    res = room[i][j]
    print("#{} {} {}".format(tc,res, max_cnt))