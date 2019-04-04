T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    scores = [0]
    visitied = [0]*(sum(arr)+1)

    for i in range(N):
        for j in range(len(scores)):
            temp = arr[i] + scores[j]
            if visitied[temp] == 0 :
                scores.append(temp)
                visitied[temp]= 1

    print("#{} {}".format(t, len(scores)))