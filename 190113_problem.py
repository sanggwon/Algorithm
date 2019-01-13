col, row = map(int,input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))
    
for m in range(col):
    for n in range(row):
        count = 0
        if(matrix[m][n] == "*"):
            continue
        elif(matrix[m][n] == "."):
            for a in range(-1,2):
                for b in range(-1,2):
                    if(m+a < 0) or (n+b < 0) or (m+a > col-1) or (n+b > row-1):
                        continue
                    if(matrix[m+a][n+b] == "*"):
                        count += 1
        matrix[m][n] = str(count)

print("".join(matrix[0]))
print("".join(matrix[1]))
print("".join(matrix[2]))