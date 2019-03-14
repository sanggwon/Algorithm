lists = [list(map(int,input().split())) for _ in range(5)]

max_num = 0
who = 0
for i in range(5) :
    if max_num < sum(lists[i]) :
        max_num = sum(lists[i])
        who = i+1
print(who,max_num)