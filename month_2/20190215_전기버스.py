import sys
sys.stdin = open("sample_input_2.txt","r")

for i in range(int(input())):
    def bus(lists) :
        [K,N,M] = lists
        bus_charge = list(map(int,input().split()))

        bus = list(map(int,range(N+1)))
        for j in bus:
            if not j in bus_charge :
                bus[j] = 0


        oil = K
        back = 1
        count = 0
        for j in range(1,len(bus)) :
            oil-=1
            if oil == 0:
                if bus[j] != 0:
                    oil = K
                    count+=1
                else :
                    while back < K and j != N:
                        if oil != 0:
                            break    
                        elif bus[j-back] !=0:
                            oil = K-back
                            count+=1
                            back = 0
                        else :
                            back +=1
                            if back == K:
                                return 0
                        
        return count

        

            
    print(f"#{i+1} {bus(list(map(int,input().split())))}")



