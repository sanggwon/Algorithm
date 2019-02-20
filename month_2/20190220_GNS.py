import sys
sys.stdin = open("sample_input_18.txt","r")

number_list = [["ZRO"], ["ONE"], ["TWO"], ["THR"], ["FOR"], ["FIV"], ["SIX"], ["SVN"], ["EGT"], ["NIN"]]
for _ in range(int(input())):
    tc, M = input().split()
    number = input().split()
    print("\n"+tc)
    for i in range(10):
        print(" ".join(number_list[i]*number.count(number_list[i][0])), end=" ")

    
