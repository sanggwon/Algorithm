for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    pizza = list(map(int,input().split()))
    d = list(range(1,M+1))
    h = []
    ih = []
    for i in range(N):
        h.append(pizza.pop(0))
        ih.append(d.pop(0))

    while len(ih) != 0 :
        p = h.pop(0)//2
        q = ih.pop(0)
        if p == 0:
            if len(pizza) != 0 :
                h.append(pizza.pop(0))
                ih.append(d.pop(0))
        else :
            h.append(p)
            ih.append(q)

    print("#{} {}".format(tc,q))
