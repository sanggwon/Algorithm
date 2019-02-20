for tc in range(int(input())):
    N = input()
    print(f"#{tc+1}", end=" ")
    if N == N[::-1]:
        print(1)
    else :
        print(0)