import time
start = time.time()
memo = [0, 1] + [0] * 5000000
result = [0, 1] + [1] * 5000000

def collatzLength(n):
    if n <= 5000000:
        res = memo[n]
        if not res: res = memo[n] = 1 + collatzLength(3*n + 1 if n % 2 else n // 2)
    else:
        res = 1 + collatzLength(3*n + 1 if n % 2 else n // 2)
    return res

for n in range(2, 5000001):
    l = collatzLength(n)
    result[n] = n if l >= memo[result[n - 1]] else result[n - 1]
print(time.time()-start)

for _ in range(int(input())):
    print (result[int(input())])