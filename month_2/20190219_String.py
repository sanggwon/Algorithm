import sys
sys.stdin = open("sample_input_8.txt","r", encoding='UTF8')

for _ in range(10):
    T = input()
    N = input()
    N_len = len(N)
    S = input()
    count = 0
    for i in range(len(S)-1):
        if N == S[i:i+N_len]:
            count += 1

    print(f"#{T} {count}")
