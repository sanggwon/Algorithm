for tc in range(1,int(input())+1):
    N = int(input())
    bus = [list(map(int,input().split())) for _ in range(N)]
    P = int(input())
    station = [list(map(int,input().split())) for _ in range(P)]
    station_index = []
    for _ in range(P) :
        station_index.append(0)
    for i in range(N):
        for j in range(bus[i][0],bus[i][1]+1):
            for n in range(P) :
                if station[n] == [j] :
                    station_index[n] +=1
    print("#{} {}".format(tc," ".join(list(map(str,station_index)))))