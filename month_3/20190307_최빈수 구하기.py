for tc in range(1,int(input())+1):
    _ = input()

    numbers = list(map(int,input().split()))

    res = [0]*101

    for i in range(101):
        res[i] = numbers.count(i)
    res.reverse()
    print("#{} {}".format(tc,100-res.index(max(res))))