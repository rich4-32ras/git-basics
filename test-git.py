from functools import lru_cache


@lru_cache()
def f(n):
    count = 1
    for d in range(1, n // 2 + 1):
        if n % d == 0 and d % 2 != 0:
            count += 1
    if count == 6:
        return True

c = 0
for n in range(1000000, 2000000):
    if f(n):
        print(n)
        c += 1
        if c > 10:
            break
