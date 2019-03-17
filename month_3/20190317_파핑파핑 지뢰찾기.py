def find(i,j,N):
    global idx_i,idx_j
    q = []
    q.append((i,j))
    paping[i][j] = 0
    while q :
        check = 0
        i, j = q.pop(0)
        next_idx = []
        for k in range(8):
            ni = i + idx_i[k]
            nj = j + idx_j[k]
            if 0<=ni<N and 0<=nj<N:
                if paping[ni][nj] == "*" :
                    check =1
                    next_idx = []
                    break
                if check == 0 and paping[ni][nj] == ".":
                    next_idx.append((ni,nj))
        paping[i][j] = check
        q.extend(next_idx)
        


            
for tc in range(1,int(input())+1):
# for tc in range(1,2):
    N = int(input())
    # N = 5
    paping = [list(input()) for _ in range(N)]
    # paping = [['.', '.', '*', '.', '.'], ['.', '.', '*', '.', '.'], ['.', '*', '.', '.', '*'], ['.', '*', '.', '.', '.'], ['.', '*', '.', '.', '.']]
    res = 0
    idx_i = [0,1,0,-1,1,-1,1,-1]
    idx_j = [1,0,-1,0,1,-1,-1,1]
    for i in range(N):
        for j in range(N):
            go = 0
            if paping[i][j] == ".":
                for k in range(8):
                    ni = i+idx_i[k]
                    nj = j+idx_j[k]
                    if 0<=ni<N and 0<=nj<N:
                        if paping[ni][nj] == "*" :
                            go = 1
                            break
                if go == 0 :
                    res += 1
                    find(i,j,N)
    for n in range(N):
        res += paping[n].count(".")
    print("#{} {} ".format(tc,res))
