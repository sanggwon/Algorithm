def card_count(N) :
    for i in N:
        if i in SDHC :
            a = SDHC.index(i)
            card[a][0] = ""
        else :
            card[a][0] += i
        if card[a][0] in card_copy[a] :
            return "ERROR"
        if len(card[a][0]) == 2:
            card_copy[a].append(card[a][0])
    for j in range(4) :
        card_cnt[j] = card_cnt[j]-len(card_copy[j])
    return ' '.join(map(str,card_cnt))


for tc in range(1,int(input())+1):
    N = input()
    SDHC = ["S","D","H","C"]
    card = []
    card_copy = []
    for _ in range(4):
        card.append([""])
    for _ in range(4):
        card_copy.append([])
    card_cnt = [13,13,13,13]

    print(f"#{tc} {card_count(N)}")