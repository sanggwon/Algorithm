word = input()
lists = list(word)
words = []
for i in lists :
    if i != " " :
        i = "개굴"
        words.append(i)
    else :
        i = i   
        words.append(i)
print("".join(words))
