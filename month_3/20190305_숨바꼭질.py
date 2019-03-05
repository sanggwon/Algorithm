def bfs(x,k):
    q = []
    visited = [0]*(100001)
    q.append(x)
    visited[x] =1
    while (len(q) != 0):
        x = q.pop(0)
        if x == k :
            return visited[k] -1
        # x-1 인접
        if x-1 >= 0  and visited[x-1] == 0:
            q.append(x-1)
            visited[x-1] =visited[x] +1
        # x+1 인접
        if x+1 <= 100000 and visited[x+1] == 0 :
            q.append(x+1)
            visited[x+1] = visited[x]+1
        # 2*x인접
        if 2*x <= 100000 and visited[2*x] == 0:
            q.append(2*x)
            visited[2*x] = visited[x]+1

    return 0

print(bfs(5,17))