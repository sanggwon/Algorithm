# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do?contestProbId=AV5V4A46AdIDFAWu&categoryId=AV5V4A46AdIDFAWu&categoryType=CODE

def bee(lists):
    [N,M,C] = lists
    bee =[]
    bee_max1 = 0
    bee_max = []
    bee_max_list = []
    result = 0
    for i in range(N):
        bee.append(list(map(int, input().split())))
    for x in range(2):
        for i in range(N):
            for j in range(N):
                if len(bee[i][j:j+M]) == M :
                    if sum(bee[i][j:j+M]) <= C :
                        if sum(bee[i][j:j+M]) > bee_max1:
                            bee_max1 = sum(bee[i][j:j+M])
                            bee_max.append(bee[i][j:j+M])
        bee_max1 = 0
        bee_max_list.extend(bee_max[-1])
        for i in range(N):
            for j in range(N) :
                if bee[i][j:j+M] == bee_max[-1] :
                    bee[i][j:j+M] = [0]*M
    for i in bee_max_list :
        result += i*i
    return result
for i in range(1):
    print(f"#{i+1} {bee(list(map(int,input().split())))}")
