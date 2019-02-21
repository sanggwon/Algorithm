import sys
sys.stdin = open("sample_input_19.txt","r")

# T = int(input())
# for t in range(1,T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     max_num = -9999
#     sum_num = 0
#     for i in range(N):
#         sum_num += arr[i]
#         max_num = sum_num if sum_num > max_num else max_num
#         sum_num = 0 if sum_num < 0 else sum_num
#     print(f"#{t} {max_num}")


# def maxsum(arr):
#     n = len(arr)
#     arr_max = max(arr)
#     sum = 0
#     for i in range(n):
#         sum = max(sum, 0) + arr[i]
#         arr_max = max(sum, arr_max)
    
#     return arr_max

# T = int(input())

# for tc in range(T):
#     n = int(input())
#     nums = list(map(int, input().split()))
#     res = maxsum(nums)

#     print(f"#{tc+1} {res}")


T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_num = -9999
    sum_num = 0
    for i in range(N):
        sum_num += arr[i]
        if sum_num > max_num :
            max_num = sum_num
        if sum_num < 0 :
            sum_num =0
    print(f"#{t} {max_num}")