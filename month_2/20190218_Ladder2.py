import sys
sys.stdin = open("sample_input_6.txt","r")

for _ in range(10):
    T = input()
    lists = []
    for _ in range(100):
        lists.append([0]+list(map(int,input().split()))+[0])

    first_num = []
    for i in range(101):
        if lists[0][i] == 1 :
            first_num.append(i)
    count = 0
    count_list = []
    for j in first_num :
        for z in range(1,99):
            count +=1
            if lists[z][j-1] == 1 :
                while lists[z][j-1] == 1:
                    j -= 1
                    count +=1
                    if lists[z+1][j] == 1:
                        break
            elif lists[z][j+1] == 1 :
                while lists[z][j+1] == 1:
                    j += 1
                    count +=1
                    if lists[z+1][j] == 1:
                        break
        count_list.append(count)
        count = 0
    min_count = min(count_list)
    result = {count:num for count,num in zip(count_list, first_num)}


    print(f"#{T} {result[min_count]-1}")