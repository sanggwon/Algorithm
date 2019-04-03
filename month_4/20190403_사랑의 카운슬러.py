from itertools import combinations
T = int(input())+1
for tc in range(1,T):
    N = int(input())
    earthworm = [list(map(int,input().split())) for _ in range(N)]
    x = []
    y = []
    min_V = 1000000000000000
    for i in range(N):
        x.append(earthworm[i][0])
        y.append(earthworm[i][1])

    total_x = sum(x)
    total_y = sum(y)

    v_x = []
    v_y = []
    for n in list(combinations(x,N//2)) :
        v_x.append(2*sum(n)-total_x)
    for m in list(combinations(y,N//2)) :
        v_y.append(2*sum(m)-total_y)

    for j in range(len(v_x)):
        if min_V > v_x[j]**2+v_y[j]**2:
            min_V = v_x[j]**2+v_y[j]**2
    print("#{} {}".format(tc,min_V))
