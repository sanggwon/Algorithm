import sys
sys.stdin = open("sample_input_7.txt","r")
di = [0,1,0,-1]
dj = [1,0,-1,0]

N = int(input())
A = []
my_sum = 0
sum_list = []
for _ in range(N):
    A.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if ni>= 0 and nj >= 0 and ni < N and nj < N:
                my_sum += abs(A[i][j]-A[ni][nj])
        sum_list.append(my_sum)
        my_sum = 0
print(sum(sum_list))