def isPrince(*frogList):
    for elem in frogList:
        x = list(elem)
        if x[0] != "F":
            pass
        else :
            return elem   
        
print(isPrince('Alice', 'Bob', 'Frog'))      