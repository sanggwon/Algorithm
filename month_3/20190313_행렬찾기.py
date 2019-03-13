def find (i,j,n) :
    r_cnt = 1
    c_cnt = 1
    for c in range(1,n-i+1):
        if C[i+c][j] != 0 :
            c_cnt +=1
        else :
            break
    for r in range(1,n-j+1):
        if C[i][j+r] != 0 :
            r_cnt +=1
        else :
            break
    return [c_cnt,r_cnt]

def swap(x, i, j):
    global res
    x[i], x[j] = x[j], x[i]
    res[i], res[j] = res[j], res[i]

def bubbleSort(x):
    for size in reversed(range(len(x))):
        for i in range(size):
            if x[i] >= x[i+1]:
                swap(x, i, i+1)


for tc in range(1,int(input())+1):
    N = int(input())
    C = []
    C.append([0]*(N+1))
    for _ in range(N) :
        C.append([0]+list(map(int,input().split())))
    check = []
    res = []
    for i in range(1,N+1):
        for j in range(1,N+1):
            if C[i][j] != 0 and C[i-1][j] == 0 and C[i][j-1] == 0 :
                res.append(find(i, j, N))

    for n in res :
        check.append(n[0]*n[1])

    bubbleSort(check)

    print("#"+str(tc),len(res), end = " ")
    for m in res :
        print(m[0],m[1], end= " ")
    print()