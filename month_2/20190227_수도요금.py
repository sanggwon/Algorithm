import sys 
sys.stdin = open("sample_input_37.txt","r")

for tc in range(1,int(input())+1):
    P,Q,R,S,W = map(int,input().split())
    
    A = P*W
    if W-R > 0:   
        B = Q+(W-R)*S
    else :
        B = Q
    
    print(f"#{tc} {min(A,B)}")