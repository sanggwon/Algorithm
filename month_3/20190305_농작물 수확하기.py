for tc in range(1,int(input())+1):
    N = int(input())
    farm = [list(input()) for _ in range(N)]
    T = N//2
    res = 0
    for i in range(N):
        if N//2 >= i :
            if T != 0 :
                res += sum(map(int,farm[i][T:-T]))
                T-=1
            else :
                res += sum(map(int, farm[i][:]))
        else :
            T+=1
            res += sum(map(int, farm[i][T:-T]))
    print("#{} {}".format(tc,res))
