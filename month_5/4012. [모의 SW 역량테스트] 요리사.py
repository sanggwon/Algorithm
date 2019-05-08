import sys
from itertools import combinations
sys.stdin = open('input.txt','r')

T = int(input())+1
for tc in range(1,T):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    foods1 = list(combinations(list(range(N)),int(N/2)))

    min_num = 99999
    for food1 in foods1 :
        food1_list = list(combinations(food1,2))

        food1_num = 0
        for i, j in food1_list :
            food1_num += arr[i][j]
            food1_num += arr[j][i]

        food2 = tuple(set(range(N))-set(food1))

        food2_list = list(combinations(food2,2))
        food2_num = 0


        for i, j in food2_list :
            food2_num += arr[i][j]
            food2_num += arr[j][i]

        if min_num > abs(food1_num-food2_num) :
            min_num = abs(food1_num-food2_num)
    print("#{} {}".format(tc, min_num))
