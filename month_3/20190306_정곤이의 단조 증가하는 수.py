def check(N, number):
    start_num = number[0]
    for j in range(1,len(number)):
        if int(start_num) > int(number[j]) :
            return -1
        start_num = int(number[j])
    return int(number)

for tc in range(1,int(input())+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    max_num = -1
    cnt = 0
    for i in range(N-1):
        cnt +=1
        for j in range(cnt,N):
            number = str(numbers[i]*numbers[j])
            if len(number) != 1:
                r = check(N,number)
                if max_num <= r :
                    max_num = r
    print("#{} {}".format(tc,max_num))