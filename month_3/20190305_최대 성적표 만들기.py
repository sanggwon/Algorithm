for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    res = 0

    for i in range(K):
        res += sorted(numbers)[::-1][i]
    print(f"#{tc} {res}")
