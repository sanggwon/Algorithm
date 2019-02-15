import sys
sys.stdin = open("sample_input_3.txt","r")

for i in range(int(input())):
    num = int(input())
    cards = sorted(input())
    
    card = {}
    for j in cards :
        card.update({j:cards.count(j)})

    card_value = 0
    for value in card.values() :
        if card_value < value :
            card_value = value

    card_key = ""
    for key in card.keys():
        if card.get(key) == card_value:
            card_key = key
            
        

    print(f"#{i+1} {card_key} {card_value}")

        

            



