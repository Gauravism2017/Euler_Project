
def pythag(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    return False

def finder(N):
    product = -1

    for a in range(1, int(N/3)):
        b = int((N*N -2*N*a)/(2*N -2*a))
        c = N - b -a
        if pythag(a, b, c):
            temp = a*b*c
            if(temp>product):
                product = temp
        else:
           continue
    return product
    

def main():
    T = int(input())
    if(T >= 1 and T <= 3000):
        for t in range(T):
            N = int(input())
            if(N >= 1 and N <= 3000):
                print(finder(N))
            else:
                continue
    else:
        exit

if __name__ == '__main__':
    main()

