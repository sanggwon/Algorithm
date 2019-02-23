import sys
sys.stdin = open("input_2.txt", "r")

for tc in range(10):
    T = input()
    I = [input() for _ in range(100)]
    max_count = 1
    for i in range(100):
        num = 0
        for j in range(98):
            length = 100-num
            start = 1
            for n in range(length-1,start,-1):
                r_count = 0
                c_count = 0
                for m in range(length//2):
                    if I[i][j+m] == I[i][j+n-m] :
                        r_count += 1
                    else :
                        r_count = 0
                        break
                for m in range(length//2):
                    if I[j+m][i] == I[j+n-m][i] :
                        c_count +=1
                    else :
                        c_count =0
                        break
                if length%2 :
                    r_count = r_count*2+1
                    c_count = c_count*2+1
                else :
                    r_count = r_count*2
                    c_count = c_count*2

                if max_count < r_count :
                    max_count = r_count
                if max_count < c_count:
                    max_count = c_count
                length -=1
                start +=1
            num +=1
    print(f"#{T} {max_count}")
                