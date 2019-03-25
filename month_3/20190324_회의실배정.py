N = int(input())
lists = [list(map(int,input().split())) for _ in range(N)]
lists.sort(key=lambda x:x[0])
lists.sort(key=lambda x:x[1])

end = 0
cnt = 0
for i in range(N):
    if lists[i][0] >= end :
        end = lists[i][1]
        cnt +=1
print(cnt)