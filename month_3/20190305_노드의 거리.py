import sys
sys.stdin = open("input5.txt","r")

# def find(check, node, E, Q ):
#     global Eixt
#     if check[0] == check[1]:
#         Eixt = 1
#     else :
#         for i in range(E):
#             if not node[i] in Q:
#                 if check[1] in node[i]:
#                     Q.append(node[i])
#                     for j in node[i]:
#                         if j != check[1]:
#                             r = find([check[0], j], node, E, Q)
#                             if Eixt == 1:
#                                 return
#                             else :
#                                 Q.pop()
# for tc in range(1,int(input())+1):
#     V,E = map(int,input().split())
#     node = [list(map(int,input().split())) for _ in range(E)]
#     check = list(map(int,input().split()))
#     Q = []
#     Eixt = 0
#     find(check, node, E, Q)
#     print("#{} {}".format(tc,len(Q)))


def bfs(s,g,v):
    q = []
    visited = [0]*(v+1) # visited 생성
    q.append(s) # 시작점 인큐
    visited[s] = 1 # 시작점 방문 표시
    while len(q) != 0 : # 큐가 비어있지 않으면
        n = q.pop(0) # 디큐
        if n == g :
            return visited[g] - 1
        for i in range(1,V+1): # 모든 노드 i에 대해
                               # n에 인접이고 미방문이면
            if adj[n][i] != 0 and visited[i] == 0 :
                q.append(i)
                visited[i] = visited[n]+1
    return 0

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for i in range(V+1)]
    for i in range(E):
        n1, n2 = map(int,input().split())
        adj[n1][n2] = 1
        adj[n2][n1] = 1 # 무방향 그래프
    S, G = map(int, input().split())

    print('#{} {}'.format(tc, bfs(S, G, V)))
