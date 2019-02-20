import sys
import copy
sys.stdin = open("sample_input_16.txt","r")

T = int(input()) # 테스트케이스
for tc in range(T):
    N = int(input()) # N*N 행렬
    numbers = [list(map(int,input().split())) for _ in range(N)] # 행렬
    num_r = copy.deepcopy(numbers) # 행렬 틀
    result = [] # 결과물
    for t in range(3): # 90,180,270 세번
        for i in range(N): 
            num_s = []
            for j in range(N):
                num_s.append(numbers[-(j+1)][i]) # 90도 회전
            num_r[i] = num_s  # 회전된 1개의 행을 각 위치에 덮어씌우기
        numbers = copy.deepcopy(num_r) # 회전할 베이스 틀에 덮어씌우기
        for z in range(N):
            result.append(num_r[z]) # 결과물에 저장
    print(f"#{tc+1}")
    for x in range(N): # 슬라이싱을 위한 for문
        for y in result[x::N] : 
            print("".join(map(str,y)), end=" ") # 슬라이싱한 결과물을 3번씩 출력
        print() # 띄어쓰기