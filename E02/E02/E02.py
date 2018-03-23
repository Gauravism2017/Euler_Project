def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2


def fib_smaller_N(N):
    n = 2
    array = []
    while fib(n) < N:
        array.append(fib(n))
        n = n+1
    return array

def find_even_sum(N):
    array = fib_smaller_N(N)
    new_array = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            new_array.append(array[i])
        else:
            continue
    sum_re = sum(new_array)
    return sum_re

T = int(input())
if(T >= 1 and T <= 10**5):
    for t in range(T):
        N = int(input())
        if(N >= 10 & N <=  4*10**16):
            print(find_even_sum(N))
        else:
            continue
else:
    exit





