def fib_to(n):
    fibs = [0, 1]
    temp = 0
    array = []
    for i in range(2, n+1):
        term = fibs[-1] + fibs[-2]
        if len(str(term)) > temp:
            temp = len(str(term))
            array.append(i)
        fibs.append(term)
    return fibs
import time
start = time.time()
t = fib_to(25000)
print(time.time()-start)
with open('fib.txt','w') as file:
    file.write("\n".join((str(j))for j in t))
#with open('fib1.txt','w') as file:
#    file.write("\n".join((str(j))for j in t1))
#for _ in range(int(input())):
#    print(t[int(input())-1])
"""t = 0
i = 20000
while(t <= 5000):
    array1 = (fib_to(i))
    term = array1[len(array1)-1]
    t = len(str(term))
    i += 1
print(i)
print(time.time()-start)"""


