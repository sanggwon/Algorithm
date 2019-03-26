from itertools import permutations
T = int(input())
for tc in range(1,T+1) :
    N = int(input())
    lists = [list(map(int,input().split())) for _ in range(N)]
    arr = [[] for _ in range(N)]
    min_num = 10000000
    for i in list(permutations(list(range(1,N)))) :
        arr = [0]+list(i)+[0]
        num = 0
        for j in range(N) :
            num += lists[arr[j]][arr[j+1]]
            if min_num <= num :
                break
        if min_num > num :
            min_num = num
    print("#{} {}".format(tc,min_num))