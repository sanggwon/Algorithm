import sys
sys.stdin = open("input.txt","r")
T = int(input().strip())+1
for tc in range(1,T):
    M , N = map(int,input().strip().split())
    A = [0]+list(map(int,input().strip().split()))
    B = [0]+list(map(int,input().strip().split()))
    AP = [list(map(int,input().strip().split())) for _ in range(N)]
    AP.sort(key= lambda x:x[1])
    AP_list = [[] for _ in range(N)]
    arr = [[0]*10 for _ in range(10)]
    idx_i = [0,1,0,-1]
    idx_j = [1,0,-1,0]
    num = -1
    ap_num = 0
    res = 0
    for i in range(10):
        for j in range(10):
            if ap_num != N :
                if i == AP[ap_num][1]-1 and j == AP[ap_num][0]-1 :
                    num += 1
                    arr[i][j] = 1
                    check = 0
                    q = []
                    q.append((i,j))
                    AP_list[num].append((i,j))
                    while check == 0 :
                        i, j = q.pop(0)
                        for k in range(4):
                            ni = i + idx_i[k]
                            nj = j + idx_j[k]
                            if 0<=ni<10 and 0<=nj<10 :
                                if arr[ni][nj] == 0 :
                                    if arr[i][j] + 1 != AP[ap_num][2]+2 :
                                        arr[ni][nj] = arr[i][j] +1
                                        q.append((ni,nj))
                                        AP_list[num].append((ni,nj))
                                    else :
                                        check = 1
                    for n,m in AP_list[num] :
                        arr[n][m] = 0
                    ap_num += 1

    ai,aj = 0,0
    bi,bj = 9,9
    for i in range(M+1):
        if A[i] == 1 :
            ai -= 1
        elif A[i] == 2 :
            aj += 1
        elif A[i] == 3:
            ai += 1
        elif A[i] == 4:
            aj -= 1

        if B[i] == 1 :
            bi -= 1
        elif B[i] == 2 :
            bj += 1
        elif B[i] == 3:
            bi += 1
        elif B[i] == 4:
            bj -= 1

        check_a = []
        check_b = []

        for j in range(N) :
            if (ai, aj) in AP_list[j] :
                check_a.append(j)
            if (bi, bj) in AP_list[j] :
                check_b.append(j)

        if len(check_a) == 1:
            res += AP[check_a[0]][3]

        if len(check_b) == 1:
            res += AP[check_b[0]][3]

    print(res)
