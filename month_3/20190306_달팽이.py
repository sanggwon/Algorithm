for tc in range(1,int(input())+1) :
    N = int(input())
    list_data = [[0]*N for i in range(N)]
    write_count = N
    num = 1
    idx_i = 0
    idx_j = -1
    sw = 1

    while write_count != 0:
        for i in range(write_count):
            idx_j += sw
            list_data[idx_i][idx_j] = num
            num += 1

        write_count -= 1

        for i in range(write_count):
            idx_i += sw
            list_data[idx_i][idx_j] = num
            num += 1

        sw = -sw
    print("#{}".format(tc))
    for res in list_data:
        print(" ".join(map(str,res)))