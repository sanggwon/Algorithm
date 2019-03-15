for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    Othello = [[0]*N for _ in range(N)]
    Othello[(N-1)//2][(N-1)//2] = 2
    Othello[((N-1)//2)+1][((N-1)//2)+1] = 2
    Othello[((N-1)//2)+1][(N-1)//2] = 1
    Othello[(N-1)//2][((N-1)//2)+1] = 1

    idx_i = [0,1,0,-1,1,1,-1,-1]
    idx_j = [1,0,-1,0,1,-1,1,-1]

    W_cnt = 0
    B_cnt = 0

    for k in range(M):
        j,i,c = map(int,input().split())
        Othello[i-1][j-1] = c
        if c == 1 :
            r = 2
        else :
            r = 1
        for x in range(8):
            q = []
            ni = i+idx_i[x]-1
            nj = j+idx_j[x]-1
            if 0 <= ni < N and 0 <= nj < N :
                while True :
                    if N <= ni or ni < 0 or N <= nj or nj < 0:
                        q = []
                        break
                    elif Othello[ni][nj] == r :
                        q.append((ni,nj))
                        ni += idx_i[x]
                        nj += idx_j[x]
                    elif Othello[ni][nj] == 0 :
                        q = []
                        break
                    elif Othello[ni][nj] == c :
                        break
                for x_i,x_y in q :
                    Othello[x_i][x_y] = c

    for col in Othello :
        B_cnt += col.count(1)
        W_cnt += col.count(2)
    print("#{} {} {}".format(tc,B_cnt,W_cnt))