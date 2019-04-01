def make_set(x):
    p[x] = x

def find_set(x):
    while p[x] != x:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    p = [0]*(V+1)
    arr = [list(map(int, input().split())) for _ in range(E)]
    arr.sort(key= lambda x:x[2])
    A = []
    for i in range(V+1):
        make_set(i)

    for j in arr :
        if find_set(j[0]) != find_set(j[1]) :
            A.append(j[2])
            union(j[0],j[1])
    print("#{} {}".format(tc,sum(A)))
