for tc in range(1,int(input())+1):
    N = int(input())
    C = [list(input().split()) for _ in range(N)]
    res = []
    for i in range(N):
        res.extend(C[i][0]*int(C[i][1]))
    print("#{}".format(tc), end="")
    for j in range(len(res)) :
        if j % 10 == 0 :
            print("\n", end="")
        print(res[j], end="")
    print()

