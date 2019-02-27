def patch(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    return patch(N - 10) + 2 * patch(N - 20)


T = int(input())
for i in range(1, T + 1):
    N = int(input())
    print(f"#{i} {patch(N)}")