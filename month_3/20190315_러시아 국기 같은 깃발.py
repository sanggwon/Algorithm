for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    flag = [input() for _ in range(N)]
    start = 0
    res = []
    for i in range(N-2):
        start += 1
        last = start-1
        B_cnt = 0
        for j in range(start,N-1):
            W_cnt = M - flag[0].count("W")
            R_cnt = M - flag[-1].count("R")
            B_cnt += M - flag[j].count("B")
            last += 1
            for k in range(1,start) :
                W_cnt += M - flag[k].count("W")
            for m in range(N-2,last,-1) :
                R_cnt += M - flag[m].count("R")
            res.append(W_cnt+R_cnt+B_cnt)
    print("#{} {}".format(tc,min(res)))

