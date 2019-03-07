for tc in range(1,int(input())+1):
    N = int(input())
    numbers = [2,3,5,7,11]
    res = []
    for i in numbers:
        cnt = 0
        while N%i == 0:
            N /= i
            cnt +=1
        res.append(cnt)
    print("#{}".format(tc), end=" ")
    for j in res :
        print(j, end=" ")
    print()

