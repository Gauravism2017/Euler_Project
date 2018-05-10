def get_digit(n):
    if n <= 9:
        return n
    number_of_digits = 1
    number_of_numbers = get_number_of_numbers(number_of_digits)
    reduced_n = n
    number_of_numbers_so_far = 0
    while reduced_n > number_of_numbers * number_of_digits:
        reduced_n -= number_of_numbers * number_of_digits
        number_of_digits += 1
        number_of_numbers_so_far += number_of_numbers
        number_of_numbers = get_number_of_numbers(number_of_digits)
    reduced_n -= 1 # no zero, argh!
    number = reduced_n // number_of_digits + number_of_numbers_so_far + 1
    place = reduced_n % number_of_digits
    #print(reduced_n, number_of_digits, number_of_numbers_so_far, number, place)
    print(str(number)[place])
    return int(str(number)[place])

def get_number_of_numbers(number_of_digits):
    return 9 * (10 ** (number_of_digits - 1))

for i in range(int(input())):
    prod = 1
    #li = list(map(int, input().split()))
    a = 999999999999999999 - i 
    b = 999999999999999998 - i 
    c = 999999999999999997 - i 
    d = 999999999999999996 - i 
    e = 999999999999999995 - i 
    f = 999999999999999994 - i 
    g = 999999999999999993 - i 
    li = [a, b, c, d, e, f, g]
    for v in li:
        prod = prod * get_digit(v)
    print(prod)
#for i in range(1000):
#   print(get_digit(99999999999999999- i))