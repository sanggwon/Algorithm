for tc in range(1,int(input())+1):
    result = []
    speed = 0
    distance = 0
    for i in range(int(input())):
        RC = list(map(int,input().split()))
        if RC[0] == 1:
            speed+=RC[1]
        elif RC[0] == 2:
            speed-=RC[1]
            if speed < 0:
                speed = 0
        distance += speed
    result.append(distance)
    for res in result :
        print(f"#{tc} {res}")