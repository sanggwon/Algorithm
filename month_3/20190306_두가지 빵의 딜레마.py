for tc in range(1,int(input())+1):
    A,B,C = map(int,input().split())
    if A < B :
        print("#{} {}".format(tc,C//A))
    else :
        print("#{} {}".format(tc, C//B))