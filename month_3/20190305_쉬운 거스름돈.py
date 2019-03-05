for tc in range(1, int(input()) + 1):
    N= int(input())
    money = [50000,10000,5000,1000,500,100,50,10]
    res = []
    for i in range(8):
        res.append(N//money[i])
        N = N%money[i]
    print("#{}\n{}".format(tc," ".join(map(str,res))))