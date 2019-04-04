T = int(input().strip())+1
for tc in range(1,T):
    a, b = map(int,input().strip().split())
    s = 1
    e = 3
    m = ()
    t = ()
    for i in range(141) :
        s = s+i
        if i != 0 :
            e = s+i
            if not len(m) :
                if s<=a<=e :
                    m = (i,a-s)
            if not len(t) :
                if s<=b<=e :
                    t = (i,b-s)
    print(m,t)

    print(abs(m[1]-t[1])-abs(m[0]-t[0])+abs(m[0]-t[0]))

