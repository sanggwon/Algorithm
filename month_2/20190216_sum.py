for i in range(10):
    T = input()
 
 
    my_list = []
    list_c = []
    list_r = []
    my_sum_c = 0
    my_sum_x1 = 0
    my_sum_x2 = 0
    for i in range(100):
        my_list.append(list(map(int,input().split())))
 
    for j in range(100) :
        list_r.append(sum(my_list[j]))
        my_sum_x1 += my_list[j][j]
        my_sum_x2 += my_list[99-j][j]
 
        for z in range(100) :
            my_sum_c += my_list[z][j]  
        list_c.append(my_sum_c)
        my_sum_c=0
 
    print(f"#{T} {max([max(list_r),max(list_c),my_sum_x1,my_sum_x2])}")