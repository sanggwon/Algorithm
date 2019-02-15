import sys
sys.stdin = open("sample_input_4.txt","r")
T = int(input())
for i in range(T):
    [N,M] = list(map(int,input().split()))
    arrangement = list(map(int,input().split()))

    num_max = 0
    num_min = sum(arrangement)
    count = M
    for j in range(N-M+1):

        if num_max < sum(arrangement[j:count]) :
            num_max = sum(arrangement[j:count])  
        if num_min > sum(arrangement[j:count]):
            num_min = sum(arrangement[j:count])
        count +=1    
 
    print(f"#{i+1} {num_max-num_min}")
        

