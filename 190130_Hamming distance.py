def solution(binaryA, binaryB):
    hamming_distance = 0
    if len(binaryA) > len(binaryB):
        binaryB = (len(binaryA) - len(binaryB))*"0"+ binaryB
    elif len(binaryA) < len(binaryB):
        binaryA = (len(binaryB) - len(binaryA))*"0"+ binaryA
    for i in range(len(binaryB)):
        if not binaryA[i] == binaryB[i] :
            hamming_distance += 1
    return hamming_distance
binaryA = "10010"
binaryB = "110"
ret = solution(binaryA, binaryB)

print("solution 함수의 반환 값은", ret, "입니다.")
