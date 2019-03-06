for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A_copy = A[:]
    B = list(map(int, input().split()))
    B_copy = B[:]
    res = -9999
    a = 0
    for i in range(abs(N-M)+1):
        if N < M :
            A = ([0]*i)+A+([0]*(abs(N-M)-i))
            for j in range(M):
                a += B[j]*A[j]
            if res <= a:
                res = a
            a = 0
            A = A_copy
        else :
            B = ([0]*i)+B+([0]*(abs(N-M)-i))
            for j in range(N):
                a += B[j]*A[j]
            if res <= a:
                res = a
            a = 0
            B = B_copy
    print ("#{} {}".format(tc,res))
