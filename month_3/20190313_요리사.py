L = int(input().strip())
N = int(input().strip())
cake = [0]*(L+1)
num = 0
res = [0,0,0,0]
person = [list(map(int,input().split())) for _ in range(N)]
for i in person :
    num += 1
    if res[2] < (i[1]-i[0]):
        res[2] = (i[1]-i[0])
        res[0] = person.index(i)+1
    for j in range(i[0],i[1]+1) :
        if cake[j] == 0 :
            cake[j] = num

for n in range(1,L+1) :
    a = cake.count(n)
    if a == 0 :
        continue
    elif res[3] < a :
        res[3] = a
        res[1] = n

for r in range(2) :
    print(res[r])
