def dfs(i,j,num_add):
    global numbers, min_num, N
    if i == N-1 and j == N-1 :
        if min_num > num_add :
            min_num = num_add
        return
    elif num_add >= min_num :
        return
    else :
        ind_i = [0,1]
        ind_j = [1,0]
        for k in range(2) :
            ni,nj = i + ind_i[k],j + ind_j[k]
            if ni < N and nj < N :
                dfs(ni,nj,num_add+numbers[ni][nj])

for tc in range(1,int(input())+1):
    N = int(input())
    numbers = [list(map(int,input().split())) for _ in range(N)]
    num_add = numbers[0][0]
    min_num = 1000
    dfs(0,0,num_add)
    print("#{} {}".format(tc,min_num))
