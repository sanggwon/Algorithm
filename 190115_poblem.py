index = [[0]*5 for i in range(5)]
count = 0
for i in range(5) :
    for j in range(5):
        count += 1
        index[i][j] = count

for x in index :
    print(x)

count = 0
num1 = 4
num2 = 5
m = 0
n = 0
p = 5
q = 4
while p != 0 :
    if m < 3 :
        for x in range(p) :
            count += 1
            index[m][n] = count
            if n < num1 :
                n += 1
        m += 1
        p -= 1
        for y in range(q) :
            count += 1
            index[m][n] = count
            if m < num1 :
                m += 1
        q -= 1
        n -= 1
    else :
        for x in range(p) :
            count += 1
            index[m][n] = count
            if 0 < n < num2 :
                if count != 23  :
                    n -= 1
        m -= 1
        p -= 1
        for y in range(q) :
            count += 1
            index[m][n] = count
            if 1 < m < num2 :
                if count != 24 :
                    m -= 1
        q -= 1
        n += 1
        num1 -= 1
        num2 -= 2
        

print(index)