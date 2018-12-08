import time
from functools import reduce
from math import sqrt

def factors(n):
        step = 2 if n%2 else 1
        li = sorted(list(set(reduce(list.__add__,([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))))
        return li[:-1]


def get_pair(nums, target_sum):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    array = []
    for num in nums:
        complement = target_sum - num
        li1 = [num, complement]
        array.append(li1)
    return array

def result(n):
    t = int((n+1)/2)
    li = list(range(1,t + 1))
    return get_pair(li, n) 

    

def abundant(n):
    if(sum(factors(n)) > n):
        return True
    else:
        return False


def array_abund():
    array_abundant = []
    for i in range(1,28123):
        if abundant(i):
            array_abundant.append(i)
    return array_abundant

array_abundant = array_abund()
def ornot(n):
    temp = "NO"
    result1 = result(n)
    for i in range(len(result1)):
        if result1[i][0] in array_abundant:
            if result1[i][1] in array_abundant:
                temp = "YES"
                break

    return temp

for _ in range(int(input())):
    n = int(input())
    if n < 24:
        print("NO")
    elif n > 28123:
        print("YES")
    else:
        print(ornot(n))
