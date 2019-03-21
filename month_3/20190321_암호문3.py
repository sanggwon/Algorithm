import sys
sys.stdin = open("input.txt", "r")
for tc in range(1,11):
    N = int(input()) # 원문 숫자의 갯수
    original = input().split()
    M = int(input()) # 명령어의 갯수
    command = input().split()
    next = 0
    for i in range(M) :
        if command[next] == "I":
            next += 1
            x = int(command[next])
            next += 1
            y = int(command[next])
            next += 1
            for j in range(y):
                original.insert(x,command[next])
                next += 1
                x += 1 # 위치도 증가
        elif command[next] == "A":
            next += 1
            y = int(command[next])
            next += 1
            for j in range(y):
                original.append(command[next])
                next += 1
        elif command[next] == "D" :
            next += 1
            x = int(command[next])
            next += 1
            y = int(command[next])
            next += 1
            for j in range(y):
                original.pop(x) # 위치 그대로
    print("#{} {}".format(tc," ".join(original[0:10])))
