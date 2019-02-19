import sys
sys.stdin = open("sample_input_14.txt","r")

T = int(input())

for tc in range(T):
    nasa_num = int(input())
    N = list(map(int,input().split()))
    nasa_x = [N[i*2] for i in range(nasa_num)]
    nasa_y = [N[(i*2)+1] for i in range(nasa_num)]
    start_x = list(set(nasa_x)-set(nasa_y))
    start_y = list(set(nasa_y)-set(nasa_x))

    index_1 = nasa_x.index(start_x[0])

    nasa_y[index_1], nasa_y[0] = nasa_y[0], nasa_y[index_1]
    nasa_x[index_1], nasa_x[0] = nasa_x[0], nasa_x[index_1]

    index_2 = nasa_y.index(start_y[0])

    nasa_y[index_2], nasa_y[-1] = nasa_y[-1], nasa_y[index_2]
    nasa_x[index_2], nasa_x[-1] = nasa_x[-1], nasa_x[index_2]
    
    for j in range(nasa_num-1):
        if not nasa_y[j] == nasa_x[j+1] :
            index_3 = nasa_x.index(nasa_y[j])
            nasa_x[index_3], nasa_x[j+1] = nasa_x[j+1],nasa_x[index_3]
            nasa_y[index_3], nasa_y[j+1] = nasa_y[j+1],nasa_y[index_3]   
    result = []
    for n in list(zip(nasa_x,nasa_y)) :
        result.extend(n)
    print(f"#{tc+1} {' '.join(map(str,result))}")

    
    
