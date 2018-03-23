T = int(input())
if(T >= 1 and T <= 10**5):
    for t in range(T):
        N = int(input())
        if(N >= 1 and N <= 10**9):
            total_sum = 0
            for i in range(N):
                if (i % 3 == 0 or i % 5 == 0):
                    total_sum = total_sum + i
            print(total_sum)
        else:
            continue
else:
    exit



