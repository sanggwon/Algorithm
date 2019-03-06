T = int(input())

for tc in range(T):
    h1, m1, h2, m2 = map(int, input().split())
    M = (m1 + m2) % 60
    H = (h1 + h2 + ((m1 + m2) // 60)) % 12
    if H == 0:
        H = 12

    print(f"#{tc+1} {H} {M}")