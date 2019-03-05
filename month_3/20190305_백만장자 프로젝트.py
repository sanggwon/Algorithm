for tc in range(1,int(input())+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    numbers.reverse()
    res = 0
    count_number = numbers[0]
    for i in range(N) :
        if count_number < numbers[i]:
            count_number = numbers[i]
        res += (count_number-numbers[i])
    print("#{} {}".format(tc,res))