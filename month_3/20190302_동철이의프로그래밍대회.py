import sys 
sys.stdin = open("input.txt","r")

for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    lists = [list(map(int,input().split())) for _ in range(N)]
    count = 0
    people = 1
    for i in range(N):
        if count < lists[i].count(1):
            count = lists[i].count(1)
        elif count == lists[i].count(1):
            people += 1
    if count == 0 :
        people = 0 
    print(f"#{tc} {people} {count}")
		