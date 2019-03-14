for tc in range(1,int(input())+1):
    A, B = input().split()
    q = []
    res = []
    for i in A:
        q.append(i)
        if len(q) == len(B) :
            if q == list(B) :
                q = []
                res.append("")
            else :
                res.append(q.pop(0))
    print("#{} {}".format(tc,len(res)+len(q)))
