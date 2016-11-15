import time

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

tal = input("Hvilket fibonacci vil du have: ")

start_time = time.time()
ans = fib(tal)
print"Det", tal, "'te fibonacci er", ans,"Det tog", (time.time() - start_time),"at udregne"
