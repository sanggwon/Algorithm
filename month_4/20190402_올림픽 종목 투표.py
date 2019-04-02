for tc in range(1,int(input())+1):
    N, M = map(int,input().strip().split())
    Ai = list(map(int,input().strip().split()))
    Bi = list(map(int,input().strip().split()))

    Ai_num = [0]*N
    for i in range(M) :
        for j in range(N):
            if Bi[i] >= Ai[j] :
                Ai_num[j] += 1
                break
    print("#{} {}".format(tc,Ai_num.index(max(Ai_num))+1))
