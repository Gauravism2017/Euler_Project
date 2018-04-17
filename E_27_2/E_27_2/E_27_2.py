import time
def sieve(n):
     
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    array = []
    for p in range(2, n):
        if prime[p]:
            array.append(p)
    return array

def is_prime(n):
    """function to check if the number
    is prime or not"""
    for i in range(2,int(abs(n)**0.5)+1):
        if n%i == 0:
            return False
    return True
def quadratic(a, b, n):
    quadractic = n*n + a*n + b
    return quadractic


def main(n):
    prime_list = sieve(1000)
    array_count_main = []
    first, second = 0, 0
    count_temp = 0
    for b in range(1, n+1):
        if b in prime_list:
            for a in range(1, n+1):
                if (a % 2 != 0):
                    count_pos = 0
                    count_neg = 0
                    for i in range(0,n):
                        quad = quadratic(a,b,i)
                        quad1 = quadratic(a*(-1),b,i)
                        if is_prime(quad):
                            count_pos = count_pos + 1  
                        if is_prime(quad1):
                            count_neg = count_neg + 1
                    print(count_neg, count_pos, count_temp, a, b)
                    if (count_pos > count_temp):
                        count_temp = count_pos
                        first = a
                        second = b
                    elif (count_neg > count_temp):
                        count_temp = count_neg
                        first = a*(-1)
                        second = b
                    print(count_temp)
                    

    return first, second               
#n = int(input())
t0 = time.time()


print(main(int(input())))

print(time.time()-t0)



