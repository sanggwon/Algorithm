import sys
sys.stdin = open("input.txt","r")

for _ in range(10):
    T = input()
    lists = []
    for i in range(100):
        lists.append([0]+list(map(int,input().split()))+[0])
        
    last_num = lists[99].index(2)
    
    for j in range(99):
        if lists[98-j][last_num-1] == 1 :
            while lists[98-j][last_num-1] == 1:
                last_num -= 1
                if lists[97-j][last_num] == 1:
                    break
        elif lists[98-j][last_num+1] == 1 :
            while lists[98-j][last_num+1] == 1:
                last_num += 1
                if lists[97-j][last_num] == 1:
                    break
    print(f"#{T} {last_num-1}")
    
