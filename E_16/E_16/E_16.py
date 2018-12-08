import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    num = 2 ** n
    #print(num)
    mystr = str(num)
    print(sum([ int(x) for x in mystr ]))
