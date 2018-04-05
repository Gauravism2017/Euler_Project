def fact(n):
    value = 1
    while n > 1:
        value = value * n
        n = n - 1
    return value
def sum_num(n):
    array = []
    for i in str(n):
        array.append(int(i))
    return array


print(sum(sum_num(fact(10))))
for _ in range(int(input())):
    print(sum(sum_num(fact(int(input())))))

