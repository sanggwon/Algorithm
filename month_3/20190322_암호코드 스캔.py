import sys
sys.stdin = open("input.txt","r")
def f(m) :
    global decond, oct_code
    first_cnt = 0
    second_cnt = 0
    third_cnt = 0
    start = 0
    number = []
    for i in format(int(m,16),"b")[::-1] :
        if i != "0" :
            start = 1
        if start == 1 :
            if i == "0" and first_cnt != 0 and second_cnt !=0 and third_cnt != 0 :
                if min(first_cnt,second_cnt,third_cnt) != 1 :
                    min_num = min(first_cnt,second_cnt,third_cnt)
                    first_cnt //= min_num
                    second_cnt //= min_num
                    third_cnt //= min_num
                if [first_cnt, second_cnt, third_cnt] in decond:
                    number.append(decond.index([first_cnt, second_cnt, third_cnt]))
                    first_cnt = 0
                    second_cnt = 0
                    third_cnt = 0

            elif i == "1" and first_cnt == 0 and second_cnt == 0:
                third_cnt += 1
            elif i == "0" and first_cnt == 0 and third_cnt != 0:
                second_cnt += 1
            elif i == "1" and second_cnt != 0 and third_cnt != 0:
                first_cnt += 1

            if len(number) == 8 :
                numbers.add("".join(list(map(str, list(reversed(number))))))
                number = []
    if min(first_cnt, second_cnt, third_cnt) != 1:
        min_num = min(first_cnt, second_cnt, third_cnt)
        first_cnt //= min_num
        second_cnt //= min_num
        third_cnt //= min_num
    if [first_cnt, second_cnt, third_cnt] in decond:
        number.append(decond.index([first_cnt, second_cnt, third_cnt]))

    if len(number) == 8:
        numbers.add("".join(list(map(str,list(reversed(number))))))



decond = [[2,1,1],[2,2,1],[1,2,2],[4,1,1],[1,3,2],[2,3,1],[1,1,4],[3,1,2],[2,1,3],[1,1,2]]

box = []
for tc in range(1,int(input())+1) :
    N, M = map(int,input().split())
    code = [input().strip() for _ in range(N)]
    numbers = set()
    res = 0
    search = []
    for i in range(N):
        if code[i].count("0") != M  :
            if not code[i] in search :
                search.append(code[i])

    for j in search :
        f(j)
    check = ""
    for r in numbers :
        if (sum(list(map(int,r[::2])))*3 + sum(list(map(int,r[1:7:2]))) + int(r[-1])) % 10 == 0:
            res += sum(list(map(int,r)))
        else :
            res += 0
    box.append("#{} {}".format(tc,res))

for i in range(len(box)):
    print(box[i])
