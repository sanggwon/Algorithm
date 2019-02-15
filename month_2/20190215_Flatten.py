import sys
sys.stdin = open("sample_input_5.txt","r")

for i in range(10):
    def planarization(dump):

        planarization = list(map(int,input().split()))
        while dump != 0 :
            max_g = max(planarization)-1
            min_g = min(planarization)+1
            planarization.remove(max(planarization))
            planarization.remove(min(planarization))
            planarization.append(max_g)
            planarization.append(min_g)
            dump -= 1
            if max_g == min_g:
                return 0
        return max(planarization)-min(planarization)

    print(f"#{i+1} {planarization(int(input()))}")