import sys
sys.stdin = open("sample_input_38.txt","r")

for tc in range(1,int(input())+1):
    N,K = map(int,input().split())
    record = ["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]
    records = []
    for r in record:
        for x in range(N//10):
            records.append(r)
    student = [list(map(int,input().split())) for _ in range(N)]
    find = []
    for i in range(N):
        find.append(student[i][0]*35/100 + student[i][1]*45/100 + student[i][2]*20/100)
    check = find[:]
    check.sort()
    for j in range(N) :
        if find[K-1] == check[N-j-1]:
            print(f"#{tc} {records[j]}")

    