def sum(n):
    sum = (n * (n + 1)) / 2
    return sum

def sum_sq(n):
    sum = (n * (n+1)*(2*n+1)) / 6
    return sum

for t in range(int(input())):
    n = int(input())
    print(int(sum(n)*sum(n)- sum_sq(n)))


