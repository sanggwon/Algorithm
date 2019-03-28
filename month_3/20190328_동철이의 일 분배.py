def dfs(n,k,s):
    global maxV
    if n == k :
        if maxV < s :
            maxV = s
    elif s <= maxV :
        return
    else :
        for i in range(k):
            if u[i] == 0 : # i번 일을 맡은 사람이 아직 없으면
                u[i] = 1 # i번 일이 배정되었음을 기록
                dfs(n+1,k,s*numbers[n][i]) # n번 사람이 i번 일을 하는데 걸리는 시간
                u[i] = 0 # i번 일을 다른 사람에게 배정할 수 있도록 풀어줌

for tc in range(1,int(input())+1):
    N = int(input())
    numbers = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            numbers[i][j] *= 0.01
    maxV = 0
    u = [0]*N # 배정된 일은 1로 표시
    dfs(0,N,1)
    print("#" + str(tc), end=" ")
    print("%.6f" % (maxV*100))