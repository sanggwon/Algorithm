for tc in range(1,int(input())+1):
    N,M,K = map(int,input().split())

    lists = list(map(int,input().split()))
    start_num = 0
    for i in range(1,K+1):
        start_num += M
        if start_num >= len(lists) :
            start_num %= len(lists)
        if start_num == 0:
            lists.append(lists[start_num-1]+lists[start_num])
            start_num-=1
        else :
            lists.insert(start_num,lists[start_num-1]+lists[start_num])

    print("#{} {}".format(tc,' '.join(map(str,list(reversed(lists))[:10]))))