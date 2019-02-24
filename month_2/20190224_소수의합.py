import time
start_time = time.time()

def primes(n):
    seive = [False,False] + [True] * (n-1)
    for k in range(2,int(n**0.5+1.5)):
        if seive[k]:
            seive[k*2::k] = [False] * ((n-k)//k)
    return [x for x in range(n+1) if seive[x]] 

count = 0
lists = primes(1000)
for i in lists :
    for j in range(lists.index(i)+1,len(lists)):
        for x in range(lists.index(lists[j])+1,len(lists)):
            if i+lists[j]+lists[x] == 1000:
                count += 1
print("start_time", start_time)
print(count)
print("seconds",(time.time()-start_time))
