for tc in range(1,int(input())+1):
    n = int(input())
    res = set([])
    cony_n = n
    cnt = 1
    while len(list(res)) != 10 :
        if cony_n//10 != 0:
            res.add(cony_n%10)
            cony_n = cony_n//10
        else :
            res.add(cony_n % 10)
            if len(list(res)) == 10 :
                break
            cnt += 1
            cony_n = n*cnt
    print("#{} {}".format(tc,n*cnt))
