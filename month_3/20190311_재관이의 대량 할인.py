for tc in range(1,int(input())+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    numbers.sort()
    numbers.reverse()
    res = sum(numbers)
    if N%3 == 0:
        for i in numbers[2::3]:
            res -= i
    else :
        for i in numbers[2:N-(N%3):3]:
            res -= i

    print("#{} {}".format(tc, res))