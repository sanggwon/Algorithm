import sys
sys.stdin = open('input.txt','r')
T = int(input())+1
for tc in range(1,T):
    N,M,K = map(int,input().split())
    arr = [[0]*(M+K+2) for _ in range(K//2+1)]+[[0]*(K//2+1)+list(map(int,input().split())) + [0]*(K//2+1) for _ in range(N)] + [[0]*(M+K+2) for _ in range(K//2+1)]

    for i in range(K//2+1+N+K//2):
        for j in range(M+K+1):
            if arr[i][j] :
                arr[i][j] = [arr[i][j],arr[i][j],0]

    ind_i = [0,-1,0,1]
    ind_j = [1,0,-1,0]

    for _ in range(K):
        for i in range(K//2+1+N+K//2):
            for j in range(M+K+1):
                if arr[i][j] and arr[i][j][1] != -arr[i][j][0]:
                    # 값이 존재하고 죽은상태가 아니면
                    if arr[i][j][1] == 0 :
                        # 활성화이면
                        for k in range(4):
                            # 상하좌우 번식
                            ni = i + ind_i[k]
                            nj = j + ind_j[k]
                            if 0<=ni<(K//2+1+N+K//2) and 0<=nj<(M+K+1):
                                # 영역내에 있으면
                                if arr[ni][nj] == 0 :
                                    # 값이 존재하지 않는 곳에
                                    arr[ni][nj] = [arr[i][j][0],arr[i][j][0],1]
                                    # 생성
                                else :
                                    # 값이 존재하면
                                    if arr[ni][nj][2] == 1 :
                                        # 방금 생성된 애가 맞다면
                                        if arr[ni][nj][0] < arr[i][j][0]:
                                            arr[ni][nj] = [arr[i][j][0],arr[i][j][0],1]
                        arr[i][j][1] -= 1
                        # 카운트
                    else :
                        # 비활성화이고
                        if arr[i][j][2] == 0 :
                            # 방금 생성하지 않았으면
                            arr[i][j][1] -= 1
                            # 카운트

        for i in range(K // 2 + 1 + N + K // 2):
            for j in range(M + K + 1):
                if arr[i][j]:
                    # 값이 존재하고
                    if arr[i][j][2] == 1:
                        # 방금 생성되었으면
                        arr[i][j][2] = 0

    count = 0
    for i in range(K // 2 + 1 + N + K // 2):
        for j in range(M + K + 1):
            if arr[i][j] :
                if arr[i][j][1] != -arr[i][j][0] :
                    count += 1

    print("#{} {}".format(tc,count))


