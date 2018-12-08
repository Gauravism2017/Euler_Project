
from math import factorial as fact

T = int(input())
for t in range(T):
    for j in [input().split(" ")]:
        m =int(j[0])
        n = int(j[1])
    print((fact(m + n) // (fact(m) * fact(n))) % 1000000007)
