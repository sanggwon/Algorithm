for tc in range(1, int(input())+1):
    N,M = map(int,input().split())
    numbers = input().split()
    for i in range(M):
        m = numbers.pop(0)
        numbers.append(m)
    print("#{} {}".format(numbers[0]))