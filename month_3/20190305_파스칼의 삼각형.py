for tc in range(1,int(input())+1):
    N = int(input())
    res =[]
    for _ in range(N):
        res.append([])
    for i in range(N):
        if i == 0:
            res[i] = [1]
        elif i == 1:
            res[i] = [1,1]
        else:
            res[i].append(1)
            for j in range(len(res[i-1])-1):
                res[i].append(res[i-1][j]+res[i-1][j+1])
            res[i].append(1)
    print("#{}".format(tc))
    for j in res :
        print(" ".join(map(str,j)))