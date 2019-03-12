def dfs(i, j, string, n):
    if n == 6:
        visited.append(string)
        return
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni, nj, string*10 + grid[ni][nj], n + 1)


di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
for tc in range(1, int(input())+1):
    visited = []

    grid = [list(map(int, input().split())) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            dfs(i, j, grid[i][j], 0)
    print("#{} {}".format(tc, len(set(visited))))