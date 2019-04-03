T = int(input())+1
for tc in range(1,T):
    N,K = map(int,input().strip().split())
    numbers = input().strip()
    numbers_copy = numbers[:]
    side = N//4
    res = set()
    numbers = numbers[1:] + numbers[:1]
    for i in range(N // 4):
        res.add(numbers[i:i + side])
    while numbers != numbers_copy:
        numbers = numbers[1:]+numbers[:1]
        for i in range(N//4):
            res.add(numbers[i:i+side])
    print("#{} {}".format(tc,int("0x"+list(reversed(sorted(list(res))))[K-1],16)))

