def card(numbers):
    [N, K] = numbers
    number_list = list(range(1,N+1))
    num_len = len(number_list)
    if K != 0 :
        while num_len != 1:
            if num_len/K >= 1:
                number_list.extend(number_list[:K])
                del number_list[:K+1]
                print("1",number_list)
            else :
                M = K%num_len
                number_list.extend(number_list[:M])
                del number_list[:M+1]
                print("2",number_list)
            num_len -= 1
    return number_list[-1]


for i in range(int(input())):
    print("#"+str((i+1)),card(list(map(int,input().split()))))





for i in range(int(input())):
    n,k=map(int,input().split())
    s = list(range(1,n+1))
    k +=1
    cursor = 0
    while len(s)>1:
        cursor = (cursor+k-1)%len(s)
        s.pop(cursor)
    print ("#"+str(i+1),s[0])