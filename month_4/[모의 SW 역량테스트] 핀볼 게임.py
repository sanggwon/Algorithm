id_i = [0,1,0,-1]
id_j = [1,0,-1,0]

T = int(input().strip())+1
for tc in range(1,T):
    N = int(input().strip())
    Pinball = [list(map(int,input().strip().split())) for _ in range(N)]
    wormhole= [[] for _ in range(5)]
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            if Pinball[i][j] > 5 :
                wormhole[Pinball[i][j]-6].append((i,j))

    for i in range(N):
        for j in range(N):
            if Pinball[i][j] == 0:
                for n in range(4):
                    ni = i+id_i[n]
                    nj = j+id_j[n]
                    cnt = 0
                    while True :
                        if 0<=ni<N and 0<=nj<N:
                            if Pinball[ni][nj] == -1 or (ni == i and nj == j) :
                                break
                            if Pinball[ni][nj] > 5 :
                                for wi,wj in wormhole[Pinball[ni][nj]-6] :
                                    if wi == ni and wj == nj :
                                        if wormhole[Pinball[ni][nj]-6].index((wi,wj)) == 0:
                                            ni, nj = wormhole[Pinball[ni][nj]-6][1]
                                        else :
                                            ni, nj = wormhole[Pinball[ni][nj]-6][0]
                                        break

                        if n == 0:
                            if nj == N :
                                n = 2
                                cnt += 1
                            elif Pinball[ni][nj] == 1:
                                n = 2
                                cnt += 1
                            elif Pinball[ni][nj] == 2:
                                n = 2
                                cnt += 1
                            elif Pinball[ni][nj] == 3:
                                n = 1
                                cnt += 1
                            elif Pinball[ni][nj] == 4:
                                n = 3
                                cnt += 1
                            elif Pinball[ni][nj] == 5:
                                n = 2
                                cnt += 1
                            ni += id_i[n]
                            nj += id_j[n]

                        elif n == 1:
                            if ni == N :
                                n = 3
                                cnt += 1
                            elif Pinball[ni][nj] == 1:
                                n = 0
                                cnt += 1
                            elif Pinball[ni][nj] == 2:
                                n = 3
                                cnt += 1
                            elif Pinball[ni][nj] == 3:
                                n = 3
                                cnt += 1
                            elif Pinball[ni][nj] == 4:
                                n = 2
                                cnt += 1
                            elif Pinball[ni][nj] == 5:
                                n = 3
                                cnt += 1
                            ni += id_i[n]
                            nj += id_j[n]

                        elif n == 2:
                            if nj < 0:
                                n = 0
                                cnt += 1
                            elif Pinball[ni][nj] == 1:
                                n = 3
                                cnt += 1
                            elif Pinball[ni][nj] == 2:
                                n = 1
                                cnt += 1
                            elif Pinball[ni][nj] == 3:
                                n = 0
                                cnt += 1
                            elif Pinball[ni][nj] == 4:
                                n = 0
                                cnt += 1
                            elif Pinball[ni][nj] == 5:
                                n = 0
                                cnt += 1
                            ni += id_i[n]
                            nj += id_j[n]

                        elif n == 3:
                            if ni < 0:
                                n = 1
                                cnt += 1
                            elif Pinball[ni][nj] == 1:
                                n = 1
                                cnt += 1
                            elif Pinball[ni][nj] == 2:
                                n = 0
                                cnt += 1
                            elif Pinball[ni][nj] == 3:
                                n = 2
                                cnt += 1
                            elif Pinball[ni][nj] == 4:
                                n = 1
                                cnt += 1
                            elif Pinball[ni][nj] == 5:
                                n = 1
                                cnt += 1
                            ni += id_i[n]
                            nj += id_j[n]
                    if max_cnt < cnt :
                        max_cnt = cnt
    print("#{} {}".format(tc,max_cnt))