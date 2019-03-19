T = int(input().strip())

for tc in range(1,T+1):
    N = int(input().strip())
    A = input().strip()
    B = input().strip()
    lcs = [[0 for i in range(N + 1)] for j in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if A[i - 1] == B[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])
    res = lcs[N][N]/N*100
    print("#"+str(tc), '%.2f' % res)

