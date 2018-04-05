import math

def get_num(n):
    temp_n = n
    s = 0
    i = 2
    while math.ceil(n) > i:
        n = temp_n / i
        if temp_n % i == 0:
            s += i
            s += int(n)
        i += 1
    return s+1

arr = [0 for i in range(100001)]
l = []
i = 220
while 100000 > i:
    if arr[i] == -1:
        i += 1
        continue
    n = get_num(i)
    if i == get_num(n) and n != i:
        l.append(i)
        l.append(n)
        #i = n
    arr[i] = -1
    if n < 100001:
        arr[n] = -1
    i += 1



for _ in range(int(input().strip())):
    n = int(input().strip())
    print(sum(filter(lambda x: x <= n, l)))
