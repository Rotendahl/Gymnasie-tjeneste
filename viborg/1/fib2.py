import time

def fib(n):
    fibs = [1,1]
    while(len(fibs) < n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[-1]

tal = input("Hvilket fibonacci vil du have: ")

start_time = time.time()
ans = fib(tal)
print "Det", tal, "'te fibonacci er", ans,"Det tog", (time.time() - start_time),"at udregne"
