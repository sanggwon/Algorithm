def up(A) :
    global N,res
    num = 0
    for i in range(N):
        check = []
        change = 0
        for j in range(N):
            if A[j][i] != 0 :
                if len(check):
                    if check[-1] == A[j][i] and change == 0:
                        check.pop()
                        check.append(A[j][i]*2)
                        change = 1
                    else :
                        check.append(A[j][i])
                        change = 0
                else :
                    check.append(A[j][i])
        if len(check) != N :
            check = check + ([0]*(N-len(check)))
        for n in range(N) :
            res[n][num] = check[n]
        num +=1


def down(A) :
    global N,res
    num = 0
    for i in range(N):
        check = []
        change = 0
        for j in reversed(range(N)):
            if A[j][i] != 0 :
                if len(check):
                    if check[-1] == A[j][i] and change == 0:
                        check.pop()
                        check.append(A[j][i]*2)
                        change = 1
                    else :
                        check.append(A[j][i])
                        change = 0
                else :
                    check.append(A[j][i])
        if len(check) != N :
            check = list(reversed(check + ([0] * (N - len(check)))))
        for n in reversed(range(N)) :
            res[n][num] = check[n]
        num +=1


def left(A) :
    global N,res
    num = 0
    for i in range(N):
        check = []
        change = 0
        for j in range(N):
            if A[i][j] != 0 :
                if len(check):
                    if check[-1] == A[i][j] and change == 0:
                        check.pop()
                        check.append(A[i][j]*2)
                        change = 1
                    else :
                        check.append(A[i][j])
                        change = 0
                else :
                    check.append(A[i][j])
        if len(check) != N :
            check = check + ([0]*(N-len(check)))
        for n in range(N) :
            res[num][n] = check[n]
        num +=1

def right(A) :
    global N,res
    num = 0
    for i in range(N):
        check = []
        change = 0
        for j in reversed(range(N)):
            if A[i][j] != 0 :
                if len(check):
                    if check[-1] == A[i][j] and change == 0:
                        check.pop()
                        check.append(A[i][j]*2)
                        change = 1
                    else :
                        check.append(A[i][j])
                        change = 0
                else :
                    check.append(A[i][j])
        if len(check) != N :
            check = list(reversed(check + ([0] * (N - len(check)))))
        for n in reversed(range(N)) :
            res[num][n] = check[n]
        num +=1


for tc in range(1,int(input())+1):
    N, S = input().split()
    N = int(N)
    lists = [list(map(int,input().split())) for _ in range(N)]
    res = [[0]*N for _ in range(N)]
    if S == "left" :
        left(lists)
    elif S == "right" :
        right(lists)
    elif S == "up" :
        up(lists)
    elif S == "down" :
        down(lists)
    print("#{}".format(tc))
    for i in res:
        print(" ".join(list(map(str,i))))