import sys
sys.stdin = open("sample_input_21.txt","r")

for tc in range(1,int(input())+1):
    def find(N,M) :
        find = ""
        for i in range(len(M)-len(N)+1):
            for j in range(len(N)):
                find += M[i+j]
            if N == find :
                return 1
            find = ""
            
        return 0
    
    print(f"#{tc} {find(input(),input())}")