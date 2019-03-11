for tc in range(1,int(input())+1):
    N,M,K = map(int,input().split())
    lists = list(map(int,input().split()))
    for i in range(M):
        A = list(map(int,input().split()))
        lists.insert(A[0],A[1])
    print("#{} {}".format(tc,lists[K]))