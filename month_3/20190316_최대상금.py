# if __name__ == "__main__":
T = int(input())
for t in range(1, T + 1):
    NUM, ITER = input().split()
    ITER = int(ITER)
    now = set()
    now.add(NUM)
    after = set()
    for i in range(ITER):
        while now:
            s = list(str(now.pop()))
            for i in range(len(NUM)):
                for j in range(i+1,len(NUM)):
                    if s[i] <= s[j] :
                        s[i], s[j] = s[j], s[i]
                        after.add(int("".join(s)))
                        s[i], s[j] = s[j], s[i]
        now, after = after, now
    print("#", t, ' ', max(map(int, now)), sep='')