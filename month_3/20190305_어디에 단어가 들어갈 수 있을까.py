for tc in range(1,int(input())+1):
    N, K = map(int,input().split())
    res = 0
    string = [list(map(int,input().split())) for _ in range(N)]
    check_r = 0
    check_c = 0
    for i in range(N):
        for j in range(N):
            if string[i][j] == 1:
                check_r +=1

            if string[i][j] == 0:
                if check_r == K :
                    res +=1
                check_r = 0

            if string[j][i] == 1 :
                check_c +=1

            if string[j][i] == 0:
                if check_c == K :
                    res+=1
                check_c = 0
        if check_r == K:
            res += 1
        if check_c == K:
            res += 1
        check_r = 0
        check_c = 0
    print("#{} {}".format(tc,res))
