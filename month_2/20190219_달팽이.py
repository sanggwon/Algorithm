import sys
sys.stdin = open("sample_input_9.txt","r",)

N = []
index = 0
write_count = 5
idx_i = 0
idx_j = -1
sw = 1
for _ in range(5):
    N.extend(list(map(int,input().split())))
N.sort()

M = [[0]*5 for i in range(5)]

while write_count > 0:
    for i in range(write_count):
        idx_j += sw
        M[idx_i][idx_j] = N[index]
        index +=1
    write_count -= 1

    for j in range(write_count):
        idx_i += sw
        M[idx_i][idx_j] = N[index]
        index +=1
    
    sw = -sw

print(M)


